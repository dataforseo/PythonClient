# SerpGoogleFinanceMarketsTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | keyword received in a POST array<br>the keyword is returned with decoded %## (plus character ‘+’ will be decoded to a space character) |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | search engine domain in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to search engine results<br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**spell** | **SpellInfo** | autocorrection of the search engine<br>if the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection |[optional]|
**refinement_chips** | **RefinementChipsInfo** | search refinement chips<br>in this case, the value will be null |[optional]|
**item_types** | **List[Optional[StrictStr]]** | types of search results in SERP<br>contains types of search results (items) found in SERP;<br>possible item types: google_finance_hero_groups, google_finance_explore_market_trends, google_finance_news, google_finance_interested, google_finance_people_also_search |[optional]|
**se_results_count** | **StrictInt** | total number of results in SERP |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[BaseSerpApiGoogleFinanceElementItem]]** | market indexes related to the market trends element<br>possible type of items: google_finance_asset_pair_element, google_finance_market_instrument_element, google_finance_market_index_element |[optional]|