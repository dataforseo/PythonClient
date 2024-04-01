# VideoDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**items** | [**List[VideoElement]**](VideoElement.md) | additional items present in the element if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.video_dataforseo_labs_serp_element_item import VideoDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of VideoDataforseoLabsSerpElementItem from a JSON string
video_dataforseo_labs_serp_element_item_instance = VideoDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(VideoDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
video_dataforseo_labs_serp_element_item_dict = video_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of VideoDataforseoLabsSerpElementItem from a dict
video_dataforseo_labs_serp_element_item_form_dict = video_dataforseo_labs_serp_element_item.from_dict(video_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


