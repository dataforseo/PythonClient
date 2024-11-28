# DataforseoLabsAmazonProductRankOverviewLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**asin** | **str** | ASIN of the product unique product identifier on Amazon; for more information, refer to this help center guide | [optional] 
**metrics** | [**AmazonMetricsBundleInfo**](AmazonMetricsBundleInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_amazon_product_rank_overview_live_item import DataforseoLabsAmazonProductRankOverviewLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsAmazonProductRankOverviewLiveItem from a JSON string
dataforseo_labs_amazon_product_rank_overview_live_item_instance = DataforseoLabsAmazonProductRankOverviewLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsAmazonProductRankOverviewLiveItem.to_json())

# convert the object into a dict
dataforseo_labs_amazon_product_rank_overview_live_item_dict = dataforseo_labs_amazon_product_rank_overview_live_item_instance.to_dict()
# create an instance of DataforseoLabsAmazonProductRankOverviewLiveItem from a dict
dataforseo_labs_amazon_product_rank_overview_live_item_from_dict = DataforseoLabsAmazonProductRankOverviewLiveItem.from_dict(dataforseo_labs_amazon_product_rank_overview_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


