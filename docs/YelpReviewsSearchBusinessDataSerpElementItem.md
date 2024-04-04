# YelpReviewsSearchBusinessDataSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank among all the listed reviews absolute position among all reviews on the list | [optional] 
**position** | **str** | the alignment of the review in SERP can take the following values: left | [optional] 
**review_id** | **str** | the unique identifier of a review received from Yelp example: WvjNtncj8PDZytbofWlC5A | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**timestamp** | **str** | the time of publication indicates timestamp of when the review was listed | [optional] 
**review_text** | **str** | the content of the review | [optional] 
**review_images** | **List[Optional[str]]** | images submitted by the reviewer you will find URLs to the images provided by the author of this review | [optional] 
**user_profile** | [**BusinessDataUserProfileInfo**](BusinessDataUserProfileInfo.md) |  | [optional] 
**responses** | [**List[ReviewResponseItemInfo]**](ReviewResponseItemInfo.md) | text of the owner’s response | [optional] 

## Example

```python
from dataforseo_client.models.yelp_reviews_search_business_data_serp_element_item import YelpReviewsSearchBusinessDataSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of YelpReviewsSearchBusinessDataSerpElementItem from a JSON string
yelp_reviews_search_business_data_serp_element_item_instance = YelpReviewsSearchBusinessDataSerpElementItem.from_json(json)
# print the JSON string representation of the object
print YelpReviewsSearchBusinessDataSerpElementItem.to_json()

# convert the object into a dict
yelp_reviews_search_business_data_serp_element_item_dict = yelp_reviews_search_business_data_serp_element_item_instance.to_dict()
# create an instance of YelpReviewsSearchBusinessDataSerpElementItem from a dict
yelp_reviews_search_business_data_serp_element_item_form_dict = yelp_reviews_search_business_data_serp_element_item.from_dict(yelp_reviews_search_business_data_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


