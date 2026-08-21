# SerpGoogleFinanceMarketsLiveAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | <em>keyword received in a POST array</em><br><strong>the keyword is returned with decoded %## (plus character '+' will be decoded to a space character)</strong> |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | <em>search engine domain in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**check_url** | **StrictStr** | <em>direct URL to search engine results</em><br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**spell** | **SpellInfo** | <em>autocorrection of the search engine</em><br>if the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection;<br>in this case, the value will be <code>null</code> |[optional]|
**refinement_chips** | **RefinementChipsInfo** | <em>search refinement chips</em><br>in this case, the value will be <code>null</code> |[optional]|
**item_types** | **List[Optional[StrictStr]]** | <em>types of search results in SERP</em><br>contains types of search results (<code>items</code>) found in SERP;<br>possible item types: <span><a href='#google_finance_hero_groups'><code>google_finance_hero_groups</code></a>, <a href='#google_finance_explore_market_trends'><code>google_finance_explore_market_trends</code></a>, <a href='#google_finance_news'><code>google_finance_news</code></a>, <a href='#google_finance_interested'><code>google_finance_interested</code></a>, <a href='#google_finance_people_also_search'><code>google_finance_people_also_search</code></a> |[optional]|
**se_results_count** | **StrictInt** | <em> total number of results in SERP</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <strong><code>items</code></strong> array</em> |[optional]|
**items** | **List[Optional[BaseSerpApiGoogleFinanceElementItem]]** | <em>elements of search results found in SERP</em> |[optional]|