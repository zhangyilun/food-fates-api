import argparse
import json
import pprint
import sys
import urllib
import urllib2
import oauth2

def request(host, path, url_params=None):
    url_params = url_params or {}
    url = 'http://{0}{1}?'.format(host, urllib.quote(path.encode('utf8')))

    consumer = oauth2.Consumer(app.config['CONSUMER_KEY'], app.config['CONSUMER_SECRET'])
    oauth_request = oauth2.Request(method="GET", url=url, parameters=url_params)

    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': app.config['TOKEN'],
            'oauth_consumer_key': app.config['CONSUMER_KEY']
        }
    )
    token = oauth2.Token(app.config['TOKEN'], app.config['TOKEN_SECRET'])
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()
    
    print u'Querying {0} ...'.format(url)

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response