import tweepy 


api_key ="2URvdjvosSqkVE99zou14s0j2"
api_secret ="OiOAEhsknVsYtn7lEoxAF0zTQYPasJ2CMhjJndagZAn0xOBldE"  
access_token ="1423408446-r6nt1a8rmc3yKi7xUUjv521JC8IMJAwyWdpCOiW"
access_token_secret ="KmFpOa7jkyxW3K8B4kWxD6Rj4tl3bEChQTGgI5bI9BO2E"
  
auth = tweepy.OAuthHandler(api_key, api_secret) 
  
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 

print("\n Enter the status which you want to update :")
x=input()
api.update_status(status =x) 

