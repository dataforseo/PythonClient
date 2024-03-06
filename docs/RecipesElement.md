[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# RecipesElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of the row | [optional]
**url** | **str** | URL | [optional]
**domain** | **str** | domain where a link points | [optional]
**source** | **str** | web source of the hotel booking element indicates the source of information included in the element | [optional]
**description** | **str** | description of the results element in SERP | [optional]
**time** | **str** | the total time it takes to prepare the cook the dish | [optional]
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.recipes_element import RecipesElement

# TODO update the JSON string below
json = "{}"
# create an instance of RecipesElement from a JSON string
recipes_element_instance = RecipesElement.from_json(json)
# print the JSON string representation of the object
print RecipesElement.to_json()

# convert the object into a dict
recipes_element_dict = recipes_element_instance.to_dict()
# create an instance of RecipesElement from a dict
recipes_element_form_dict = recipes_element.from_dict(recipes_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")