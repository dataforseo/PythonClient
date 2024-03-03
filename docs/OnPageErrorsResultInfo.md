# OnPageErrorsResultInfo


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
from dataforseo_client.models.on_page_errors_result_info import OnPageErrorsResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageErrorsResultInfo from a JSON string
on_page_errors_result_info_instance = OnPageErrorsResultInfo.from_json(json)
# print the JSON string representation of the object
print OnPageErrorsResultInfo.to_json()

# convert the object into a dict
on_page_errors_result_info_dict = on_page_errors_result_info_instance.to_dict()
# create an instance of OnPageErrorsResultInfo from a dict
on_page_errors_result_info_form_dict = on_page_errors_result_info.from_dict(on_page_errors_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


