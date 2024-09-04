# TrustpilotReviewSearchBusinessDataSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the review in SERP can take the following values: right | [optional] 
**url** | **str** | the URL of the review | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**verified** | **bool** | indicates whether the review has the “Verified” mark | [optional] 
**language** | **str** | the language of the review | [optional] 
**timestamp** | **str** | date and time when a review was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**title** | **str** | the title of the review | [optional] 
**review_text** | **str** | the content of the review | [optional] 
**review_images** | **List[str]** | images submitted by the reviewer displays URLs to the images provided by the author of the review; please note that Trustpilot doesn’t allow adding images to reviews, so the review_images parameter will always equal null | [optional] 
**user_profile** | [**BusinessDataUserProfileInfo**](BusinessDataUserProfileInfo.md) |  | [optional] 
**responses** | [**List[ReviewResponseItemInfo]**](ReviewResponseItemInfo.md) | owner’s response to the submitted review | [optional] 

## Example

```python
from dataforseo_client.models.trustpilot_review_search_business_data_serp_element_item import TrustpilotReviewSearchBusinessDataSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of TrustpilotReviewSearchBusinessDataSerpElementItem from a JSON string
trustpilot_review_search_business_data_serp_element_item_instance = TrustpilotReviewSearchBusinessDataSerpElementItem.from_json(json)
# print the JSON string representation of the object
print TrustpilotReviewSearchBusinessDataSerpElementItem.to_json()

# convert the object into a dict
trustpilot_review_search_business_data_serp_element_item_dict = trustpilot_review_search_business_data_serp_element_item_instance.to_dict()
# create an instance of TrustpilotReviewSearchBusinessDataSerpElementItem from a dict
trustpilot_review_search_business_data_serp_element_item_form_dict = trustpilot_review_search_business_data_serp_element_item.from_dict(trustpilot_review_search_business_data_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


