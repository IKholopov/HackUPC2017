import twitter
import json
import requests
import hackupc.settings as settings
from bestin.utils import convert_degs_to_decimal
from bestin.models import Activity
from bestin.process import content_analyzer

def analyze_feed(user):
    if user.social_auth.get().provider == 'instagram':
        process_instagram(user)
    if user.social_auth.get().provider == 'twitter':
        process_twitter(user)

def get_score(intput_text):
    return content_analyzer().process_text(intput_text)

def process_twitter(user):
    tokens = user.social_auth.get().extra_data["access_token"]
    oauth_key = tokens["oauth_token"]
    oauth_secret = tokens["oauth_token_secret"]
    api = twitter.Api(consumer_key=settings.SOCIAL_AUTH_TWITTER_KEY,
                        consumer_secret=settings.SOCIAL_AUTH_TWITTER_SECRET,
                        access_token_key=oauth_key,
                        access_token_secret=oauth_secret)
    statuses = api.GetUserTimeline(include_rts=False, count=20)
    charity_twitts = []
    geo_tagged = []
    for status in statuses:
        score = get_score(status.text)
        print(score)
        if score > 0:
            geo = status.coordinates
            place = status.place
            if geo is not None:
                geo = geo["coordinates"]
            elif place is not None:
                place = place["full_name"]
                responce = requests.get('http://maps.google.com/maps/api/geocode/json?address='+place)
                location = json.loads(responce.text)["results"][0]["geometry"]["location"]
                geo = [location["lng"], location["lat"]]
            print(geo)
            geo_str = str(geo)
            try:
                activity = Activity.objects.get(social_status_id=status.id)
            except Activity.DoesNotExist:
                charity_twitts.append(Activity.create(social_status_id=status.id, user_id=user, source=status.text,
                                score=score, geodata=geo_str))
                if geo is not None:
                    geo_tagged.append({"UserID": user.id, "text": status.text.replace('#', ' '),
                    "score": score, "lat": geo[1], "lon": geo[0]})

    Activity.objects.bulk_create(charity_twitts)
    adds = []
    print(geo_tagged)
    for tagged in geo_tagged:
        adds.append({"geometry": {"x": tagged["lon"]*10**5, "y": tagged["lat"]*10**5}, "attributes": tagged})
    print(adds)
    print(requests.post('https://services7.arcgis.com/0MAMn0h8N3f8X276/arcgis/rest/services/Social_Activity/FeatureServer/applyEdits?f=pjson&edits='+json.dumps([{"id": 0, "adds": adds}]),
            headers={'Content-type': 'application/json', 'Accept': 'text/plain'}).text)

    #print(api.GetStatus(status_id='837968179766886401'))
