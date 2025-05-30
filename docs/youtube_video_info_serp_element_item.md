# YoutubeVideoInfoSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**video_id** | **StrictStr** | ID of the video received in a POST array |[optional]|
**title** | **StrictStr** | title of the video |[optional]|
**url** | **StrictStr** | URL of the video |[optional]|
**thumbnail_url** | **StrictStr** | the URL of the page where the thumbnail is hosted |[optional]|
**channel_id** | **StrictStr** | the ID of the channel where the video is published |[optional]|
**channel_name** | **StrictStr** | the name of the channel where the video is published |[optional]|
**channel_url** | **StrictStr** | the URL of the channel where the video is published |[optional]|
**channel_logo** | **StrictStr** | the URL of the page where the logo image of the channel is hosted |[optional]|
**description** | **StrictStr** | description of the video |[optional]|
**views_count** | **StrictFloat** | number of views of the video |[optional]|
**likes_count** | **StrictFloat** | number of likes on the video |[optional]|
**comments_count** | **StrictFloat** | number of comments on the video |[optional]|
**channel_subscribers_count** | **ChannelSubscribersCount** | number of subscribers of the channel |[optional]|
**publication_date** | **StrictStr** | the date when the video is published |[optional]|
**timestamp** | **StrictStr** | date and time when the result is published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2022-11-15 12:57:46 +00:00 |[optional]|
**keywords** | **List[Optional[StrictStr]]** | keywords relevant to the video |[optional]|
**category** | **StrictStr** | the category the video belongs to |[optional]|
**is_live** | **StrictBool** | indicates whether the video is on live |[optional]|
**is_embeddable** | **StrictBool** | indicates whether the video is embeddable |[optional]|
**duration_time** | **StrictStr** | duration of the video |[optional]|
**duration_time_seconds** | **StrictFloat** | duration of the video in seconds |[optional]|
**subtitles** | **List[Optional[Subtitles]]** | array of elements describing properties of subtitles in the video |[optional]|
**streaming_quality** | **List[Optional[StreamingQualityElement]]** | array of elements that contain information about all possible streaming qualities of the video |[optional]|