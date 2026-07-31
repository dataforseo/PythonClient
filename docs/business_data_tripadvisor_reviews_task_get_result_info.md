# BusinessDataTripadvisorReviewsTaskGetResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**url_path** | **StrictStr** | <em>URL path received in a POST array</em> |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | <em>search engine domain in a POST array</em> |[optional]|
**check_url** | **StrictStr** | <em>direct URL to search engine results</em><br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**title** | **StrictStr** | <em>title of the 'reviews' element in SERP</em><br>the name of the local establishment for which the reviews are collected |[optional]|
**location** | **StrictStr** | <em>location of the local establishment</em><br>address of the local establishment for which the reviews are collected |[optional]|
**reviews_count** | **StrictInt** | <em>the total number of reviews</em> |[optional]|
**rating** | **RatingInfo** | <em>rating of the corresponding local establishment</em><br>popularity rate based on reviews and displayed in SERP |[optional]|
**rating_distribution** | **Dict[str, Optional[StrictInt]]** | <em>rating distribution by votes</em><br>the distribution of votes across the rating in the range from 1 to 5 |[optional]|
**items_count** | **StrictInt** | <em>the number of reviews items in the results array</em><br>you can get more results by using the <code>depth</code> parameter when setting a task |[optional]|
**items** | **List[Optional[TripadvisorReviewSearch]]** | <em>found reviews</em><br>you can get more results by using the <code>depth</code> parameter when setting a task |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|