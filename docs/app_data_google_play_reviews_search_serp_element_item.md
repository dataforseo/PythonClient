# AppDataGooglePlayReviewsSearchSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**version** | **StrictStr** | version of the app<br>version of the app for which the review is submitted |[optional]|
**timestamp** | **StrictStr** | date and time when the review was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**id** | **StrictStr** | id of the review |[optional]|
**helpful_count** | **StrictInt** | number of helpful votes<br>indicates how many users considered the review helpful and voted with the thumbs up icon |[optional]|
**review_text** | **StrictStr** | content of the review |[optional]|
**user_profile** | **AppUserProfileInfo** | user profile of the reviewer |[optional]|
**responses** | **List[Optional[ResponseDataInfo]]** | response from the developer |[optional]|