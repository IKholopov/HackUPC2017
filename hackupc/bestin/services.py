import twitter
import json
import hackupc.settings as settings
from bestin.utils import convert_degs_to_decimal
from bestin.models import Activity

def analyze_feed(user):
    if user.social_auth.get().provider == 'instagram':
        process_instagram(user)
    if user.social_auth.get().provider == 'twitter':
        process_twitter(user)

def get_score(intput_text):
    return 10

def process_twitter(user):
    tokens = user.social_auth.get().extra_data["access_token"]
    oauth_key = tokens["oauth_token"]
    oauth_secret = tokens["oauth_token_secret"]
    api = twitter.Api(consumer_key=settings.SOCIAL_AUTH_TWITTER_KEY,
                        consumer_secret=settings.SOCIAL_AUTH_TWITTER_SECRET,
                        access_token_key=oauth_key,
                        access_token_secret=oauth_secret)
    statuses = api.GetUserTimeline(include_rts=False, count=200)
    charity_twitts = []
    for status in statuses:
        score = get_score(status.text)
        if score > 0:
            geo = status.coordinates
            if geo is not None:
                geo = str(geo["coordinates"])
            try:
                activity = Activity.objects.get(social_status_id=status.id)
            except Activity.DoesNotExist:
                charity_twitts.append(Activity.create(social_status_id=status.id, user_id=user, source=status.text,
                                score=score, geodata=geo))
    print(len(charity_twitts))
    Activity.objects.bulk_create(charity_twitts)

    #print(api.GetStatus(status_id='837968179766886401'))
