# MerchantGoogleProductsTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | keyword received in a POST arraykeyword is returned with decoded %## (plus character '+' will be decoded to a space character) |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | search engine domain in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to Google Shopping resultsyou can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | date and time when the result was receivedin the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”example:2019-11-15 12:57:46 +00:00 |[optional]|
**spell** | **SpellInfo** | autocorrection of the search engineif the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection |[optional]|
**item_types** | **List[Optional[StrictStr]]** | types of search results found in Google Shopping SERPcontains types of all search results (items) found in the returned SERPpossible item types:google_shopping_sponsored_carousel, google_shopping_paid, google_shopping_serp, google_shopping_carousel, related_searches |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[BaseMerchantGoogleShoppingProductsElementItem]]** | additional items present in the elementcontains a list of related keywords;if there are none, equals null |[optional]|