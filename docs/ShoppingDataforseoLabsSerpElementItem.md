# ShoppingDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the item | [optional] 
**items** | [**List[ShoppingElement]**](ShoppingElement.md) | additional items present in the element if there are none, equals null | [optional] 

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


