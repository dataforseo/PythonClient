[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# PerspectivesElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of the row | [optional]
**description** | **str** | description of the results element in SERP | [optional]
**url** | **str** | URL | [optional]
**domain** | **str** | domain where a link points | [optional]
**var_date** | **str** | the date when the page source of the element was published | [optional]
**source** | **str** | web source of the hotel booking element indicates the source of information included in the element | [optional]
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]

## Example

```python
from dataforseo_client.models.perspectives_element import PerspectivesElement

# TODO update the JSON string below
json = "{}"
# create an instance of PerspectivesElement from a JSON string
perspectives_element_instance = PerspectivesElement.from_json(json)
# print the JSON string representation of the object
print PerspectivesElement.to_json()

# convert the object into a dict
perspectives_element_dict = perspectives_element_instance.to_dict()
# create an instance of PerspectivesElement from a dict
perspectives_element_form_dict = perspectives_element.from_dict(perspectives_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")