# SerpBaiduOrganicTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | <em>keyword received in a POST array<br><br>        </em><strong>the keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character)</strong> |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | <em>search engine domain in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**check_url** | **StrictStr** | <em>direct URL to search engine results</em><br><br>            you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br><br>            in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br><br>            example:<br><br>            <code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**spell** | **SpellInfo** | <em>autocorrection of the search engine</em><br><br>            if the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection |[optional]|
**refinement_chips** | **RefinementChipsInfo** | <em>search refinement chips</em><br><br>            equals <code>null</code> |[optional]|
**item_types** | **List[Optional[StrictStr]]** | <em>types of search results in SERP</em><br><br>            contains types of search results (<code>items</code>) found in SERP.<br><br>            possible item types:<br><br>            <code>images</code>, <code>local_pack</code>, <code>map</code>, <code>organic</code>, <code>paid</code>, <code>related_searches</code>, <code>video</code>, <code>stocks_box</code>, <code>dictionary</code>, <code>shopping</code> |[optional]|
**se_results_count** | **StrictInt** | <em> total number of results in SERP</em> |[optional]|
**pages_count** | **StrictInt** | <em>total pages retrieved</em><br><br>            total number of retrieved SERPs in the result |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <strong><code>items</code></strong> array</em> |[optional]|
**items** | **List[Optional[BaseSerpApiElementItem]]** | <em>additional items present in the element</em><br><br>            if there are none, equals <code>null</code> |[optional]|