# TrustpilotReviewSearch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank among all the listed reviews<br>absolute position among all reviews on the list |[optional]|
**position** | **StrictStr** | the alignment of the review in SERP<br>can take the following values: right |[optional]|
**url** | **StrictStr** | the URL of the review |[optional]|
**rating** | **RatingInfo** | the rating score submitted by the reviewer |[optional]|
**verified** | **StrictBool** | indicates whether the review has the “Verified” mark |[optional]|
**language** | **StrictStr** | the language of the review |[optional]|
**timestamp** | **StrictStr** | date and time when a review was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**title** | **StrictStr** | the title of the review |[optional]|
**review_text** | **StrictStr** | the content of the review |[optional]|
**review_images** | **List[Optional[StrictStr]]** | images submitted by the reviewer<br>displays URLs to the images provided by the author of the review;<br>please note that Trustpilot doesn’t allow adding images to reviews, so the review_images parameter will always equal null |[optional]|
**user_profile** | **BusinessDataUserProfileInfo** | user profile of the reviewer |[optional]|
**responses** | **List[Optional[ReviewResponseItemInfo]]** | owner’s response to the submitted review |[optional]|