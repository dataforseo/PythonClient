# AppStoreReviewsSearch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank among all the listed reviews<br>absolute position among all reviews on the list |[optional]|
**position** | **StrictStr** | the alignment of the review in SERP<br>can take the following values: left |[optional]|
**version** | **StrictStr** | version of the app<br>version of the app for which the review is submitted |[optional]|
**rating** | **RatingInfo** | the rating score submitted by the reviewer |[optional]|
**timestamp** | **StrictStr** | date and time when the review was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**id** | **StrictStr** | id of the review |[optional]|
**title** | **StrictStr** | title of the review |[optional]|
**review_text** | **StrictStr** | content of the review |[optional]|
**user_profile** | **AppUserProfileInfo** | user profile of the reviewer |[optional]|