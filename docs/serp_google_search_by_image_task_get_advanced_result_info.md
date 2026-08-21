# SerpGoogleSearchByImageTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**image_url** | **StrictStr** | <em>URL specified in a POST array</em> |[optional]|
**keyword** | **StrictStr** | <em>keyword Google associated with the specified image</em> |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | <em>search engine domain in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**check_url** | **StrictStr** | <em>direct URL to search engine results</em><br>            you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>            in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>            example:<br>            <code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**spell** | **SpellInfo** | <em>autocorrection of the search engine</em><br>            if the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection |[optional]|
**refinement_chips** | **RefinementChipsInfo** | <em>search refinement chips</em><br> |[optional]|
**item_types** | **List[Optional[StrictStr]]** | <em>types of search results in SERP</em><br>            contains types of search results (<code>items</code>) found in SERP.<br>            possible item types:<br>            <code>organic</code>,<br>            <code>images</code> |[optional]|
**se_results_count** | **StrictInt** | <em> total number of results in SERP</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <strong><code>items</code></strong> array</em> |[optional]|
**items** | **List[Optional[BaseSerpApiGoogleSearchByImagesElementItem]]** | <em>items featured in the faq_box</em> |[optional]|