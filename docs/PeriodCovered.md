# PeriodCovered


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | date and time when the period starts in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2020-03-02 02:00:00 +00:00 | [optional] 
**end_date** | **str** | date and time when the period ends in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2022-12-09 02:00:00 +00:00 | [optional] 
**displayed_date** | **str** | period displayed in SERP example: Mar 2, 2020 - Dec 9, 2022 | [optional] 

## Example

```python
from dataforseo_client.models.period_covered import PeriodCovered

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodCovered from a JSON string
period_covered_instance = PeriodCovered.from_json(json)
# print the JSON string representation of the object
print(PeriodCovered.to_json())

# convert the object into a dict
period_covered_dict = period_covered_instance.to_dict()
# create an instance of PeriodCovered from a dict
period_covered_from_dict = PeriodCovered.from_dict(period_covered_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


