# TripadvisorReviewSearchBusinessDataSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**position** | **StrictStr** | the alignment of the review in SERP<br>can take the following values: right |[optional]|
**url** | **StrictStr** | URL of the review |[optional]|
**rating** | **RatingInfo** | the rating score submitted by the reviewer |[optional]|
**date_of_visit** | **StrictStr** | date of the reviewer’s visit to the local establishment<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**timestamp** | **StrictStr** | date and time when the review was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**title** | **StrictStr** | title of the review |[optional]|
**review_text** | **StrictStr** | content of the review |[optional]|
**review_images** | **List[Optional[ImageUrlInfo]]** | contains URLs of the images used in the review |[optional]|
**user_profile** | **BusinessDataUserProfileInfo** | information from the reviewer’s profile |[optional]|
**responses** | **List[Optional[ReviewResponseItemInfo]]** | contains information about the owner’s response |[optional]|
**review_highlights** | **List[Optional[ReviewHighlights]]** | review highlights<br>contains highlighted review criteria and assessments |[optional]|