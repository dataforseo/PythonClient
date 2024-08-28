# KeywordsDataClickstreamDataBulkSearchVolumeLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character) | [optional] 
**search_volume** | **int** | clickstream-based average monthly search volume rate represents the (approximate) number of searches for the given keyword idea based on clickstream you can learn more about clickstream search volume in this Help Center article | [optional] 
**monthly_searches** | [**List[MonthlySearches]**](MonthlySearches.md) | monthly searches represents the (approximate) number of searches on this keyword idea (as available for the past twelve months), targeted to the specified geographic locations | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_clickstream_data_bulk_search_volume_live_item import KeywordsDataClickstreamDataBulkSearchVolumeLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataClickstreamDataBulkSearchVolumeLiveItem from a JSON string
keywords_data_clickstream_data_bulk_search_volume_live_item_instance = KeywordsDataClickstreamDataBulkSearchVolumeLiveItem.from_json(json)
# print the JSON string representation of the object
print KeywordsDataClickstreamDataBulkSearchVolumeLiveItem.to_json()

# convert the object into a dict
keywords_data_clickstream_data_bulk_search_volume_live_item_dict = keywords_data_clickstream_data_bulk_search_volume_live_item_instance.to_dict()
# create an instance of KeywordsDataClickstreamDataBulkSearchVolumeLiveItem from a dict
keywords_data_clickstream_data_bulk_search_volume_live_item_form_dict = keywords_data_clickstream_data_bulk_search_volume_live_item.from_dict(keywords_data_clickstream_data_bulk_search_volume_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


