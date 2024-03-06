[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# VideoElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**source** | **str** | web source of the hotel booking element indicates the source of information included in the element | [optional]
**title** | **str** | title of the row | [optional]
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**url** | **str** | URL | [optional]
**preview** | **str** | URL to the video preview image | [optional]

## Example

```python
from dataforseo_client.models.video_element import VideoElement

# TODO update the JSON string below
json = "{}"
# create an instance of VideoElement from a JSON string
video_element_instance = VideoElement.from_json(json)
# print the JSON string representation of the object
print VideoElement.to_json()

# convert the object into a dict
video_element_dict = video_element_instance.to_dict()
# create an instance of VideoElement from a dict
video_element_form_dict = video_element.from_dict(video_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")