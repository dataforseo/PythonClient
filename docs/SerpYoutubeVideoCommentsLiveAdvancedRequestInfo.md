[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# SerpYoutubeVideoCommentsLiveAdvancedRequestInfo

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
**depth** | **int** | parsing depth optional field number of results in SERP default value: 20 max value: 700 Note: your account will be billed per each SERP containing up to 20 results; thus, setting a depth above 20 may result in additional charges if the search engine returns more than 20 results; if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance | [optional]
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional]

## Example

```python
from dataforseo_client.models.serp_youtube_video_comments_live_advanced_request_info import SerpYoutubeVideoCommentsLiveAdvancedRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpYoutubeVideoCommentsLiveAdvancedRequestInfo from a JSON string
serp_youtube_video_comments_live_advanced_request_info_instance = SerpYoutubeVideoCommentsLiveAdvancedRequestInfo.from_json(json)
# print the JSON string representation of the object
print SerpYoutubeVideoCommentsLiveAdvancedRequestInfo.to_json()

# convert the object into a dict
serp_youtube_video_comments_live_advanced_request_info_dict = serp_youtube_video_comments_live_advanced_request_info_instance.to_dict()
# create an instance of SerpYoutubeVideoCommentsLiveAdvancedRequestInfo from a dict
serp_youtube_video_comments_live_advanced_request_info_form_dict = serp_youtube_video_comments_live_advanced_request_info.from_dict(serp_youtube_video_comments_live_advanced_request_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")