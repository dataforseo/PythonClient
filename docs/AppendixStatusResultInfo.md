# AppendixStatusResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | **str** | name of the API the list of APIs: serp keywords_data appendix dataforseo_labs domain_analytics merchant on_page business_data backlinks app_data content_analysis content_generation | [optional] 
**status** | **str** | current status you can find all information about your API statuses for the last 60 days here the list of possible current statuses: major_outage partial_outage long_response_time long_execution_time webhook_delay send_delay | [optional] 
**endpoints** | [**List[AppendixStatusEndpointsInfo]**](AppendixStatusEndpointsInfo.md) | array of objects that contain status information for API endpoints | [optional] 

## Example

```python
from dataforseo_client.models.appendix_status_result_info import AppendixStatusResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixStatusResultInfo from a JSON string
appendix_status_result_info_instance = AppendixStatusResultInfo.from_json(json)
# print the JSON string representation of the object
print(AppendixStatusResultInfo.to_json())

# convert the object into a dict
appendix_status_result_info_dict = appendix_status_result_info_instance.to_dict()
# create an instance of AppendixStatusResultInfo from a dict
appendix_status_result_info_form_dict = appendix_status_result_info.from_dict(appendix_status_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


