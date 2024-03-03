# PopularProductsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**items** | [**List[PopularProductsElement]**](PopularProductsElement.md) | contains results featured in the ‘hotels_pack’ element of SERP | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.popular_products_serp_element_item import PopularProductsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of PopularProductsSerpElementItem from a JSON string
popular_products_serp_element_item_instance = PopularProductsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print PopularProductsSerpElementItem.to_json()

# convert the object into a dict
popular_products_serp_element_item_dict = popular_products_serp_element_item_instance.to_dict()
# create an instance of PopularProductsSerpElementItem from a dict
popular_products_serp_element_item_form_dict = popular_products_serp_element_item.from_dict(popular_products_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


