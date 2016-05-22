# handler AWS IoT Button handler using Lambda
Lambda handler for the AWS IoT Button

(https://aws.amazon.com/iot/button/)

The IoT button sends 3 different events corresponding to the type of click. Single, Double or Long click. Right now I
don't do anything special with these events other than sending a Slack notification.


## Installation
Installation is somewhat manual at this point:

1. edit makefile to use proper AWS account number

2. copy config.json.example to config.json and edit (see below for encrypted Slack URL)

3. Make and deploy:
```shell
  make init
  make deploy-new
```

4. configure IoT button (see below)

5. set event source on lambda to the proper IoT button

### Configure config.json

```shell
  cp config.json.example config.json
```

configure the Slack channel, emoji, username etc to your liking

make a KMS key in the proper region, I called mine 'DefaultKey'

```shell
  aws kms encrypt --key-id alias/DefaultKey --plaintext "hooks.slack.com/services/....... (whatever your Slack webhook URL is)"
```

take that CiphertextBlob and drop it in config.json


### Configure IoT Button (pointing it at this lambda)

TODO: need to fill this section in

## Future ideas
* Logging to Dynamo
* Home Automation system integration
* SMS notifications


