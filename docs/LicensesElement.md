[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# LicensesElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of the row | [optional]
**url** | **str** | URL | [optional]
**domain** | **str** | domain where a link points | [optional]

## Example

```python
from dataforseo_client.models.licenses_element import LicensesElement

# TODO update the JSON string below
json = "{}"
# create an instance of LicensesElement from a JSON string
licenses_element_instance = LicensesElement.from_json(json)
# print the JSON string representation of the object
print LicensesElement.to_json()

# convert the object into a dict
licenses_element_dict = licenses_element_instance.to_dict()
# create an instance of LicensesElement from a dict
licenses_element_form_dict = licenses_element.from_dict(licenses_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")