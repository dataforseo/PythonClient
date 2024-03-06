[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BusinessDataErrorsResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the task | [optional]
**datetime** | **str** | date and time when an error occurred in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**function** | **str** | corresponding API function | [optional]
**error_code** | **int** | error code | [optional]
**error_message** | **str** | error message or error URL error message (see full list) or URL that caused an error | [optional]
**http_url** | **str** | URL that caused an error URL you used for making an API call or pingback/postback URL | [optional]
**http_method** | **str** | HTTP method | [optional]
**http_code** | **int** | HTTP status code | [optional]
**http_time** | **float** | time taken by HTTP request for tasks set with a pingback/postback, this field will show the time it took your server to respond | [optional]
**http_response** | **str** | HTTP response server response | [optional]

## Example

```python
from dataforseo_client.models.business_data_errors_result_info import BusinessDataErrorsResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataErrorsResultInfo from a JSON string
business_data_errors_result_info_instance = BusinessDataErrorsResultInfo.from_json(json)
# print the JSON string representation of the object
print BusinessDataErrorsResultInfo.to_json()

# convert the object into a dict
business_data_errors_result_info_dict = business_data_errors_result_info_instance.to_dict()
# create an instance of BusinessDataErrorsResultInfo from a dict
business_data_errors_result_info_form_dict = business_data_errors_result_info.from_dict(business_data_errors_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")