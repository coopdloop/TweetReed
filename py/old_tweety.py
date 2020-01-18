import json
import requests
import base64

# For dev
configfile = 'C:\\Users\\thecasual\\Desktop\\TweetReed\\config\\config.json'

with open(configfile) as c:
    config = json.load(c)

consumerkey=config['consumerkey']
consumersecret=config['consumersecret']
accesstokenkey=config['accesstokenkey']
accesstokensecret=config['accesstokensecret']

# Used for testing with burp
proxies = {
    "https" : "https://localhost:8080"
}

def getaccesstoken():
    oauthurl = 'https://api.twitter.com/oauth2/token'
    bearertoken = base64.b64encode((consumerkey + ":" + consumersecret).encode('utf-8')).decode("utf-8")
    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded;charset=UTF-8',
        'Authorization' : "Basic " + bearertoken
    }
    body = 'grant_type=client_credentials'
    r = requests.post(headers=headers, data=body, url = oauthurl, verify=False)
    if r.status_code == 200:
        return json.loads(r.text)['access_token']
    else:
        return "Request failed!"

def twitterrequest(accesstoken):
    # TODO
    twitterstatus = 'https://api.twitter.com/1.1/statuses/user_timeline.json?count=100&screen_name=twitterapi'
    headers = {
        "Authorization" : "Bearer " + accesstoken
    }
    r = requests.get(url=twitterstatus, headers=headers)
    print(r.text)


accesstoken = getaccesstoken()
print(accesstoken)
twitterrequest(accesstoken)