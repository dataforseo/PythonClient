# SerpYoutubeVideoCommentsLiveAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**video_id** | **StrictStr** | ID of the video received in a POST array |[optional]|
**se_domain** | **StrictStr** | search engine domain in a POST array |[optional]|
**location_code** | **StrictFloat** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to search engine results<br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**spell** | **SpellInfo** | autocorrection of the search engine<br>if the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection |[optional]|
**item_types** | **List[Optional[StrictStr]]** | types of search results in SERP<br>contains types of search results (items) found in SERP.<br>possible item:<br>youtube_comment |[optional]|
**title** | **StrictStr** | title of the video |[optional]|
**comments_count** | **StrictFloat** | number of comments on the video |[optional]|
**items_count** | **StrictFloat** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[BaseYoutubeSerpElementItem]]** | elements of search results found in SERP |[optional]|