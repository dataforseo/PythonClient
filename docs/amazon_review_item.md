# AmazonReviewItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank among all the listed reviews<br>absolute position among all reviews on the list |[optional]|
**position** | **StrictStr** | the alignment of the review in SERP<br>can take the following values: right |[optional]|
**xpath** | **StrictStr** | the XPath of the element |[optional]|
**verified** | **StrictBool** | indicates whether the review has the “Verified Purchase” mark |[optional]|
**subtitle** | **StrictStr** | subtitle of the review |[optional]|
**helpful_votes** | **StrictStr** | helpful votes count<br>number of users who clicked on the ‘Helpful” button under the review text |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | images of the product submitted by the reviewer |[optional]|
**videos** | **List[Optional[VideoElement]]** | videos of the product submitted by the reviewer |[optional]|
**user_profile** | **UserProfileInfo** | user profile of the reviewer |[optional]|
**title** | **StrictStr** | title of the review |[optional]|
**url** | **StrictStr** | URL to the reviewer’s profile |[optional]|
**review_text** | **StrictStr** | content of the review |[optional]|
**publication_date** | **StrictStr** | date and time when the review was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**rating** | **RatingInfo** | the rating score submitted by the reviewer |[optional]|