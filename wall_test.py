import time
import csv
import requests


def take_1000_posts():
    token = 'b285cce58a234246f180b164b08e2e8a7fccea60ea250b695691d6492bc81e65438d83ec993852d17f1eb'
    version = 5.126
    domain = 'bookflow'
    offset = 0
    count = 100
    all_posts = []

    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get', params={
            'access_token' : token,
            'v' : version,
            'domain' : domain,
            'count' : count,
            'offset': 0
            })
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
        time.sleep(0.5)
    return all_posts


def file_writer(data):
    with open('programming.csv', 'w') as f:
        a_pen = csv.writer(f)
        a_pen.writerow(('likes', 'body', 'url'))
        for post in data:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['size'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass

            a_pen.writerow((post['likes']['count'], post['text']))

all_posts = take_1000_posts()
file_writer(all_posts)
print(len(all_posts))