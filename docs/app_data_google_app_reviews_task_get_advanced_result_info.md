# AppDataGoogleAppReviewsTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**app_id** | **StrictStr** | application id received in a POST array |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | search engine domain in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to search engine results<br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**title** | **StrictStr** | title of the app<br>title of the application for which the reviews are collected |[optional]|
**rating** | **RatingInfo** | rating of the app<br>rating of the application for which the reviews are collected |[optional]|
**reviews_count** | **StrictInt** | the total number of reviews |[optional]|
**items_count** | **StrictInt** | the number of reviews items in the results array<br>you can get more results by using the depth parameter when setting a task |[optional]|
**items** | **List[Optional[BaseAppDataSerpElementItem]]** | found reviews<br>you can get more results by using the depth parameter when setting a task |[optional]|