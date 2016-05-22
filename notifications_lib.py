from __future__ import print_function
import boto3
from base64 import b64decode
import json
import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)



def send_to_slack(message_content):
	logger.info('sending to Slack.')

	with open('config.json') as config_file:
		config = json.load(config_file)

	slack_hook_url = "https://" + boto3.client('kms').decrypt(CiphertextBlob=b64decode(config['slack_webhook_url_encrypted']))['Plaintext']

	slack_message = {
    	'channel': config['slack_channel'],
    	'text': message_content,
    	# TODO: implement username: >"username": "aws-bot",
    	'icon_emoji': config['slack_emoji']
	}

	# TODO: make exception handling more granular (http errors for example)
	try:
		req = requests.post(slack_hook_url, json.dumps(slack_message))
	except Exception as e:
		logger.error('Error posting message to Slack:\n' + e)


	logger.info('done sending to Slack')


