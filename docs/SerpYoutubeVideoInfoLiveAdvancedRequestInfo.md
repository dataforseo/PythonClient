# SerpYoutubeVideoInfoLiveAdvancedRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_id** | **str** | ID of the video required field you can find video ID in the URL or ‘youtube_video’ item of YouTube Organic result example: vQXvyV0zIP4 | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code if you use this field, you don’t need to specify location_code you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/locations example: United States | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name  if you use this field, you don’t need to specify location_name you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/locations example: 2840 | [optional] 
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/languages example: English | [optional] 
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/languages example: en | [optional] 
**device** | **str** | device type optional field only value: desktop | [optional] 
**os** | **str** | device operating system optional field choose from the following values: windows, macos default value: windows | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.serp_youtube_video_info_live_advanced_request_info import SerpYoutubeVideoInfoLiveAdvancedRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpYoutubeVideoInfoLiveAdvancedRequestInfo from a JSON string
serp_youtube_video_info_live_advanced_request_info_instance = SerpYoutubeVideoInfoLiveAdvancedRequestInfo.from_json(json)
# print the JSON string representation of the object
print SerpYoutubeVideoInfoLiveAdvancedRequestInfo.to_json()

# convert the object into a dict
serp_youtube_video_info_live_advanced_request_info_dict = serp_youtube_video_info_live_advanced_request_info_instance.to_dict()
# create an instance of SerpYoutubeVideoInfoLiveAdvancedRequestInfo from a dict
serp_youtube_video_info_live_advanced_request_info_form_dict = serp_youtube_video_info_live_advanced_request_info.from_dict(serp_youtube_video_info_live_advanced_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


