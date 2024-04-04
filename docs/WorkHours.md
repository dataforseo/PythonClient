# WorkHours


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timetable** | **Dict[str, Optional[List[WorkDayInfo]]]** | work hours timetable | [optional] 
**current_status** | **str** | current status of the establishment indicates whether the establishment is opened or closed | [optional] 

## Example

```python
from dataforseo_client.models.work_hours import WorkHours

# TODO update the JSON string below
json = "{}"
# create an instance of WorkHours from a JSON string
work_hours_instance = WorkHours.from_json(json)
# print the JSON string representation of the object
print WorkHours.to_json()

# convert the object into a dict
work_hours_dict = work_hours_instance.to_dict()
# create an instance of WorkHours from a dict
work_hours_form_dict = work_hours.from_dict(work_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


