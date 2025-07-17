# SerpYoutubeVideoSubtitlesTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**video_id** | **StrictStr** | ID of the video received in a POST array |[optional]|
**se_domain** | **StrictStr** | search engine domain in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to search engine results<br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**spell** | **SpellInfo** | autocorrection of the search engine<br>if the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection |[optional]|
**item_types** | **List[Optional[StrictStr]]** | types of search results in SERP<br>contains types of search results (items) found in SERP.<br>possible item:<br>youtube_subtitles |[optional]|
**unsupported_language** | **StrictBool** | indicates whether the language is unsupported by the system |[optional]|
**translate_language** | **StrictStr** | language code of translated text |[optional]|
**origin_language** | **StrictStr** | language code of original text |[optional]|
**category** | **StrictStr** | the category the video belongs to |[optional]|
**subtitles_count** | **StrictInt** | number of subtitles in the video |[optional]|
**title** | **StrictStr** | title of the video |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[YoutubeSubtitles]]** | elements of search results found in SERP |[optional]|