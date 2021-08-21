# rain_alert
This application uses third party api to notify the user when it's raining.
# One Call API
The One Call API provides the following weather data for any geographical coordinates:

Current weather
Minute forecast for 1 hour
Hourly forecast for 48 hours
Daily forecast for 7 days
National weather alerts
Historical weather data for the previous 5 days
THESE ARE THE CONDITION ID'S THAT ARE USED FOR VARIOUS WHEATHER PURPOSES:
https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2

# twilio api docs:
SMS API
Twilio’s Programmable SMS API helps you add robust messaging capabilities to your applications.

Using this REST API, you can send and receive SMS messages, track the delivery of sent messages, and retrieve and modify message history.

Want more general information on Twilio and SMS? See our Programmable SMS overview and the SMS API pricing page.

Base URL
All URLs referenced in the API documentation have the following base:

https://api.twilio.com/2010-04-01
The API is served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.

You can control your connectivity into Twilio’s platform by including your specific edge location in the subdomain. This will allow you to bring Twilio’s public or private network connectivity closer to your applications for improved performance.

For instance, customers with infrastructure in Germany can make use of the frankfurt edge location by using this base URL:

https://api.frankfurt.us1.twilio.com/2010-04-01
If you have a private connection through Interconnect in Germany, you can make use of the frankfurt-ix edge location by using this base URL:

https://api.frankfurt-ix.us1.twilio.com/2010-04-01
SMS API authentication
HTTP requests to the API are protected with HTTP Basic authentication. To learn more about how Twilio handles authentication, please refer to our security documentation.

In short, you will use your Twilio Account SID as the username and your Auth Token as the password for HTTP Basic authentication with Twilio.

curl -G https://api.twilio.com/2010-04-01/Accounts \
     -u <YOUR_ACCOUNT_SID>:<YOUR_AUTH_TOKEN>
You can find your Account SID and Auth Token in the Console.

To learn more about authentication and interaction with the Twilio REST API, check out our documentation for requests to the API and Twilio’s response.

# Send messages with the SMS API
Twilio’s SMS API helps you send and manage messages programmatically:

To send an outbound SMS, WhatsApp, or Channels message with the API, POST to the Message resource.
You’ll also use the Message resource to fetch messages and list messages associated with your account.
You can also leverage the REST API to query metadata and manage your messages:

Delete or redact content from an existing message.
Track message feedback.
Fetch, update, or delete media associated with a message.
Fetch and update the short codes tied to your account.
Manage your account’s messaging services.
