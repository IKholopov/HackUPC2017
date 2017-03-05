import twitter
import json
import requests
from pprint import pprint
import hackupc.settings as settings
from bestin.utils import convert_degs_to_decimal
from bestin.models import Activity
from bestin.process import content_analyzer
from instagram_scrabber import get_self_media
def analyze_feed(user):
    if user.social_auth.get().provider == 'instagram':
        process_instagram(user)
    if user.social_auth.get().provider == 'twitter':
        process_twitter(user)

def get_score(intput_text):
    return content_analyzer().process_text(intput_text)

def process_instagram(user):
    token = user.social_auth.get().extra_data["access_token"]
    posts = get_self_media(token)
    charity_twitts = []
    geo_tagged = []
    for post in posts:
        score = get_score(post["text"])
        print(score)
        if score > 0:
            geo = [post["lng"], post["lat"]]
            post_id =int(post["id"].split('_')[0])%1000000
            if geo[0] is not None:
                print(geo)
                geo_str = str(geo)
            try:
                activity = Activity.objects.get(social_status_id=post_id)
            except Activity.DoesNotExist:
                charity_twitts.append(Activity.create(social_status_id=post_id, user_id=user, source=post["text"],
                                score=score, geodata=geo_str))
                if geo is not None:
                    geo_tagged.append({"UserID": user.id, "text": post["text"].replace('#', ' '),
                    "score": score, "lat": geo[1], "lon": geo[0]})
    Activity.objects.bulk_create(charity_twitts)
    adds = []
    print(geo_tagged)
    for tagged in geo_tagged:
        adds.append({"geometry": {"x": 1.1*tagged["lon"]*10**5, "y": 1.2225*tagged["lat"]*10**5}, "attributes": tagged})
    print(adds)
    print(requests.post('https://services7.arcgis.com/0MAMn0h8N3f8X276/arcgis/rest/services/Social_Activity/FeatureServer/applyEdits?f=pjson&edits='+json.dumps([{"id": 0, "adds": adds}]),
            headers={'Content-type': 'application/json', 'Accept': 'text/plain'}).text)

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
            geo_str = str(geo)
            status_id = status.id % 1000000
            try:
                activity = Activity.objects.get(social_status_id=status_id)
            except Activity.DoesNotExist:
                charity_twitts.append(Activity.create(social_status_id=status_id, user_id=user, source=status.text,
                                score=score, geodata=geo_str))
                if geo is not None:
                    geo_tagged.append({"UserID": user.id, "text": status.text.replace('#', ' '),
                    "score": score, "lat": geo[1], "lon": geo[0]})

    Activity.objects.bulk_create(charity_twitts)
    adds = []
    print(geo_tagged)
    for tagged in geo_tagged:
        adds.append({"geometry": {"x": 1.1*tagged["lon"]*10**5, "y": 1.2225*tagged["lat"]*10**5}, "attributes": tagged})
    print(adds)
    print(requests.post('https://services7.arcgis.com/0MAMn0h8N3f8X276/arcgis/rest/services/Social_Activity/FeatureServer/applyEdits?f=pjson&edits='+json.dumps([{"id": 0, "adds": adds}]),
            headers={'Content-type': 'application/json', 'Accept': 'text/plain'}).text)

    #print(api.GetStatus(status_id='837968179766886401'))
