# SerpYahooOrganicLiveRegularResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | <em>keyword received in a POST array</em><br><strong>keyword is returned with decoded %## (plus character '+' will be decoded to a space character)</strong> |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | <em>search engine domain in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**check_url** | **StrictStr** | <em>direct URL to search engine results<br></em>You can use it to make sure that we provided exact results |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**spell** | **SpellInfo** | <em>autocorrection of the search engine</em><br>if the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection |[optional]|
**refinement_chips** | **RefinementChipsInfo** | <em>search refinement chips</em><br>equals <code>null</code> |[optional]|
**item_types** | **List[Optional[StrictStr]]** | <em>types of search results found in SERP</em><br>contains types of all search results (<code>items</code>) found in the returned SERP<br>possible item types:<br><code>featured_snippet</code>, <code>images</code>, <code>local_pack</code>, <code>hotels_pack</code>, <code>organic</code>, <code>paid</code>, <code>people_also_ask</code>, <code>related_searches</code>, <code>shopping</code>, <code>recipes</code>, <code>top_stories</code>, <code>video</code>, <code>ai_overview</code>;<br><strong>note</strong> that this array contains all types of search results found in the returned SERP;<br>however, this endpoint provides data for <code>organic</code>, <code>paid</code>, and <code>featured_snippet</code> types only;<br>to get all items (including SERP features and rich snippets) found in the returned SERP, please refer to the <a href='/v3/serp/yahoo/organic/task_get/advanced/?bash' rel='noopener noreferrer' target='_blank'>Yahoo Organiс Advanced SERP endpoint</a> |[optional]|
**se_results_count** | **StrictInt** | <em>total number of results in SERP</em> |[optional]|
**pages_count** | **StrictInt** | <em>total pages retrieved</em><br>total number of retrieved SERPs in the result |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <strong><code>items</code></strong> array</em> |[optional]|
**items** | **List[Optional[BaseSerpApiElementItem]]** | <em>items in SERP</em> |[optional]|