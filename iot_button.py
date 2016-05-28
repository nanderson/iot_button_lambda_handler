from __future__ import print_function
import json
import logging
import notifications_lib
import lambda_helper_lib

logger = logging.getLogger()
#logger.setLevel(logging.INFO)
logging.basicConfig()

logger.info('loading function')

def lambda_handler(event, context):
    logger.info('loading lambda_handler')
    logger.info(json.dumps(event))

    if lambda_helper_lib.is_real_event(event):
        if event['clickType'] == 'SINGLE':
            notifications_lib.send_to_slack('*IoT Button - Single Click*\n(voltage:' + event['batteryVoltage'] + ')')
        elif event['clickType'] == 'DOUBLE':
            notifications_lib.send_to_slack(
                '*IoT Button - Double Click*\n(voltage:' + event['batteryVoltage'] + ')\n\n_Event:_```' + json.dumps(
                    event) + '```')
        elif event['clickType'] == 'LONG':
            notifications_lib.send_to_slack(
                '*IoT Button - Long Click*\n(voltage:' + event['batteryVoltage'] + ')\n\n_Event:_```' + json.dumps(
                    event) + '```\n_Context_```' + lambda_helper_lib.context_property_iterator(context) + '```')
        # print(lambda_helper_lib.context_to_str(context))
    else:
        notifications_lib.send_to_slack('*IoT Button - test event*\n```' + json.dumps(event) + '```')

    logger.info('leaving lambda_handler')
    return 'success'
