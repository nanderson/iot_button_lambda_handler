from __future__ import print_function
import json
import logging
import notifications_lib
import lambda_helper_lib

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info('loading function')

def lambda_handler(event, context):
	logger.info('loading lambda_handler')
	print(lambda_helper_lib.event_to_str(event))

	if lambda_helper_lib.is_real_event(event):
		if event['clickType'] == 'SINGLE':
			notifications_lib.send_to_slack('IoT Button - Single Click\n(voltage:' + event['batteryVoltage'] + ')')
		elif event['clickType'] == 'DOUBLE':
			notifications_lib.send_to_slack('IoT Button - Double Click\n(voltage:' + event['batteryVoltage'] + ')')
		elif event['clickType'] == 'LONG':
			notifications_lib.send_to_slack('IoT Button - Long Click\n(voltage:' + event['batteryVoltage'] + ')')
			print(lambda_helper_lib.context_to_str(context))
	else:
		notifications_lib.send_to_slack('IoT Button - test event')

	logger.info('leaving lambda_handler')
	return 'success'
