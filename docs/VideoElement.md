# VideoElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**source** | **str** | source of the element indicates the source of information included in the top_stories_element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**url** | **str** | URL | [optional] 

## Example

```python
from dataforseo_client.models.video_element import VideoElement

# TODO update the JSON string below
json = "{}"
# create an instance of VideoElement from a JSON string
video_element_instance = VideoElement.from_json(json)
# print the JSON string representation of the object
print(VideoElement.to_json())

# convert the object into a dict
video_element_dict = video_element_instance.to_dict()
# create an instance of VideoElement from a dict
video_element_from_dict = VideoElement.from_dict(video_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


