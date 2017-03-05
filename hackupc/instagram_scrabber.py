__author__ = 'Security'
import urllib.request as r
import json
from pprint import pprint
ACCESS_TOKEN = "822117162.e9ef95d.16e81916674b46f9a9988a052a53fe7c"

"""
###                                 ^^   ^^
### ПЕП-8 идет нахуй                00   00
###                                  \___/
"""


def pictures_by_location(lat, lng, dist=5000):
    """
    example of request_url: "https://api.instagram.com/v1/media/search?lat=48.858844&lng=2.294351&access_token=ACCESS-TOKEN"

    :return: {'image_url': image_url, 'instagram_link': link, 'lat': lat, 'lng': lng, 'user_name': user_name, 'text': text})
    """
    r_url = "https://api.instagram.com/v1/media/search?distance="+str(dist)+"&lat=" + str(lat) + "&lng=" + str(lng) + "&access_token=" + str(ACCESS_TOKEN)
    data = r.urlopen(r_url).read().decode('utf8')
    data = json.loads(data)
    results = []
    pprint(data['data'])
    for d in data['data']:
        image_url = d['images']['standard_resolution']['url']
        link = d['link']
        lat = d['location']['latitude']
        lng = d['location']['longitude']
        id = d['id']
        user_name = d['user']['username']
        text = d['caption']['text']
        results.append({'id': id, 'image_url': image_url, 'instagram_link': link, 'lat': lat, 'lng': lng, 'user_name': user_name, 'text': text})
    return results

def get_user_info(token):
    """
    example of request_url:
    https://api.instagram.com/v1/users/self/?access_token=ACCESS-TOKEN

    :return:
    """

    r_url = "https://api.instagram.com/v1/users/self/?access_token=" + str(token)
    data = r.urlopen(r_url).read().decode('utf8')
    data = json.loads(data)
    # pprint(data)
    return {'bio_title': data['data']['bio'],
     'user_name': data['data']['username'],
     'profile_picture': data['data']['profile_picture']}

def get_self_media(token):
    """
    example of request_url:
    ttps://api.instagram.com/v1/users/self/media/recent/?access_token=ACCESS-TOKEN

    :return:
    """
    r_url = "https://api.instagram.com/v1/users/self/media/recent/?access_token=" + str(token)
    data = r.urlopen(r_url).read().decode('utf8')
    data = json.loads(data)
    # pprint(data)

    results = []
    for d in data['data']:
        image_url = d['images']['standard_resolution']['url']
        link = d['link']
        user_name = d['user']['username']
        text = d['caption']['text']
        id = d['id']
        if d['location'] is not None:
            lat = d['location']['latitude']
            lng = d['location']['longitude']
        else:
            lat = lng = None
        results.append({'id': id, 'image_url': image_url, 'instagram_link': link, 'lat': lat, 'lng': lng, 'user_name': user_name, 'text': text})
    return results



# pictures_by_location(55.929597, 37.519426)
# get_user_info(ACCESS_TOKEN)
# get_self_media(ACCESS_TOKEN)
