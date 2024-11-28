# PopularTimes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**popular_times_by_days** | **Dict[str, Optional[List[BusyWorkingTimeInfo]]]** | popular hours information about busy hours of the local establishment on each day of the week | [optional] 

## Example

```python
from dataforseo_client.models.popular_times import PopularTimes

# TODO update the JSON string below
json = "{}"
# create an instance of PopularTimes from a JSON string
popular_times_instance = PopularTimes.from_json(json)
# print the JSON string representation of the object
print(PopularTimes.to_json())

# convert the object into a dict
popular_times_dict = popular_times_instance.to_dict()
# create an instance of PopularTimes from a dict
popular_times_from_dict = PopularTimes.from_dict(popular_times_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


