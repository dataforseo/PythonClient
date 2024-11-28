# DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**asins** | **Dict[str, Optional[str]]** | ASINs in a POST array | [optional] 
**location_code** | **int** | location code in a POST array if there is no data, then the value is null | [optional] 
**language_code** | **str** | language code in a POST array if there is no data, then the value is null | [optional] 
**total_count** | **int** | total amount of results in our database relevant to your request | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[DataforseoLabsAmazonProductKeywordIntersectionsLiveItem]**](DataforseoLabsAmazonProductKeywordIntersectionsLiveItem.md) | contains detected Amazon product competitors and related data | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_amazon_product_keyword_intersections_live_result_info import DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo from a JSON string
dataforseo_labs_amazon_product_keyword_intersections_live_result_info_instance = DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo.to_json())

# convert the object into a dict
dataforseo_labs_amazon_product_keyword_intersections_live_result_info_dict = dataforseo_labs_amazon_product_keyword_intersections_live_result_info_instance.to_dict()
# create an instance of DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo from a dict
dataforseo_labs_amazon_product_keyword_intersections_live_result_info_from_dict = DataforseoLabsAmazonProductKeywordIntersectionsLiveResultInfo.from_dict(dataforseo_labs_amazon_product_keyword_intersections_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


