# DataforseoLabsErrorsResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the task | [optional] 
**datetime** | **str** | date and time when an error occurred in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**function** | **str** | corresponding API function | [optional] 
**error_code** | **int** | error code | [optional] 
**error_message** | **str** | error message or error URL error message (see full list) or URL that caused an error | [optional] 
**http_url** | **str** | URL that caused an error URL you used for making an API call | [optional] 
**http_method** | **str** | HTTP method | [optional] 
**http_code** | **int** | HTTP status code | [optional] 
**http_time** | **float** | time taken by HTTP request | [optional] 
**http_response** | **str** | HTTP response server response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_errors_result_info import DataforseoLabsErrorsResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsErrorsResultInfo from a JSON string
dataforseo_labs_errors_result_info_instance = DataforseoLabsErrorsResultInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsErrorsResultInfo.to_json()

# convert the object into a dict
dataforseo_labs_errors_result_info_dict = dataforseo_labs_errors_result_info_instance.to_dict()
# create an instance of DataforseoLabsErrorsResultInfo from a dict
dataforseo_labs_errors_result_info_form_dict = dataforseo_labs_errors_result_info.from_dict(dataforseo_labs_errors_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


