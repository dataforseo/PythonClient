# RecipesSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[RecipesElement]**](RecipesElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.recipes_serp_element_item import RecipesSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of RecipesSerpElementItem from a JSON string
recipes_serp_element_item_instance = RecipesSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(RecipesSerpElementItem.to_json())

# convert the object into a dict
recipes_serp_element_item_dict = recipes_serp_element_item_instance.to_dict()
# create an instance of RecipesSerpElementItem from a dict
recipes_serp_element_item_from_dict = RecipesSerpElementItem.from_dict(recipes_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


