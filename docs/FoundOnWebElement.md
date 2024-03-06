[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# FoundOnWebElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of the row | [optional]
**subtitle** | **str** | subtitle of the element | [optional]
**image** | [**ImagesElement**](ImagesElement.md) |  | [optional]

## Example

```python
from dataforseo_client.models.found_on_web_element import FoundOnWebElement

# TODO update the JSON string below
json = "{}"
# create an instance of FoundOnWebElement from a JSON string
found_on_web_element_instance = FoundOnWebElement.from_json(json)
# print the JSON string representation of the object
print FoundOnWebElement.to_json()

# convert the object into a dict
found_on_web_element_dict = found_on_web_element_instance.to_dict()
# create an instance of FoundOnWebElement from a dict
found_on_web_element_form_dict = found_on_web_element.from_dict(found_on_web_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")