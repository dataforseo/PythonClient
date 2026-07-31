# GooglePlayReviewsSearch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>position within a group of elements with identical <code>type</code> values</em><br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank among all the listed reviews</em><br>absolute position among all reviews on the list |[optional]|
**position** | **StrictStr** | <em>the alignment of the review in SERP</em><br>can take the following values: <code>left</code> |[optional]|
**version** | **StrictStr** | <em>version of the app</em><br>version of the app for which the review is submitted |[optional]|
**rating** | **RatingInfo** | <em>the rating score submitted by the reviewer</em> |[optional]|
**timestamp** | **StrictStr** | <em>date and time when the review was published</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br><code>2019-11-15 12:57:46 +00:00</code> |[optional]|
**id** | **StrictStr** | <em>id of the review</em> |[optional]|
**helpful_count** | **StrictInt** | <em>number of helpful votes</em><br>indicates how many users considered the review helpful and voted with the thumbs up icon |[optional]|
**title** | **StrictStr** | <em>title of the review</em><br>Google Play doesn't provide an option to title reviews, so this parameter will always equal <code>null</code> |[optional]|
**review_text** | **StrictStr** | <em>content of the review</em> |[optional]|
**user_profile** | **AppUserProfileInfo** | <em>user profile of the reviewer</em> |[optional]|
**responses** | **List[Optional[ResponseDataInfo]]** | <em>response from the developer</em> |[optional]|