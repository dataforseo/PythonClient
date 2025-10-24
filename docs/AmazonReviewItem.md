# AmazonReviewItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**rank_group** | **number** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank among all the listed reviews<br>absolute position among all reviews on the list |[optional]|
**position** | **string** | the alignment of the review in SERP<br>can take the following values: right |[optional]|
**xpath** | **string** | the XPath of the element |[optional]|
**verified** | **boolean** | indicates whether the review has the “Verified Purchase” mark |[optional]|
**subtitle** | **string** | subtitle of the review |[optional]|
**helpful_votes** | **string** | helpful votes count<br>number of users who clicked on the ‘Helpful” button under the review text |[optional]|
**images** | **AiModeImagesElementInfo[]** | images of the product submitted by the reviewer |[optional]|
**videos** | **VideoElement[]** | videos of the product submitted by the reviewer |[optional]|
**user_profile** | **UserProfileInfo** | user profile of the reviewer |[optional]|
**title** | **string** | title of the review |[optional]|
**url** | **string** | URL to the reviewer’s profile |[optional]|
**review_text** | **string** | content of the review |[optional]|
**publication_date** | **string** | date and time when the review was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**rating** | **RatingInfo** | the rating score submitted by the reviewer |[optional]|