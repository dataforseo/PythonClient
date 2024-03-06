[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ProductConsiderationsElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of the row | [optional]
**consideration_category** | **str** | category of the consideration element the category is indicated just above the title fo the consideration element | [optional]
**expanded_element** | [**ProductConsiderationsExpandedElement**](ProductConsiderationsExpandedElement.md) |  | [optional]

## Example

```python
from dataforseo_client.models.product_considerations_element import ProductConsiderationsElement

# TODO update the JSON string below
json = "{}"
# create an instance of ProductConsiderationsElement from a JSON string
product_considerations_element_instance = ProductConsiderationsElement.from_json(json)
# print the JSON string representation of the object
print ProductConsiderationsElement.to_json()

# convert the object into a dict
product_considerations_element_dict = product_considerations_element_instance.to_dict()
# create an instance of ProductConsiderationsElement from a dict
product_considerations_element_form_dict = product_considerations_element.from_dict(product_considerations_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")