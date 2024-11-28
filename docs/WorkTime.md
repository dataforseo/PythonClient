# WorkTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_hours** | [**WorkHours**](WorkHours.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.work_time import WorkTime

# TODO update the JSON string below
json = "{}"
# create an instance of WorkTime from a JSON string
work_time_instance = WorkTime.from_json(json)
# print the JSON string representation of the object
print(WorkTime.to_json())

# convert the object into a dict
work_time_dict = work_time_instance.to_dict()
# create an instance of WorkTime from a dict
work_time_from_dict = WorkTime.from_dict(work_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


