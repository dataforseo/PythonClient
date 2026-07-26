# MerchantAmazonProductsLiveAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | <em>keyword received in a POST array</em><br><strong>keyword is returned with decoded %## (plus character '+' will be decoded to a space character)</strong> |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | <em>search engine domain in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**check_url** | **StrictStr** | <em>direct URL to Amazon results</em><br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**spell** | **SpellInfo** | <em>autocorrection of the search engine</em><br>if the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection |[optional]|
**item_types** | **List[Optional[StrictStr]]** | <em>types of search results found in Amazon SERP</em><br>contains types of all search results (<code>items</code>) found in the returned SERP<br>possible item types:<br><code>amazon_serp</code>, <code>amazon_paid</code>, <code>editorial_recommendations</code>, <code>top_rated_from_our_brands</code>, <code>related_searches</code> |[optional]|
**se_results_count** | **StrictInt** | <em>search engine results count</em> |[optional]|
**categories** | **Any** | <em>amazon product departments and subcategories</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <strong><code>items</code></strong> array</em> |[optional]|
**items** | **List[Optional[BaseMerchantAmazonElementItem]]** | <em>Amazon product items</em> |[optional]|