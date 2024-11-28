# BusyWorkingTimeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | [**WorkTimeInfo**](WorkTimeInfo.md) |  | [optional] 
**popular_index** | **int** | popularity index relative time-bound popularity index measured from 0 to 100; higher value corresponds to a busier time of a day | [optional] 

## Example

```python
from dataforseo_client.models.busy_working_time_info import BusyWorkingTimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusyWorkingTimeInfo from a JSON string
busy_working_time_info_instance = BusyWorkingTimeInfo.from_json(json)
# print the JSON string representation of the object
print(BusyWorkingTimeInfo.to_json())

# convert the object into a dict
busy_working_time_info_dict = busy_working_time_info_instance.to_dict()
# create an instance of BusyWorkingTimeInfo from a dict
busy_working_time_info_from_dict = BusyWorkingTimeInfo.from_dict(busy_working_time_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


