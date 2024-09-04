# ShoppingDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**items** | [**List[ShoppingElement]**](ShoppingElement.md) | elements of search results found in SERP | [optional] 

## Example

```python
from dataforseo_client.models.shopping_dataforseo_labs_serp_element_item import ShoppingDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ShoppingDataforseoLabsSerpElementItem from a JSON string
shopping_dataforseo_labs_serp_element_item_instance = ShoppingDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print ShoppingDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
shopping_dataforseo_labs_serp_element_item_dict = shopping_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of ShoppingDataforseoLabsSerpElementItem from a dict
shopping_dataforseo_labs_serp_element_item_form_dict = shopping_dataforseo_labs_serp_element_item.from_dict(shopping_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


