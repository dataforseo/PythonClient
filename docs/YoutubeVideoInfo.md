# YoutubeVideoInfo

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**rank_group** | **number** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank in SERP for the target domain<br>absolute position among all the elements in SERP |[optional]|
**video_id** | **string** | ID of the video received in a POST array |[optional]|
**title** | **string** | title of the video |[optional]|
**url** | **string** | URL of the video |[optional]|
**thumbnail_url** | **string** | the URL of the page where the thumbnail is hosted |[optional]|
**channel_id** | **string** | the ID of the channel where the video is published |[optional]|
**channel_name** | **string** | the name of the channel where the video is published |[optional]|
**channel_url** | **string** | the URL of the channel where the video is published |[optional]|
**channel_logo** | **string** | the URL of the page where the logo image of the channel is hosted |[optional]|
**description** | **string** | description of the video |[optional]|
**views_count** | **number** | number of views of the video |[optional]|
**likes_count** | **number** | number of likes on the video |[optional]|
**comments_count** | **number** | number of comments on the video |[optional]|
**channel_subscribers_count** | **ChannelSubscribersCount** | number of subscribers of the channel |[optional]|
**publication_date** | **string** | the date when the video is published |[optional]|
**timestamp** | **string** | date and time when the result is published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2022-11-15 12:57:46 +00:00 |[optional]|
**keywords** | **string[]** | keywords relevant to the video |[optional]|
**category** | **string** | the category the video belongs to |[optional]|
**is_live** | **boolean** | indicates whether the video is on live |[optional]|
**is_embeddable** | **boolean** | indicates whether the video is embeddable |[optional]|
**duration_time** | **string** | duration of the video |[optional]|
**duration_time_seconds** | **number** | duration of the video in seconds |[optional]|
**subtitles** | **Subtitles[]** | array of elements describing properties of subtitles in the video |[optional]|
**streaming_quality** | **StreamingQualityElement[]** | array of elements that contain information about all possible streaming qualities of the video |[optional]|