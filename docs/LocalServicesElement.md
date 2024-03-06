[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# LocalServicesElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of the row | [optional]
**url** | **str** | URL | [optional]
**domain** | **str** | domain where a link points | [optional]
**description** | **str** | description of the results element in SERP | [optional]
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional]
**profile_image_url** | **str** | URL of the image featured in the element | [optional]

## Example

```python
from dataforseo_client.models.local_services_element import LocalServicesElement

# TODO update the JSON string below
json = "{}"
# create an instance of LocalServicesElement from a JSON string
local_services_element_instance = LocalServicesElement.from_json(json)
# print the JSON string representation of the object
print LocalServicesElement.to_json()

# convert the object into a dict
local_services_element_dict = local_services_element_instance.to_dict()
# create an instance of LocalServicesElement from a dict
local_services_element_form_dict = local_services_element.from_dict(local_services_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")