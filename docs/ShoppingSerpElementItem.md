# ShoppingSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the row | [optional] 
**items** | [**List[ShoppingElement]**](ShoppingElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.shopping_serp_element_item import ShoppingSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ShoppingSerpElementItem from a JSON string
shopping_serp_element_item_instance = ShoppingSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(ShoppingSerpElementItem.to_json())

# convert the object into a dict
shopping_serp_element_item_dict = shopping_serp_element_item_instance.to_dict()
# create an instance of ShoppingSerpElementItem from a dict
shopping_serp_element_item_from_dict = ShoppingSerpElementItem.from_dict(shopping_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


