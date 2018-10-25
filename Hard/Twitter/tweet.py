
# importing the module 
import tweepy 
  
# personal details 
consumer_key ="2URvdjvosSqkVE99zou14s0j2"
consumer_secret ="OiOAEhsknVsYtn7lEoxAF0zTQYPasJ2CMhjJndagZAn0xOBldE"
access_token ="1423408446-r6nt1a8rmc3yKi7xUUjv521JC8IMJAwyWdpCOiW"
access_token_secret ="KmFpOa7jkyxW3K8B4kWxD6Rj4tl3bEChQTGgI5bI9BO2E"
  
# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
  
# update the status 
api.update_status(status ="Hello Everyone !!") 

