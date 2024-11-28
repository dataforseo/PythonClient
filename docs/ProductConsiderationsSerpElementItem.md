# ProductConsiderationsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the row | [optional] 
**items** | [**List[ProductConsiderationsElement]**](ProductConsiderationsElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.product_considerations_serp_element_item import ProductConsiderationsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProductConsiderationsSerpElementItem from a JSON string
product_considerations_serp_element_item_instance = ProductConsiderationsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(ProductConsiderationsSerpElementItem.to_json())

# convert the object into a dict
product_considerations_serp_element_item_dict = product_considerations_serp_element_item_instance.to_dict()
# create an instance of ProductConsiderationsSerpElementItem from a dict
product_considerations_serp_element_item_from_dict = ProductConsiderationsSerpElementItem.from_dict(product_considerations_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


