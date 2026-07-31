# TrustpilotReviewSearch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>position within a group of elements with identical <code>type</code> values</em><br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank among all the listed reviews</em><br>absolute position among all reviews on the list |[optional]|
**position** | **StrictStr** | <em>the alignment of the review in SERP</em><br>can take the following values: <code>right</code> |[optional]|
**url** | **StrictStr** | <em>the URL of the review</em> |[optional]|
**rating** | **RatingInfo** | <em>the rating score submitted by the reviewer</em> |[optional]|
**verified** | **StrictBool** | <em>indicates whether the review has the 'Verified' mark</em> |[optional]|
**language** | **StrictStr** | <em>the language of the review</em> |[optional]|
**timestamp** | **StrictStr** | <em>date and time when a review was published</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code>2019-11-15 12:57:46 +00:00</code> |[optional]|
**title** | **StrictStr** | <em>the title of the review</em> |[optional]|
**review_text** | **StrictStr** | <em>the content of the review</em> |[optional]|
**review_images** | **List[Optional[StrictStr]]** | <em>images submitted by the reviewer</em><br>displays URLs to the images provided by the author of the review;<br><strong>please note</strong> that Trustpilot doesn't allow adding images to reviews, so the <code>review_images</code> parameter will always equal <code>null</code> |[optional]|
**user_profile** | **BusinessDataUserProfileInfo** | <em>user profile of the reviewer</em> |[optional]|
**responses** | **List[Optional[ReviewResponseItemInfo]]** | <em>owner's response to the submitted review</em> |[optional]|