# TripadvisorReviewSearch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>position within a group of elements with identical <code>type</code> values</em><br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank among all the listed reviews</em><br>absolute position among all reviews on the list |[optional]|
**position** | **StrictStr** | <em>the alignment of the review in SERP</em><br>can take the following values: <code>right</code> |[optional]|
**url** | **StrictStr** | <em>URL of the review</em> |[optional]|
**rating** | **RatingInfo** | <em>the rating score submitted by the reviewer</em> |[optional]|
**date_of_visit** | **StrictStr** | <em>date of the reviewer's visit to the local establishment</em><br>in the UTC format: 'yyyy-mm-dd hh-mm-ss +00:00'<br>example:<br><code>2019-11-15 12:57:46 +00:00</code> |[optional]|
**timestamp** | **StrictStr** | <em>date and time when the review was published</em><br>in the UTC format: 'yyyy-mm-dd hh-mm-ss +00:00'<br>example:<br><code>2019-11-15 12:57:46 +00:00</code> |[optional]|
**review_id** | **StrictStr** | <em>ID of the review</em> |[optional]|
**title** | **StrictStr** | <em>title of the review</em> |[optional]|
**review_text** | **StrictStr** | <em>content of the review</em> |[optional]|
**language** | **StrictStr** | <em>language of the review text</em> |[optional]|
**original_language** | **StrictStr** | <em>language of the untranslated review text</em> |[optional]|
**review_images** | **List[Optional[ImageUrlInfo]]** | <em>contains URLs of the images used in the review</em> |[optional]|
**user_profile** | **BusinessDataUserProfileInfo** | <em>information from the reviewer's profile</em> |[optional]|
**responses** | **List[Optional[ReviewResponseItemInfo]]** | <em>contains information about the owner's response</em> |[optional]|
**review_highlights** | **Any** | <em>review highlights</em><br>contains highlighted review criteria and assessments |[optional]|