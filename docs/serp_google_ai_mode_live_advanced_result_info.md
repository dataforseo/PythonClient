# SerpGoogleAiModeLiveAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | keyword received in a POST arraythe keyword is returned with decoded %## (plus symbol '+' will be decoded to a space character) |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | search engine domain in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to search engine resultsyou can use it to make sure that we provided exact results |[optional]|
**datetime** | **StrictStr** | date and time when the result was receivedin the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”example:2019-11-15 12:57:46 +00:00 |[optional]|
**spell** | **SpellInfo** | autocorrection of the search engineif the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection;in this case, the value will be null |[optional]|
**refinement_chips** | **RefinementChipsInfo** | search refinement chipsin this case, the value will be null |[optional]|
**item_types** | **List[Optional[StrictStr]]** | types of search results in SERPcontains types of search results (items) found in SERP.possible item types:ai_overview |[optional]|
**se_results_count** | **StrictInt** | total number of results in SERP |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[AiModeAiOverviewInfo]]** | items present in the element |[optional]|