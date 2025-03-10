# VideoSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**items** | [**List[VideoElement]**](VideoElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.video_serp_element_item import VideoSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of VideoSerpElementItem from a JSON string
video_serp_element_item_instance = VideoSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(VideoSerpElementItem.to_json())

# convert the object into a dict
video_serp_element_item_dict = video_serp_element_item_instance.to_dict()
# create an instance of VideoSerpElementItem from a dict
video_serp_element_item_from_dict = VideoSerpElementItem.from_dict(video_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


