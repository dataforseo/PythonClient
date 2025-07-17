# GooglePlayReviewsSearch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank among all the listed reviews<br>absolute position among all reviews on the list |[optional]|
**position** | **StrictStr** | the alignment of the review in SERP<br>can take the following values: left |[optional]|
**version** | **StrictStr** | version of the app<br>version of the app for which the review is submitted |[optional]|
**rating** | **RatingElement** | the rating score submitted by the reviewer |[optional]|
**timestamp** | **StrictStr** | date and time when the review was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**id** | **StrictStr** | id of the review |[optional]|
**helpful_count** | **StrictInt** | number of helpful votes<br>indicates how many users considered the review helpful and voted with the thumbs up icon |[optional]|
**title** | **StrictStr** | title of the review<br>Google Play doesn’t provide an option to title reviews, so this parameter will always equal null |[optional]|
**review_text** | **StrictStr** | content of the review |[optional]|
**user_profile** | **AppUserProfileInfo** | user profile of the reviewer |[optional]|
**responses** | **Any** | response from the developer |[optional]|