# YoutubeSubtitlesSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP for the target domain absolute position among all the elements in SERP | [optional] 
**text** | **str** | text translated in subtitles | [optional] 
**start_time** | **int** | the second subtitled text starts | [optional] 
**end_time** | **int** | the second subtitled text ends | [optional] 
**duration_time** | **int** | duration of subtitles in seconds | [optional] 

## Example

```python
from dataforseo_client.models.youtube_subtitles_serp_element_item import YoutubeSubtitlesSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of YoutubeSubtitlesSerpElementItem from a JSON string
youtube_subtitles_serp_element_item_instance = YoutubeSubtitlesSerpElementItem.from_json(json)
# print the JSON string representation of the object
print YoutubeSubtitlesSerpElementItem.to_json()

# convert the object into a dict
youtube_subtitles_serp_element_item_dict = youtube_subtitles_serp_element_item_instance.to_dict()
# create an instance of YoutubeSubtitlesSerpElementItem from a dict
youtube_subtitles_serp_element_item_form_dict = youtube_subtitles_serp_element_item.from_dict(youtube_subtitles_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


