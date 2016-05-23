

def context_to_str(context):
	context_str = '_Context:_\n'
	context_str += '```'
	context_str += 'context.function_name:' + context.function_name + '\n'
	context_str += 'context.function_version:' + context.function_version + '\n'
	context_str += 'context.invoked_function_arn:' + context.invoked_function_arn + '\n'
	context_str += 'context.memory_limit_in_mb:' + context.memory_limit_in_mb + '\n'
	context_str += 'context.aws_request_id:' + context.aws_request_id + '\n'
	context_str += 'context.log_group_name:' + context.log_group_name + '\n'
	context_str += 'context.log_stream_name:' + context.log_stream_name + '\n'

	if (context.identity is not None):
		context_str += 'context.identity.cognito_identity_id:' + safe_get(context.identity.cognito_identity_id) + '\n'
		context_str += 'context.identity.cognito_identity_pool_id:' + safe_get(context.identity.cognito_identity_pool_id) + '\n'
	else:
		context_str += 'context.identity:--None--\n'

	if (context.client_context is not None):
		context_str += 'context.client_context.client.installation_id:' + context.client_context.client.installation_id + '\n'
		context_str += 'context.client_context.client.app_title:' + context.client_context.client.app_title + '\n'
		context_str += 'context.client_context.client.app_version_name:' + context.client_context.client.app_version_name + '\n'
		context_str += 'context.client_context.client.app_version_code:' + context.client_context.client.app_version_code + '\n'
		context_str += 'context.client_context.client.app_package_name:' + context.client_context.client.app_package_name + '\n'
		context_str += 'context.client_context.custom:' + str(context.client_context.custom) + '\n'
		context_str += 'context.client_context.env:' + str(context.client_context.env) + '\n'
	else:
		context_str += 'context.client_context:--None--\n'
	
	context_str += 'context.get_remaining_time_in_millis:' + str(context.get_remaining_time_in_millis()) + '\n'
	context_str += '```'

	return context_str


def event_to_str(event):
	event_str = '_Event:_\n'
	event_str += '```'
	try:
		event_str += 'batteryVoltage:' + event['batteryVoltage'] + '\n'
		event_str += 'serialNumber:' + event['serialNumber'] + '\n'
		event_str += 'clickType:' + event['clickType'] + '\n'
	except KeyError:
		event_str += '--test event--\n'

	event_str += '```'
	return event_str


def is_real_event(event):
	if 'clickType' in event:
		return True
	else:
		return False



def safe_get(index):
	if (index is not None):
		return index
	else:
		return '--None--'