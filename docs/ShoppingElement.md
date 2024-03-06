[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ShoppingElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of the row | [optional]
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional]
**source** | **str** | web source of the hotel booking element indicates the source of information included in the element | [optional]
**description** | **str** | description of the results element in SERP | [optional]
**marketplace** | **str** | merchant account provider commerce site that hosts products or websites of individual sellers under the same merchant account example: by Google | [optional]
**marketplace_url** | **str** | relevant marketplace URL URL of the page on the marketplace website where the product is hosted | [optional]
**url** | **str** | URL | [optional]

## Example

```python
from dataforseo_client.models.shopping_element import ShoppingElement

# TODO update the JSON string below
json = "{}"
# create an instance of ShoppingElement from a JSON string
shopping_element_instance = ShoppingElement.from_json(json)
# print the JSON string representation of the object
print ShoppingElement.to_json()

# convert the object into a dict
shopping_element_dict = shopping_element_instance.to_dict()
# create an instance of ShoppingElement from a dict
shopping_element_form_dict = shopping_element.from_dict(shopping_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")