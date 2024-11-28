# RefineProductsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the row | [optional] 
**items** | [**List[RefineProductsElement]**](RefineProductsElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.refine_products_serp_element_item import RefineProductsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of RefineProductsSerpElementItem from a JSON string
refine_products_serp_element_item_instance = RefineProductsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(RefineProductsSerpElementItem.to_json())

# convert the object into a dict
refine_products_serp_element_item_dict = refine_products_serp_element_item_instance.to_dict()
# create an instance of RefineProductsSerpElementItem from a dict
refine_products_serp_element_item_from_dict = RefineProductsSerpElementItem.from_dict(refine_products_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


