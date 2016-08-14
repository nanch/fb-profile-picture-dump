import requests
import json
import urllib2
import webbrowser
from pprint import pprint

token = ''
api_url = 'https://graph.facebook.com/v2.7/'
params = {'access_token' : token}


def extractFriends():
    call = "me/taggable_friends?fields=name,picture.width(9999).height(9999).type(large)&limit=5000"
    response = requests.get(api_url + call, params=params)
    r = (json.loads(response.content))
    #pprint(r)
    for f in r['data']:
        #print f['name']
        p_url = str(f['picture']['data']['url'])
        #print p_url

        opener1 = urllib2.build_opener()
        page1 = opener1.open(p_url)
        my_picture = page1.read()

        filename = f['name']+"_"+f['id']+".jpg"
        print(filename + " downloaded...")
        fout = open('images/'+filename, "wb")
        fout.write(my_picture)
        fout.close()

extractFriends()