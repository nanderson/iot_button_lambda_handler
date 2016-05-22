PACKAGE=iot_button.zip
SOURCES=iot_button.py notifications_lib.py lambda_helper_lib.py config.json
LIBS=requests/ requests-2.10.0.dist-info/
LIBS_PATH=lib/python2.7/site-packages/
AWS_FUNCTION_DESCRIPTION="An AWS Lambda function that reacts to the press of an IoT Button"
AWS_FUNCTION_NAME=iot_button
AWS_HANDLER_NAME=iot_button.lambda_handler
AWS_ROLE=arn:aws:iam::656363001641:role/lambda_basic_execution
AWS_HANDLER=iot_button.lambda_handler
AWS_REGION=us-west-2


all: package


package:
	rm -f $(PACKAGE)
	zip -rq $(PACKAGE) $(SOURCES)
	ARCHIVE=`readlink -m $(PACKAGE)`; pushd $(LIBS_PATH); zip -rq $$ARCHIVE $(LIBS)

deploy: package
	aws lambda update-function-code \
		--function-name $(AWS_FUNCTION_NAME) \
		--region us-west-2 \
		--zip-file fileb://$(PACKAGE) \
		--publish 

deploy-new: package
	aws lambda create-function \
		--region $(AWS_REGION) \
		--function-name $(AWS_FUNCTION_NAME) \
		--zip-file fileb://$(PACKAGE) \
		--role $(AWS_ROLE)  \
		--handler $(AWS_HANDLER) \
		--runtime python2.7 \
		--description $(AWS_FUNCTION_DESCRIPTION) \
		--timeout 5 \
		--memory-size 128

invoke:
	aws lambda invoke \
		--invocation-type RequestResponse \
		--function-name $(AWS_FUNCTION_NAME) \
		--region $(AWS_REGION) \
		--log-type Tail \
		--payload '{"testing":"true", "source":"makefile", "project":"$(AWS_FUNCTION_NAME)"}' \
		/tmp/$(AWS_FUNCTION_NAME)_output.txt
	echo
	cat /tmp/$(AWS_FUNCTION_NAME)_output.txt
	echo

init:
	virtualenv .; source bin/activate; pip install requests
