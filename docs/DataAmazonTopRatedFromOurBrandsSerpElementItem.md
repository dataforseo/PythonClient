# DataAmazonTopRatedFromOurBrandsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in Amazon SERP possible values: left, right | [optional] 
**items** | [**List[AmazonSerpElement]**](AmazonSerpElement.md) | Amazon product items | [optional] 

## Example

```python
from dataforseo_client.models.data_amazon_top_rated_from_our_brands_serp_element_item import DataAmazonTopRatedFromOurBrandsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataAmazonTopRatedFromOurBrandsSerpElementItem from a JSON string
data_amazon_top_rated_from_our_brands_serp_element_item_instance = DataAmazonTopRatedFromOurBrandsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print DataAmazonTopRatedFromOurBrandsSerpElementItem.to_json()

# convert the object into a dict
data_amazon_top_rated_from_our_brands_serp_element_item_dict = data_amazon_top_rated_from_our_brands_serp_element_item_instance.to_dict()
# create an instance of DataAmazonTopRatedFromOurBrandsSerpElementItem from a dict
data_amazon_top_rated_from_our_brands_serp_element_item_form_dict = data_amazon_top_rated_from_our_brands_serp_element_item.from_dict(data_amazon_top_rated_from_our_brands_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


