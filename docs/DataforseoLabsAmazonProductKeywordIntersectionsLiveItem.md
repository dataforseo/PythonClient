# DataforseoLabsAmazonProductKeywordIntersectionsLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**keyword_data** | [**AmazonKeywordData**](AmazonKeywordData.md) |  | [optional] 
**intersection_result** | [**Dict[str, BaseAmazonSerpElementItem]**](BaseAmazonSerpElementItem.md) | data on the intersection | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_amazon_product_keyword_intersections_live_item import DataforseoLabsAmazonProductKeywordIntersectionsLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsAmazonProductKeywordIntersectionsLiveItem from a JSON string
dataforseo_labs_amazon_product_keyword_intersections_live_item_instance = DataforseoLabsAmazonProductKeywordIntersectionsLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsAmazonProductKeywordIntersectionsLiveItem.to_json())

# convert the object into a dict
dataforseo_labs_amazon_product_keyword_intersections_live_item_dict = dataforseo_labs_amazon_product_keyword_intersections_live_item_instance.to_dict()
# create an instance of DataforseoLabsAmazonProductKeywordIntersectionsLiveItem from a dict
dataforseo_labs_amazon_product_keyword_intersections_live_item_form_dict = dataforseo_labs_amazon_product_keyword_intersections_live_item.from_dict(dataforseo_labs_amazon_product_keyword_intersections_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


