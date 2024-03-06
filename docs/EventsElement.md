[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# EventsElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of the row | [optional]
**snippet** | **str** | text alongside the link title | [optional]
**url** | **str** | URL | [optional]

## Example

```python
from dataforseo_client.models.events_element import EventsElement

# TODO update the JSON string below
json = "{}"
# create an instance of EventsElement from a JSON string
events_element_instance = EventsElement.from_json(json)
# print the JSON string representation of the object
print EventsElement.to_json()

# convert the object into a dict
events_element_dict = events_element_instance.to_dict()
# create an instance of EventsElement from a dict
events_element_form_dict = events_element.from_dict(events_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")