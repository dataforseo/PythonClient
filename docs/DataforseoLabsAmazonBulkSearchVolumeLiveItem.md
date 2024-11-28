# DataforseoLabsAmazonBulkSearchVolumeLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**keyword** | **str** | keyword in a POST array | [optional] 
**search_volume** | **int** | average monthly search volume rate represents the (approximate) number of searches for the returned keyword on Amazon | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_amazon_bulk_search_volume_live_item import DataforseoLabsAmazonBulkSearchVolumeLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsAmazonBulkSearchVolumeLiveItem from a JSON string
dataforseo_labs_amazon_bulk_search_volume_live_item_instance = DataforseoLabsAmazonBulkSearchVolumeLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsAmazonBulkSearchVolumeLiveItem.to_json())

# convert the object into a dict
dataforseo_labs_amazon_bulk_search_volume_live_item_dict = dataforseo_labs_amazon_bulk_search_volume_live_item_instance.to_dict()
# create an instance of DataforseoLabsAmazonBulkSearchVolumeLiveItem from a dict
dataforseo_labs_amazon_bulk_search_volume_live_item_from_dict = DataforseoLabsAmazonBulkSearchVolumeLiveItem.from_dict(dataforseo_labs_amazon_bulk_search_volume_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


