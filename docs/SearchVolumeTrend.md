# SearchVolumeTrend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly** | **int** | search volume change in percent compared to the previous month | [optional] 
**quarterly** | **int** | search volume change in percent compared to the previous quarter | [optional] 
**yearly** | **int** | search volume change in percent compared to the previous year | [optional] 

## Example

```python
from dataforseo_client.models.search_volume_trend import SearchVolumeTrend

# TODO update the JSON string below
json = "{}"
# create an instance of SearchVolumeTrend from a JSON string
search_volume_trend_instance = SearchVolumeTrend.from_json(json)
# print the JSON string representation of the object
print(SearchVolumeTrend.to_json())

# convert the object into a dict
search_volume_trend_dict = search_volume_trend_instance.to_dict()
# create an instance of SearchVolumeTrend from a dict
search_volume_trend_from_dict = SearchVolumeTrend.from_dict(search_volume_trend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


