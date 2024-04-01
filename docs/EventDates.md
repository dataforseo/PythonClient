# EventDates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_datetime** | **str** | date and time when the event starts if time zone is specified in the event, value will be returned in the UTC format: “yyyy-mm-ddThh-mm-ss+00:00” example: 2019-11-15T12:57:46+00:00 if time zone is not specified in the event, unspecified local time will be returned in the following format: “yyyy-mm-ddThh-mm-ss” example: 2019-11-15T12:57:46 | [optional] 
**end_datetime** | **str** | date and time when the event ends if time zone is specified in the event, value will be returned in the UTC format: “yyyy-mm-ddThh-mm-ss+00:00” example: 2019-11-15T12:57:46+00:00 if time zone is not specified in the event, unspecified local time will be returned in the following format: “yyyy-mm-ddThh-mm-ss” example: 2019-11-15T12:57:46 | [optional] 
**displayed_dates** | **str** | date or date range as it is displayed in SERP | [optional] 

## Example

```python
from dataforseo_client.models.event_dates import EventDates

# TODO update the JSON string below
json = "{}"
# create an instance of EventDates from a JSON string
event_dates_instance = EventDates.from_json(json)
# print the JSON string representation of the object
print(EventDates.to_json())

# convert the object into a dict
event_dates_dict = event_dates_instance.to_dict()
# create an instance of EventDates from a dict
event_dates_form_dict = event_dates.from_dict(event_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


