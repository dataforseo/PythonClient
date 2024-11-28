# VideoDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**items** | [**List[VideoElement]**](VideoElement.md) | elements of search results found in SERP | [optional] 

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
video_dataforseo_labs_serp_element_item_from_dict = VideoDataforseoLabsSerpElementItem.from_dict(video_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


