[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# TopStoriesElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**source** | **str** | web source of the hotel booking element indicates the source of information included in the element | [optional]
**domain** | **str** | domain where a link points | [optional]
**title** | **str** | title of the row | [optional]
**var_date** | **str** | the date when the page source of the element was published | [optional]
**amp_version** | **bool** | Accelerated Mobile Pages indicates whether an item has the Accelerated Mobile Page (AMP) version | [optional]
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**url** | **str** | URL | [optional]

## Example

```python
from dataforseo_client.models.top_stories_element import TopStoriesElement

# TODO update the JSON string below
json = "{}"
# create an instance of TopStoriesElement from a JSON string
top_stories_element_instance = TopStoriesElement.from_json(json)
# print the JSON string representation of the object
print TopStoriesElement.to_json()

# convert the object into a dict
top_stories_element_dict = top_stories_element_instance.to_dict()
# create an instance of TopStoriesElement from a dict
top_stories_element_form_dict = top_stories_element.from_dict(top_stories_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")