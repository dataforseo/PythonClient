# AppendixStatusEndpointsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | name of the endpoint the list of possible endpoints: task_get task_post live postback/pingback | [optional] 
**status** | **str** | current status you can find all information about the statuses of our endpoints for the last 60 days here the list of possible current statuses: major_outage partial_outage long_response_time long_execution_time webhook_delay send_delay | [optional] 

## Example

```python
from dataforseo_client.models.appendix_status_endpoints_info import AppendixStatusEndpointsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixStatusEndpointsInfo from a JSON string
appendix_status_endpoints_info_instance = AppendixStatusEndpointsInfo.from_json(json)
# print the JSON string representation of the object
print(AppendixStatusEndpointsInfo.to_json())

# convert the object into a dict
appendix_status_endpoints_info_dict = appendix_status_endpoints_info_instance.to_dict()
# create an instance of AppendixStatusEndpointsInfo from a dict
appendix_status_endpoints_info_from_dict = AppendixStatusEndpointsInfo.from_dict(appendix_status_endpoints_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


