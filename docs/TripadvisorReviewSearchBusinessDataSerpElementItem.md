# TripadvisorReviewSearchBusinessDataSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the review in SERP can take the following values: right | [optional] 
**url** | **str** | URL of the review | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**date_of_visit** | **str** | date of the reviewer’s visit to the local establishment in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**timestamp** | **str** | date and time when the review was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**title** | **str** | title of the review | [optional] 
**review_text** | **str** | content of the review | [optional] 
**review_images** | [**List[ImageUrlInfo]**](ImageUrlInfo.md) | contains URLs of the images used in the review | [optional] 
**user_profile** | [**BusinessDataUserProfileInfo**](BusinessDataUserProfileInfo.md) |  | [optional] 
**responses** | [**List[ReviewResponseItemInfo]**](ReviewResponseItemInfo.md) | contains information about the owner’s response | [optional] 
**review_highlights** | [**List[ReviewHighlights]**](ReviewHighlights.md) | review highlights contains highlighted review criteria and assessments | [optional] 

## Example

```python
from dataforseo_client.models.tripadvisor_review_search_business_data_serp_element_item import TripadvisorReviewSearchBusinessDataSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of TripadvisorReviewSearchBusinessDataSerpElementItem from a JSON string
tripadvisor_review_search_business_data_serp_element_item_instance = TripadvisorReviewSearchBusinessDataSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(TripadvisorReviewSearchBusinessDataSerpElementItem.to_json())

# convert the object into a dict
tripadvisor_review_search_business_data_serp_element_item_dict = tripadvisor_review_search_business_data_serp_element_item_instance.to_dict()
# create an instance of TripadvisorReviewSearchBusinessDataSerpElementItem from a dict
tripadvisor_review_search_business_data_serp_element_item_from_dict = TripadvisorReviewSearchBusinessDataSerpElementItem.from_dict(tripadvisor_review_search_business_data_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


