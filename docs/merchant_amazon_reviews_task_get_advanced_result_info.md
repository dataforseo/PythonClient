# MerchantAmazonReviewsTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**asin** | **StrictStr** | asin received in a POST array |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | search engine domain in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to search engine results<br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**spell** | **SpellInfo** | autocorrection of the search engine<br>if the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection |[optional]|
**title** | **StrictStr** | title of the product on Amazon<br>the title of the product for which the reviews are collected |[optional]|
**image** | **AiModeImagesElement** | product image data |[optional]|
**rating** | **RatingElement** | rating of the product on Amazon<br>popularity rate based on reviews and displayed in SERP |[optional]|
**reviews_count** | **StrictInt** | the total number of reviews |[optional]|
**item_types** | **List[Optional[StrictStr]]** | type of search results in Amazon SERP<br>contains types of search results (items) found in Amazon SERP;<br>possible item types:<br>amazon_review_item |[optional]|
**items_count** | **StrictInt** | the number of reviews items in the results array<br>you can get more results by using the depth parameter when setting a task |[optional]|
**items** | **List[Optional[AmazonReviewItem]]** | found reviews<br>you can get more results by using the depth parameter when setting a task |[optional]|