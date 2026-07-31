# BusinessDataTrustpilotReviewsTaskGetResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **StrictStr** | <em>domain of the business entity</em> |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | <em>search engine domain in a POST array</em> |[optional]|
**check_url** | **StrictStr** | <em>direct URL to search engine results</em><br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**title** | **StrictStr** | <em>title of the 'reviews' element on Trustpilot</em><br>the name of the business entity for which the reviews are collected |[optional]|
**location** | **StrictStr** | <em>location of the business entity as specified on Trustpilot</em><br>address of the business entity for which the reviews are collected |[optional]|
**reviews_count** | **StrictStr** | <em>the total number of reviews</em> |[optional]|
**rating** | **Any** | <em>rating of the corresponding business entity</em><br>popularity rate based on reviews and displayed in SERP |[optional]|
**items_count** | **StrictInt** | <em>the number of items in the results array</em><br>you can get more results by using the <code>depth</code> parameter when setting a task |[optional]|
**items** | **List[Optional[TrustpilotReviewSearch]]** | <em>found reviews</em><br>you can get more results by using the <code>depth</code> parameter when setting a task |[optional]|