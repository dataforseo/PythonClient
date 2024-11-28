# SerpYoutubeVideoSubtitlesTaskPostRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_id** | **str** | ID of the video required field you can find video ID in the URL or ‘youtube_video’ item of YouTube Organic result example: Y8Wu4rSNJms | [optional] 
**priority** | **int** | task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page. | [optional] 
**subtitles_language** | **str** | language code of original text you can get the language code from YouTube Video Info result | [optional] 
**subtitles_translate_language** | **str** | language code of translated text possible values: \&quot;az\&quot;, \&quot;ay\&quot;, \&quot;ak\&quot;, \&quot;sq\&quot;, \&quot;am\&quot;, \&quot;en\&quot;, \&quot;ar\&quot;, \&quot;hy\&quot;, \&quot;as\&quot;, \&quot;af\&quot;, \&quot;eu\&quot;, \&quot;be\&quot;, \&quot;bn\&quot;, \&quot;my\&quot;, \&quot;bg\&quot;, \&quot;bs\&quot;, \&quot;bho\&quot;, \&quot;cy\&quot;, \&quot;hu\&quot;, \&quot;vi\&quot;, \&quot;haw\&quot;, \&quot;ht\&quot;, \&quot;gl\&quot;, \&quot;lg\&quot;, \&quot;el\&quot;, \&quot;ka\&quot;, \&quot;gn\&quot;, \&quot;gu\&quot;, \&quot;gd\&quot;, \&quot;da\&quot;, \&quot;fy\&quot;, \&quot;zu\&quot;, \&quot;iw\&quot;, \&quot;ig\&quot;, \&quot;yi\&quot;, \&quot;id\&quot;, \&quot;ga\&quot;, \&quot;is\&quot;, \&quot;es\&quot;, \&quot;it\&quot;, \&quot;yo\&quot;, \&quot;kk\&quot;, \&quot;kn\&quot;, \&quot;ca\&quot;, \&quot;qu\&quot;, \&quot;rw\&quot;, \&quot;ky\&quot;, \&quot;zh-Hant\&quot;, \&quot;zh-Hans\&quot;, \&quot;ko\&quot;, \&quot;co\&quot;, \&quot;xh\&quot;, \&quot;ku\&quot;, \&quot;km\&quot;, \&quot;lo\&quot;, \&quot;la\&quot;, \&quot;lv\&quot;, \&quot;ln\&quot;, \&quot;lt\&quot;, \&quot;lb\&quot;, \&quot;mk\&quot;, \&quot;mg\&quot;, \&quot;ms\&quot;, \&quot;ml\&quot;, \&quot;dv\&quot;, \&quot;mt\&quot;, \&quot;mi\&quot;, \&quot;mr\&quot;, \&quot;mn\&quot;, \&quot;und\&quot;, \&quot;de\&quot;, \&quot;ne\&quot;, \&quot;nl\&quot;, \&quot;no\&quot;, \&quot;ny\&quot;, \&quot;or\&quot;, \&quot;om\&quot;, \&quot;pa\&quot;, \&quot;fa\&quot;, \&quot;pl\&quot;, \&quot;pt\&quot;, \&quot;ps\&quot;, \&quot;ro\&quot;, \&quot;ru\&quot;, \&quot;sm\&quot;, \&quot;sa\&quot;, \&quot;ceb\&quot;, \&quot;nso\&quot;, \&quot;sr\&quot;, \&quot;si\&quot;, \&quot;sd\&quot;, \&quot;sk\&quot;, \&quot;sl\&quot;, \&quot;so\&quot;, \&quot;sw\&quot;, \&quot;su\&quot;, \&quot;tg\&quot;, \&quot;th\&quot;, \&quot;ta\&quot;, \&quot;tt\&quot;, \&quot;te\&quot;, \&quot;ti\&quot;, \&quot;ts\&quot;, \&quot;tr\&quot;, \&quot;tk\&quot;, \&quot;uz\&quot;, \&quot;ug\&quot;, \&quot;uk\&quot;, \&quot;ur\&quot;, \&quot;fil\&quot;, \&quot;fi\&quot;, \&quot;fr\&quot;, \&quot;ha\&quot;, \&quot;hi\&quot;, \&quot;hmn\&quot;, \&quot;hr\&quot;, \&quot;cs\&quot;, \&quot;sv\&quot;, \&quot;sn\&quot;, \&quot;ee\&quot;, \&quot;eo\&quot;, \&quot;et\&quot;, \&quot;st\&quot;, \&quot;jv\&quot;, \&quot;ja\&quot;, \&quot;kri\&quot; | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code if you use this field, you don’t need to specify location_code you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/locations example: United States | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name if you use this field, you don’t need to specify location_name you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/locations example: 2840 | [optional] 
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/languages example: English | [optional] 
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/languages example: en | [optional] 
**device** | **str** | device type optional field only value: desktop | [optional] 
**os** | **str** | device operating system optional field choose from the following values: windows, macos default value: windows | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 
**postback_url** | **str** | return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id&#x3D;$id http://your-server.com/postbackscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in postback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 
**postback_data** | **str** | postback_url datatype required field if you specify postback_url corresponds to the datatype that will be sent to your server possible value: advanced | [optional] 
**pingback_url** | **str** | notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id&#x3D;$id http://your-server.com/pingscript?id&#x3D;$id&amp;tag&#x3D;$tag Note: special characters in pingback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center | [optional] 

## Example

```python
from dataforseo_client.models.serp_youtube_video_subtitles_task_post_request_info import SerpYoutubeVideoSubtitlesTaskPostRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpYoutubeVideoSubtitlesTaskPostRequestInfo from a JSON string
serp_youtube_video_subtitles_task_post_request_info_instance = SerpYoutubeVideoSubtitlesTaskPostRequestInfo.from_json(json)
# print the JSON string representation of the object
print(SerpYoutubeVideoSubtitlesTaskPostRequestInfo.to_json())

# convert the object into a dict
serp_youtube_video_subtitles_task_post_request_info_dict = serp_youtube_video_subtitles_task_post_request_info_instance.to_dict()
# create an instance of SerpYoutubeVideoSubtitlesTaskPostRequestInfo from a dict
serp_youtube_video_subtitles_task_post_request_info_from_dict = SerpYoutubeVideoSubtitlesTaskPostRequestInfo.from_dict(serp_youtube_video_subtitles_task_post_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


