[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of the row | [optional]
**description** | **str** | description of the results element in SERP | [optional]
**url** | **str** | URL | [optional]
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.app_element import AppElement

# TODO update the JSON string below
json = "{}"
# create an instance of AppElement from a JSON string
app_element_instance = AppElement.from_json(json)
# print the JSON string representation of the object
print AppElement.to_json()

# convert the object into a dict
app_element_dict = app_element_instance.to_dict()
# create an instance of AppElement from a dict
app_element_form_dict = app_element.from_dict(app_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")