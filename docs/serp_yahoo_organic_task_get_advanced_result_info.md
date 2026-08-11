# SerpYahooOrganicTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | <em>keyword received in a POST array<br></em><strong>the keyword is returned with decoded %## (plus symbol '+' will be decoded to a space character)</strong> |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | <em>search engine domain in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**check_url** | **StrictStr** | <em>direct URL to search engine results</em><br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**spell** | **SpellInfo** | <em>autocorrection of the search engine</em><br>if the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection |[optional]|
**refinement_chips** | **RefinementChipsInfo** | <em>search refinement chips</em><br>equals <code>null</code> |[optional]|
**item_types** | **List[Optional[StrictStr]]** | <em>types of search results in SERP</em><br>contains types of search results (<code>items</code>) found in SERP.<br>possible item types:<br><span><a href='#featured_snippet'><code>featured_snippet</code></a>, <a href='#images'><code>images</code></a>, <a href='#local_pack'><code>local_pack</code></a>, <a href='#hotels_pack'><code>hotels_pack</code></a>, <a href='#organic'><code>organic</code></a>, <a href='#paid'><code>paid</code></a>, <a href='#people_also_ask'><code>people_also_ask</code></a>, <a href='#related_searches'><code>related_searches</code></a>, <a href='#shopping'><code>shopping</code></a>, <a href='#recipes'><code>recipes</code></a>, <a href='#top_stories'><code>top_stories</code></a>, <a href='#video'><code>video</code></a></span>, <a href='#ai_overview'><code>ai_overview</code></a></span> |[optional]|
**se_results_count** | **StrictInt** | <em> total number of results in SERP</em> |[optional]|
**pages_count** | **StrictInt** | <em>total pages retrieved</em><br>total number of retrieved SERPs in the result |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <strong><code>items</code></strong> array</em> |[optional]|
**items** | **List[Optional[BaseSerpApiElementItem]]** | <em>additional items present in the element</em><br>if there are none, equals <code>null</code> |[optional]|