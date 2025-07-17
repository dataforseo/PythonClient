# TripadvisorReviewSearch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank among all the listed reviews<br>absolute position among all reviews on the list |[optional]|
**position** | **StrictStr** | the alignment of the review in SERP<br>can take the following values: right |[optional]|
**url** | **StrictStr** | URL of the review |[optional]|
**rating** | **RatingElement** | the rating score submitted by the reviewer |[optional]|
**date_of_visit** | **StrictStr** | date of the reviewer’s visit to the local establishment<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**timestamp** | **StrictStr** | date and time when the review was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**review_id** | **StrictStr** | ID of the review |[optional]|
**title** | **StrictStr** | title of the review |[optional]|
**review_text** | **StrictStr** | content of the review |[optional]|
**language** | **StrictStr** | language of the review text |[optional]|
**original_language** | **StrictStr** | language of the untranslated review text |[optional]|
**review_images** | **List[Optional[ImageUrlInfo]]** | contains URLs of the images used in the review |[optional]|
**user_profile** | **BusinessDataUserProfileInfo** | information from the reviewer’s profile |[optional]|
**responses** | **List[Optional[ReviewResponseItemInfo]]** | contains information about the owner’s response |[optional]|