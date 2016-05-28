import unittest

import iot_button


class FunctionalTest(unittest.TestCase):
    def test_1(self):
        event = {"batteryVoltage": "testing", "serialNumber": "testing", "not_a_real_clickType": "LONG"}
        context = {"aws_request_id": "foo",
                   "log_stream_name": "foo",
                   "invoked_function_arn": "foo",
                   "client_context": "",
                   "log_group_name": "foo",
                   "function_name": "foo",
                   "function_version": "$LATEST",
                   "identity": TestingCognitoIdentity(),
                   "memory_limit_in_mb": "128",
                   }

        self.assertEqual(iot_button.lambda_handler(event, context), 'success')


class TestingCognitoIdentity:
    foo = "foo"
    bar = "bar"

    def some_method(self):
        return True


if __name__ == '__main__':
    unittest.main()
