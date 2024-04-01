# DataAppAppStoreReviewsSearchSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank among all the listed reviews absolute position among all reviews on the list | [optional] 
**position** | **str** | the alignment of the review in SERP can take the following values: left | [optional] 
**version** | **str** | version of the app version of the app for which the review is submitted | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**timestamp** | **str** | date and time when the review was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”; example: 2019-11-15 12:57:46 +00:00 | [optional] 
**id** | **str** | id of the review | [optional] 
**title** | **str** | title of the review | [optional] 
**review_text** | **str** | content of the review | [optional] 
**user_profile** | [**AppUserProfileInfo**](AppUserProfileInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.data_app_app_store_reviews_search_serp_element_item import DataAppAppStoreReviewsSearchSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataAppAppStoreReviewsSearchSerpElementItem from a JSON string
data_app_app_store_reviews_search_serp_element_item_instance = DataAppAppStoreReviewsSearchSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(DataAppAppStoreReviewsSearchSerpElementItem.to_json())

# convert the object into a dict
data_app_app_store_reviews_search_serp_element_item_dict = data_app_app_store_reviews_search_serp_element_item_instance.to_dict()
# create an instance of DataAppAppStoreReviewsSearchSerpElementItem from a dict
data_app_app_store_reviews_search_serp_element_item_form_dict = data_app_app_store_reviews_search_serp_element_item.from_dict(data_app_app_store_reviews_search_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


