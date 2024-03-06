[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppendixWebhookResendRequestInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | task identifier unique task identifier in our system in the UUID format you can specify up to 100 identifiers; each identifier in the task array must be specified as a separate object | [optional]

## Example

```python
from dataforseo_client.models.appendix_webhook_resend_request_info import AppendixWebhookResendRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixWebhookResendRequestInfo from a JSON string
appendix_webhook_resend_request_info_instance = AppendixWebhookResendRequestInfo.from_json(json)
# print the JSON string representation of the object
print AppendixWebhookResendRequestInfo.to_json()

# convert the object into a dict
appendix_webhook_resend_request_info_dict = appendix_webhook_resend_request_info_instance.to_dict()
# create an instance of AppendixWebhookResendRequestInfo from a dict
appendix_webhook_resend_request_info_form_dict = appendix_webhook_resend_request_info.from_dict(appendix_webhook_resend_request_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")