# WEATHER API PROVIDER: https://home.openweathermap.org/api_keys
# FIND YOUR CITY'S COORDINATES: https://www.latlong.net/
# SENDING MESSAGES API: https://www.twilio.com/try-twilio
# TO TEST YOUR CODE CAN CHOOSE THE PLACE WHERE IT IS RAINING NOW: https://www.ventusky.com/
# HOW TO MAKE YOUR TWILIO WORKS ON FREE CLOUD ACCOUNTS:https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/
# FREE ACCOUNT FOR CODE RUNNING:

import requests
# use this line of code when you place your app on free account cloud like: https://www.pythonanywhere.com/
# import os
from twilio.rest import Client
# use this line of code when you place your app on free account cloud like: https://www.pythonanywhere.com/
# from twilio.http.http_client import TwilioHttpClient

# USE HERE YOUR AUTH TOKEN AND API KEY FROM YOUR TWILIO API ACCOUNT:
account_sid = "xxxxxxx"
auth_token = "xxxxxxx"

# USE HERE YOUR API KEY AND ENDPOINT FROM YOUR WEATHER API ACCOUNT:
api_key = "xxxxxx"
ENDPOINT = "xxxxxx"

# PUT HERE COORDINATES OF YOUR CITY:
weather_params = {
    "lat": 47.997189,
    "lon": 7.853770,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # # use this line of code when you place your app on free account cloud like: https://www.pythonanywhere.com/
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token)
    # use this line of code when you place your app on free account cloud like: https://www.pythonanywhere.com/
    # client = Client(account_sid, auth_token, http_client=proxy_client)

    # CREATE YOUR MESSAGE YOU WANT TO SEND:
    message = client.messages \
        .create(
        body="It's going to rain today! Don't forget your umbrella!",
        # put here the phone number that twilio provided to your account:
        from_='xxxxxx',
        # put here the phone number you want to send messages:
        to='xxxxxx'
    )
    print(message.status)

