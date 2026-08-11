# SerpYoutubeVideoSubtitlesLiveAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**video_id** | **StrictStr** | <em>ID of the video received in a POST array</em> |[optional]|
**se_domain** | **StrictStr** | <em>search engine domain in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**check_url** | **StrictStr** | <em>direct URL to search engine results<br></em>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**spell** | **SpellInfo** | <em>autocorrection of the search engine</em><br>if the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection |[optional]|
**item_types** | **List[Optional[StrictStr]]** | <em>types of search results in SERP</em><br>contains types of search results (<code>items</code>) found in SERP.<br>possible item:<br><code>youtube_subtitles</code> |[optional]|
**unsupported_language** | **StrictBool** | <em>indicates whether the language is unsupported by the system</em> |[optional]|
**translate_language** | **StrictStr** | <em>language code of translated text</em> |[optional]|
**origin_language** | **StrictStr** | <em>language code of original text</em> |[optional]|
**category** | **StrictStr** | <em>the category the video belongs to</em><br><strong>Note:</strong> this field is deprecated and always returns <code>null</code> |[optional]|
**subtitles_count** | **StrictInt** | <em>number of subtitles in the video</em> |[optional]|
**title** | **StrictStr** | <em>title of the video</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <strong><code>items</code></strong> array</em> |[optional]|
**items** | **List[Optional[YoutubeSubtitles]]** | <em>elements of search results found in SERP</em> |[optional]|