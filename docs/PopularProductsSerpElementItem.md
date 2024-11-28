# PopularProductsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the row | [optional] 
**items** | [**List[PopularProductsElement]**](PopularProductsElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.popular_products_serp_element_item import PopularProductsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of PopularProductsSerpElementItem from a JSON string
popular_products_serp_element_item_instance = PopularProductsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(PopularProductsSerpElementItem.to_json())

# convert the object into a dict
popular_products_serp_element_item_dict = popular_products_serp_element_item_instance.to_dict()
# create an instance of PopularProductsSerpElementItem from a dict
popular_products_serp_element_item_from_dict = PopularProductsSerpElementItem.from_dict(popular_products_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


