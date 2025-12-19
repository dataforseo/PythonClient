# SerpYoutubeVideoInfoLiveAdvancedRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**video_id** | **StrictStr** | ID of the video<br>required field<br>you can find video ID in the URL or 'youtube_video' item of YouTube Organic result<br>example:<br>vQXvyV0zIP4 |[optional]|
**location_code** | **StrictInt** | search engine location code<br>required field if you don't specify location_name <br>if you use this field, you don't need to specify location_name<br>you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/locations<br>example:<br>2840 |[optional]|
**language_code** | **StrictStr** | search engine language code<br>required field if you don't specify language_name<br>if you use this field, you don't need to specify language_name<br>you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/languages<br>example:<br>en |[optional]|
**device** | **StrictStr** | device type<br>optional field<br>only value: desktop |[optional]|
**location_name** | **StrictStr** | full name of search engine location<br>required field if you don't specify location_code<br>if you use this field, you don't need to specify location_code<br>you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/locations<br>example:<br>United States |[optional]|
**language_name** | **StrictStr** | full name of search engine language<br>required field if you don't specify language_code<br>if you use this field, you don't need to specify language_code<br>you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/languages<br>example:<br>English |[optional]|
**os** | **StrictStr** | device operating system<br>optional field<br>choose from the following values: windows, macos<br>default value: windows |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|