# RecipesSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[RecipesElement]**](RecipesElement.md) | additional items present in the element if there are none, equals null | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.recipes_serp_element_item import RecipesSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of RecipesSerpElementItem from a JSON string
recipes_serp_element_item_instance = RecipesSerpElementItem.from_json(json)
# print the JSON string representation of the object
print RecipesSerpElementItem.to_json()

# convert the object into a dict
recipes_serp_element_item_dict = recipes_serp_element_item_instance.to_dict()
# create an instance of RecipesSerpElementItem from a dict
recipes_serp_element_item_form_dict = recipes_serp_element_item.from_dict(recipes_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


