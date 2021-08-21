import requests
from twilio.rest import Client
auth_token = "dcb040039ee3b30c025851f7b0481fed"
account_sid = "AC0147920d6910b340e8d76be4896a241d"
api_key = "618acf11896bda8b792e2829fb320fc1"
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
# lat = 13.082680
# long = 80.270721



weather_params = {
    "lat" : 30.592850,
    "lon" : 114.305542,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}


response = requests.get(OWN_ENDPOINT, params=weather_params)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
#check = (weather_data["hourly"][0]["weather"][0]["id"])
response.raise_for_status()
will_rain = False
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True
        

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
             .create(
                     body="It's going to rain today.Please remember to bring an umbrella☔.",
                     from_='+17816136465',
                     to='your verified number'
                 )
    print(message.status)
