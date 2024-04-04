# WorkInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_hours** | [**WorkHours**](WorkHours.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.work_info import WorkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WorkInfo from a JSON string
work_info_instance = WorkInfo.from_json(json)
# print the JSON string representation of the object
print WorkInfo.to_json()

# convert the object into a dict
work_info_dict = work_info_instance.to_dict()
# create an instance of WorkInfo from a dict
work_info_form_dict = work_info.from_dict(work_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


