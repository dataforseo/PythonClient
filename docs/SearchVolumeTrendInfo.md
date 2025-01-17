# SearchVolumeTrendInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly** | **int** | search volume change in percent compared to the previous month | [optional] 
**quarterly** | **int** | search volume change in percent compared to the previous quarter | [optional] 
**yearly** | **int** | search volume change in percent compared to the previous year | [optional] 

## Example

```python
from dataforseo_client.models.search_volume_trend_info import SearchVolumeTrendInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SearchVolumeTrendInfo from a JSON string
search_volume_trend_info_instance = SearchVolumeTrendInfo.from_json(json)
# print the JSON string representation of the object
print(SearchVolumeTrendInfo.to_json())

# convert the object into a dict
search_volume_trend_info_dict = search_volume_trend_info_instance.to_dict()
# create an instance of SearchVolumeTrendInfo from a dict
search_volume_trend_info_from_dict = SearchVolumeTrendInfo.from_dict(search_volume_trend_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


