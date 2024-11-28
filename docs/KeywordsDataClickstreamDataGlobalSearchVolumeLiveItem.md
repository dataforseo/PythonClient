# KeywordsDataClickstreamDataGlobalSearchVolumeLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character) | [optional] 
**search_volume** | **int** | clickstream-based average monthly search volume rate represents the (approximate) number of searches for the given keyword idea based on clickstream you can learn more about clickstream search volume in this Help Center article | [optional] 
**country_distribution** | [**List[CountryDistribution]**](CountryDistribution.md) | distribution of clickstream by countries represents clickstream-based search volume in available countries, as well as its respective percentage of global search volume | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_clickstream_data_global_search_volume_live_item import KeywordsDataClickstreamDataGlobalSearchVolumeLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataClickstreamDataGlobalSearchVolumeLiveItem from a JSON string
keywords_data_clickstream_data_global_search_volume_live_item_instance = KeywordsDataClickstreamDataGlobalSearchVolumeLiveItem.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataClickstreamDataGlobalSearchVolumeLiveItem.to_json())

# convert the object into a dict
keywords_data_clickstream_data_global_search_volume_live_item_dict = keywords_data_clickstream_data_global_search_volume_live_item_instance.to_dict()
# create an instance of KeywordsDataClickstreamDataGlobalSearchVolumeLiveItem from a dict
keywords_data_clickstream_data_global_search_volume_live_item_from_dict = KeywordsDataClickstreamDataGlobalSearchVolumeLiveItem.from_dict(keywords_data_clickstream_data_global_search_volume_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


