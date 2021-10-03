import africastalking
import json

class SMS:
	def __init__(self):
		# Set your app credentials
		self.username = "yegonke"
		self.api_key = "67f0ca71b68b514114ea1500c97025c052d2c26b8bc95320a526d6acda06b616"

		# Initialize the SDK
		africastalking.initialize(self.username, self.api_key)

		# Get the SMS service
		self.sms = africastalking.SMS

	def send(self, mobile, otp):
		# Set the numbers you want to send to in international format
		recipients = [mobile]

		# Set your message
		message =  otp

		# Set your shortCode or senderId
		sender = "shortCode or senderId"
		try:
				# Thats it, hit send and we'll take care of the rest.
			response = self.sms.send(message, recipients)
			print(response)
		except Exception as e:
			# print ('Encountered an error while sending: %s' % str(e))
			response = 'Encountered an error while sending: %s' % str(e)
		return response