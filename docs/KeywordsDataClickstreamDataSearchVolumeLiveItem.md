# KeywordsDataClickstreamDataSearchVolumeLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword provided in the POST array | [optional] 
**search_volume** | **int** | current search volume rate of a keyword | [optional] 
**monthly_searches** | [**List[MonthlySearches]**](MonthlySearches.md) | monthly search volume rates array of objects with search volume rates in a certain month of a year | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_clickstream_data_search_volume_live_item import KeywordsDataClickstreamDataSearchVolumeLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataClickstreamDataSearchVolumeLiveItem from a JSON string
keywords_data_clickstream_data_search_volume_live_item_instance = KeywordsDataClickstreamDataSearchVolumeLiveItem.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataClickstreamDataSearchVolumeLiveItem.to_json())

# convert the object into a dict
keywords_data_clickstream_data_search_volume_live_item_dict = keywords_data_clickstream_data_search_volume_live_item_instance.to_dict()
# create an instance of KeywordsDataClickstreamDataSearchVolumeLiveItem from a dict
keywords_data_clickstream_data_search_volume_live_item_from_dict = KeywordsDataClickstreamDataSearchVolumeLiveItem.from_dict(keywords_data_clickstream_data_search_volume_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


