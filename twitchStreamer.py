# https://2.python-requests.org/en/master/
import requests
import smtplib

USER = "gacrok@gmail.com"
PASS = "PASSWORD" #abstracting my password right now until I know how to hide it while posting on git
data = "Riot Games is streaming right now"
s = smtplib.SMTP_SSL('smtp.mail.com',465)


# This is one of the routes where Twich expose data, https://dev.twitch.tv/docs
endpoint = "https://api.twitch.tv/helix/streams?"

headers = {"Client-ID": "0t8nw0vtyqvw9nmzy1i97qw4svwsix"}

# The previously set endpoint needs some parameter, here, the Twitcher we want to follow
# Disclaimer, I don't even know who this is, but he was the first one on Twich to have a live stream so I could have nice examples
params = {"user_login": "riotgames"}

# It is now time to make the actual request
response = requests.get(endpoint, params = params, headers = headers)
print(response.json())

stored_response = response.json()
streams = stored_response.get('data', [])

active = lambda stream: stream.get('type') == 'live'
active_stream = filter(active, streams)

#returns True if active_stream has one element
one_active_stream = any(active_stream)

print(one_active_stream)
if one_active_stream:
    s.login(USER, PASS)
    s.sendmail(USER, USER,data)
    s.quit()