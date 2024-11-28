# GoogleReviewsSearchBusinessDataSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the review in SERP can take the following values: right | [optional] 
**xpath** | **str** | the XPath of the review | [optional] 
**review_text** | **str** | the content of the review | [optional] 
**original_review_text** | **str** | original content of the review the original content of the review, no auto-translate applied | [optional] 
**time_ago** | **str** | the time of publication indicates the time (in the ‘time ago’ format) when the review was listed | [optional] 
**timestamp** | **str** | date and time when a review was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**reviews_count** | **int** | total number of reviews submitted by the reviewer | [optional] 
**photos_count** | **int** | total number of photos submitted by the reviewer | [optional] 
**local_guide** | **bool** | indicates whether the reviewer has a ‘local guide’ status | [optional] 
**profile_name** | **str** | profile name of the reviewer | [optional] 
**profile_url** | **str** | URL of the reviewer’s profile | [optional] 
**review_url** | **str** | the URL of the review | [optional] 
**profile_image_url** | **str** | URL of the reviewer’s profile image | [optional] 
**owner_answer** | **str** | text of the owner’s response the owner’s response to the review | [optional] 
**original_owner_answer** | **str** | original text of the owner’s response the original response to the review, no auto-translate applied | [optional] 
**owner_time_ago** | **str** | publication time indicates the time (in the ‘time ago’ format) when the owner submitted the response to the review | [optional] 
**owner_timestamp** | **str** | date and time of the owner’s reply to the review in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**review_id** | **str** | the unique identifier of a review on Google example: ChZDSUhNMG9nS0VJQ0FnSUMxbHFyMFlnEAE | [optional] 
**images** | [**List[ImagesElement]**](ImagesElement.md) | images submitted by the reviewer | [optional] 
**review_highlights** | [**List[ReviewHighlights]**](ReviewHighlights.md) | review highlights contains highlighted review criteria and assessments | [optional] 

## Example

```python
from dataforseo_client.models.google_reviews_search_business_data_serp_element_item import GoogleReviewsSearchBusinessDataSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleReviewsSearchBusinessDataSerpElementItem from a JSON string
google_reviews_search_business_data_serp_element_item_instance = GoogleReviewsSearchBusinessDataSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(GoogleReviewsSearchBusinessDataSerpElementItem.to_json())

# convert the object into a dict
google_reviews_search_business_data_serp_element_item_dict = google_reviews_search_business_data_serp_element_item_instance.to_dict()
# create an instance of GoogleReviewsSearchBusinessDataSerpElementItem from a dict
google_reviews_search_business_data_serp_element_item_from_dict = GoogleReviewsSearchBusinessDataSerpElementItem.from_dict(google_reviews_search_business_data_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


