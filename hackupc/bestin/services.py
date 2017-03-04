import twitter
import json
import hackupc.settings as settings

def analyze_feed(user):
    if user.provider == 'instagram':
        process_instagram(user)
    if user.provider == 'twitter':
        process_twitter(user)

def process_twitter(user):
    tokens = user.extra_data["access_token"]
    oauth_key = tokens["oauth_token"]
    oauth_secret = tokens["oauth_token_secret"]
    api = twitter.Api(consumer_key=settings.SOCIAL_AUTH_TWITTER_KEY,
                        consumer_secret=settings.SOCIAL_AUTH_TWITTER_SECRET,
                        access_token_key=oauth_key,
                        access_token_secret=oauth_secret)
    print(api.GetUserTimeline(include_rts=False, count=200))
