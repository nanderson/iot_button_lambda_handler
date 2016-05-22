# handler AWS IoT Button handler using Lambda
Opinionated and POC handler for the AWS IoT Button
https://aws.amazon.com/iot/button/

The button sends 3 different events corresponding to the type of click. Single, Double or Long click. Right now I
don't do anything special with these events other than logging the data and sending a Slack notification.


## Installation
Installation is somewhat manual at this point.

edit makefile to use proper AWS account number
make init
make deploy-new
configure IoT butting
set event source on lambda to the proper IoT button

### Configure config.json
cp config.json.example config.json
configure the Slack channel, emoji, username etc to your liking
slack web hook url:
make a KMS key in the proper region, I called mine 'DefaultKey'
aws kms encrypt --key-id alias/DefaultKey --plaintext "hooks.slack.com/services/....... (whatever your Slack webhook URL is)"
take that CiphertextBlob and drop it in config.json


### Initialize local project
make init
(basically just makes a virtualenv and pip installs 'requests')

### Deploy
make deploy

### Configure IoT Button (pointing it at this lambda)


## Future ideas
* Logging to Dynamo
* Home Automation system integration
* SMS notifications


