# YoutubeVideoInfoSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP for the target domain absolute position among all the elements in SERP | [optional] 
**video_id** | **str** | ID of the video received in a POST array | [optional] 
**title** | **str** | title of the video | [optional] 
**url** | **str** | URL of the video | [optional] 
**thumbnail_url** | **str** | the URL of the page where the thumbnail is hosted | [optional] 
**channel_id** | **str** | the ID of the channel where the video is published | [optional] 
**channel_name** | **str** | the name of the channel where the video is published | [optional] 
**channel_url** | **str** | the URL of the channel where the video is published | [optional] 
**channel_logo** | **str** | the URL of the page where the logo image of the channel is hosted | [optional] 
**description** | **str** | description of the video | [optional] 
**views_count** | **int** | number of views of the video | [optional] 
**likes_count** | **int** | number of likes on the video | [optional] 
**comments_count** | **int** | number of comments on the video | [optional] 
**publication_date** | **str** | the date when the video is published | [optional] 
**timestamp** | **str** | date and time when the result is published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2022-11-15 12:57:46 +00:00 | [optional] 
**keywords** | **List[Optional[str]]** | keywords relevant to the video | [optional] 
**category** | **str** | the category the video belongs to | [optional] 
**is_live** | **bool** | indicates whether the video is on live | [optional] 
**duration_time** | **str** | duration of the video | [optional] 
**duration_time_seconds** | **int** | duration of the video in seconds | [optional] 
**subtitles** | **str** | subtitles in the video | [optional] 
**streaming_quality** | [**List[StreamingQualityElement]**](StreamingQualityElement.md) | array of elements that contain information about all possible streaming qualities of the video | [optional] 

## Example

```python
from dataforseo_client.models.youtube_video_info_serp_element_item import YoutubeVideoInfoSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of YoutubeVideoInfoSerpElementItem from a JSON string
youtube_video_info_serp_element_item_instance = YoutubeVideoInfoSerpElementItem.from_json(json)
# print the JSON string representation of the object
print YoutubeVideoInfoSerpElementItem.to_json()

# convert the object into a dict
youtube_video_info_serp_element_item_dict = youtube_video_info_serp_element_item_instance.to_dict()
# create an instance of YoutubeVideoInfoSerpElementItem from a dict
youtube_video_info_serp_element_item_form_dict = youtube_video_info_serp_element_item.from_dict(youtube_video_info_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


