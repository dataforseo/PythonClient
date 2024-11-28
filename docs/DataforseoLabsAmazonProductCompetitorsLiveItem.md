# DataforseoLabsAmazonProductCompetitorsLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**asin** | **str** | ASIN of the product unique product identifier on Amazon; for more information, refer to this help center guide | [optional] 
**avg_position** | **float** | average position of the product in Amazon SERP Note: average position is calculated for intersected keywords only; the value for a given product may differ when combined with different target products | [optional] 
**sum_position** | **int** | sum of all product positions in Amazon SERP Note: average position is calculated for intersected keywords only; the value for a given product may differ when combined with different target products | [optional] 
**intersections** | **int** | number of intersecting keywords | [optional] 
**competitor_metrics** | [**AmazonMetricsBundleInfo**](AmazonMetricsBundleInfo.md) |  | [optional] 
**full_metrics** | [**AmazonMetricsBundleInfo**](AmazonMetricsBundleInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_amazon_product_competitors_live_item import DataforseoLabsAmazonProductCompetitorsLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsAmazonProductCompetitorsLiveItem from a JSON string
dataforseo_labs_amazon_product_competitors_live_item_instance = DataforseoLabsAmazonProductCompetitorsLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsAmazonProductCompetitorsLiveItem.to_json())

# convert the object into a dict
dataforseo_labs_amazon_product_competitors_live_item_dict = dataforseo_labs_amazon_product_competitors_live_item_instance.to_dict()
# create an instance of DataforseoLabsAmazonProductCompetitorsLiveItem from a dict
dataforseo_labs_amazon_product_competitors_live_item_from_dict = DataforseoLabsAmazonProductCompetitorsLiveItem.from_dict(dataforseo_labs_amazon_product_competitors_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


