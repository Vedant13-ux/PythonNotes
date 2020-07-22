import urllib.request
import urllib.parse
import urllib.parse
import hidden
import oauth


def augment(url, parameters):
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'],
                                   secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])

    oath_request = oauth.OAuthRequest.from_consumer_and_token(
        consumer, token=token, http_method='GET', http_url=url, parameters=parameters)
    oath_request.sign_request(
        oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
    return oath_request.to_url()
