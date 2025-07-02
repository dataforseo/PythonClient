# GoogleReviewsSearchBusinessDataSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**position** | **StrictStr** | the alignment of the review in SERP<br>can take the following values: right |[optional]|
**xpath** | **StrictStr** | the XPath of the review |[optional]|
**review_text** | **StrictStr** | the content of the review |[optional]|
**original_review_text** | **StrictStr** | original content of the review<br>the original content of the review, no auto-translate applied |[optional]|
**time_ago** | **StrictStr** | the time of publication<br>indicates the time (in the ‘time ago’ format) when the review was listed |[optional]|
**timestamp** | **StrictStr** | date and time when a review was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**rating** | **RatingInfo** | the rating score submitted by the reviewer |[optional]|
**reviews_count** | **StrictInt** | total number of reviews submitted by the reviewer |[optional]|
**photos_count** | **StrictInt** | total number of photos submitted by the reviewer |[optional]|
**local_guide** | **StrictBool** | indicates whether the reviewer has a ‘local guide’ status |[optional]|
**profile_name** | **StrictStr** | profile name of the reviewer |[optional]|
**profile_url** | **StrictStr** | URL of the reviewer’s profile |[optional]|
**review_url** | **StrictStr** | the URL of the review |[optional]|
**profile_image_url** | **StrictStr** | URL of the reviewer’s profile image |[optional]|
**owner_answer** | **StrictStr** | text of the owner’s response<br>the owner’s response to the review |[optional]|
**original_owner_answer** | **StrictStr** | original text of the owner’s response<br>the original response to the review, no auto-translate applied |[optional]|
**owner_time_ago** | **StrictStr** | publication time<br>indicates the time (in the ‘time ago’ format) when the owner submitted the response to the review |[optional]|
**owner_timestamp** | **StrictStr** | date and time of the owner’s reply to the review<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**review_id** | **StrictStr** | the unique identifier of a review on Google<br>example:<br>ChZDSUhNMG9nS0VJQ0FnSUMxbHFyMFlnEAE |[optional]|
**images** | **List[Optional[ImagesElement]]** | images submitted by the reviewer |[optional]|
**review_highlights** | **List[Optional[ReviewHighlights]]** | review highlights<br>contains highlighted review criteria and assessments |[optional]|