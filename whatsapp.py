# # Download the helper library from https://www.twilio.com/docs/python/install
# from twilio.rest import Client
#
#
# # Your Account Sid and Auth Token from twilio.com/console
# # DANGER! This is insecure. See http://twil.io/secure
# account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# auth_token = 'your_auth_token'
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#                               body='Hello there!',
#                               from_='whatsapp:+14155238886',
#                               to='whatsapp:+15005550006'
#                           )
#
# print(message.sid)


# import os
# # from twilio.rest import Client
# #
# #
# # client = Client()
# #
# # from_whatsapp_number="whatsapp:+447747208339"
# # Number_Format="whatsapp:+447795523201"
# # to_whatsapp_number="whatsapp:" + os.environ["Number_Format"]
# #
# # client.messages.create(body="Ahoy Adults",
# #                        from=from_whatsapp_number,
# #                        to=to_whatsapp_number)