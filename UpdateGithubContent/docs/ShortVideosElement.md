# ShortVideosElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**domain** | **str** | website domain | [optional] 
**url** | **str** | URL | [optional] 
**source** | **str** | source of the element indicates the source of information included in the top_stories_element | [optional] 

## Example

```python
from dataforseo_client.models.short_videos_element import ShortVideosElement

# TODO update the JSON string below
json = "{}"
# create an instance of ShortVideosElement from a JSON string
short_videos_element_instance = ShortVideosElement.from_json(json)
# print the JSON string representation of the object
print ShortVideosElement.to_json()

# convert the object into a dict
short_videos_element_dict = short_videos_element_instance.to_dict()
# create an instance of ShortVideosElement from a dict
short_videos_element_form_dict = short_videos_element.from_dict(short_videos_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


