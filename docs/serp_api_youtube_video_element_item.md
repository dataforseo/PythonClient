# SerpApiYoutubeVideoElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | <em>title of the video</em> |[optional]|
**video_id** | **StrictStr** | <em>ID of the video</em> |[optional]|
**thumbnail_url** | **StrictStr** | <em>the URL of the page where the thumbnail is hosted</em> |[optional]|
**channel_name** | **StrictStr** | <em>the name of the channel where the video is published</em> |[optional]|
**channel_url** | **StrictStr** | <em>the URL of the channel where the video is published</em> |[optional]|
**channel_logo** | **StrictStr** | <em>the URL of the page where the logo image of the channel is hosted</em> |[optional]|
**description** | **StrictStr** | <em>description of the channel</em> |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | <em>highlighted keywords in the description</em> |[optional]|
**badges** | **List[Optional[StrictStr]]** | <em>video badges</em><br>            example:<br>            <code>New</code>, <code>CC</code>, <code>4K</code><br> |[optional]|
**is_live** | **StrictBool** | <em>indicates whether the video is a live broadcast</em> |[optional]|
**is_shorts** | **StrictBool** | <em>indicates whether the video is shorts</em> |[optional]|
**is_movie** | **StrictBool** | <em>indicates whether the video is a movie</em> |[optional]|
**views_count** | **StrictInt** | <em>number of views of the video</em> |[optional]|
**publication_date** | **StrictStr** | <em>the date when the video is published</em> |[optional]|
**timestamp** | **StrictStr** | <em>date and time when the result is published</em><br>            in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>            example:<br>            <code>2022-11-15 12:57:46 +00:00</code><br> |[optional]|
**duration_time** | **StrictStr** | <em>duration of the video</em> |[optional]|
**duration_time_seconds** | **StrictInt** | <em>duration of the video in seconds</em> |[optional]|