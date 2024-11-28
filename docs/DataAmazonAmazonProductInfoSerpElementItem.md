# DataAmazonAmazonProductInfoSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in Amazon SERP possible values: left, right | [optional] 
**title** | **str** | product title | [optional] 
**details** | **str** | product specs and other details | [optional] 
**image_url** | **str** | the URL of the product image | [optional] 
**author** | **str** | product brand name | [optional] 
**data_asin** | **str** | ASIN of the product received in a POST array | [optional] 
**parent_asin** | **str** | parent ASIN of the product | [optional] 
**product_asins** | **List[Optional[str]]** | ASINs of all found product modifications | [optional] 
**price_from** | **float** | the lower limit of the product price range example: 49.98 | [optional] 
**price_to** | **float** | the upper limit of the product price range example: 384.99 | [optional] 
**currency** | **str** | currency in the ISO format example: USD | [optional] 
**is_amazon_choice** | **bool** | “Amazon’s choice” label if the value is true, the product is marked with the “Amazon’s choice” label | [optional] 
**rating** | [**RatingElement**](RatingElement.md) |  | [optional] 
**is_newer_model_available** | **bool** | indicates whether the newer model of the product is available | [optional] 
**newer_model** | [**AmazonProductNewerModelInfo**](AmazonProductNewerModelInfo.md) |  | [optional] 
**categories** | [**List[ProductCategoryInfo]**](ProductCategoryInfo.md) | contains related product categories | [optional] 
**product_information** | [**List[BaseProductInformationItem]**](BaseProductInformationItem.md) | contains related product information | [optional] 
**product_images_list** | **List[Optional[str]]** | contains URLs for all images of the product displayed on the left side of the main image | [optional] 
**product_videos_list** | **List[Optional[str]]** | contains URLs for all videos of the product displayed on the right side of the main video | [optional] 
**description** | **str** | contains description of the product | [optional] 
**is_available** | **bool** | indicates whether the product is available for ordering if the value is true, the product can be ordered | [optional] 
**top_local_reviews** | [**List[BaseAmazonSerpElementItem]**](BaseAmazonSerpElementItem.md) | array of objects with top reviews from target location to obtain additional local reviews, you can specify the load_more_local_reviews parameter in Task POST | [optional] 
**top_global_reviews** | [**List[BaseAmazonSerpElementItem]**](BaseAmazonSerpElementItem.md) | array of objects with top reviews from around the world | [optional] 

## Example

```python
from dataforseo_client.models.data_amazon_amazon_product_info_serp_element_item import DataAmazonAmazonProductInfoSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataAmazonAmazonProductInfoSerpElementItem from a JSON string
data_amazon_amazon_product_info_serp_element_item_instance = DataAmazonAmazonProductInfoSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(DataAmazonAmazonProductInfoSerpElementItem.to_json())

# convert the object into a dict
data_amazon_amazon_product_info_serp_element_item_dict = data_amazon_amazon_product_info_serp_element_item_instance.to_dict()
# create an instance of DataAmazonAmazonProductInfoSerpElementItem from a dict
data_amazon_amazon_product_info_serp_element_item_from_dict = DataAmazonAmazonProductInfoSerpElementItem.from_dict(data_amazon_amazon_product_info_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


