# YoutubeVideoInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>            position within a group of elements with identical <code>type</code> values<br>            positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em> absolute rank in SERP for the target domain</em><br>            absolute position among all the elements in SERP |[optional]|
**video_id** | **StrictStr** | <em>ID of the video received in a POST array</em> |[optional]|
**title** | **StrictStr** | <em>title of the video</em> |[optional]|
**url** | **StrictStr** | <em>URL of the video</em> |[optional]|
**thumbnail_url** | **StrictStr** | <em>the URL of the page where the thumbnail is hosted</em> |[optional]|
**channel_id** | **StrictStr** | <em>the ID of the channel where the video is published</em> |[optional]|
**channel_name** | **StrictStr** | <em>the name of the channel where the video is published</em> |[optional]|
**channel_url** | **StrictStr** | <em>the URL of the channel where the video is published</em> |[optional]|
**channel_logo** | **StrictStr** | <em>the URL of the page where the logo image of the channel is hosted</em> |[optional]|
**description** | **StrictStr** | <em>description of the video</em> |[optional]|
**views_count** | **StrictInt** | <em>number of views of the video</em> |[optional]|
**likes_count** | **StrictInt** | <em>number of likes on the video</em> |[optional]|
**comments_count** | **StrictInt** | <em>number of comments on the video</em> |[optional]|
**channel_subscribers_count** | **ChannelSubscribersCount** | <em>number of subscribers of the channel</em> |[optional]|
**publication_date** | **StrictStr** | <em>the date when the video is published</em> |[optional]|
**timestamp** | **StrictStr** | <em>date and time when the result is published</em><br>            in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>            example:<br>            <code>2022-11-15 12:57:46 +00:00</code> |[optional]|
**keywords** | **List[Optional[StrictStr]]** | <em>keywords relevant to the video</em><br>            also known as 'YouTube tags' |[optional]|
**category** | **StrictStr** | <em>the category the video belongs to</em> |[optional]|
**is_live** | **StrictBool** | <em>indicates whether the video is on live</em> |[optional]|
**is_embeddable** | **StrictBool** | <em>indicates whether the video is embeddable</em> |[optional]|
**duration_time** | **StrictStr** | <em>duration of the video</em> |[optional]|
**duration_time_seconds** | **StrictInt** | <em>duration of the video in seconds</em> |[optional]|
**subtitles** | **List[Optional[Subtitles]]** | <em>array of elements describing properties of subtitles in the video</em> |[optional]|
**streaming_quality** | **List[Optional[StreamingQualityElement]]** | <em>array of elements that contain information about all possible streaming qualities of the video</em> |[optional]|