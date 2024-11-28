# DataAppGooglePlayReviewsSearchSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | version of the app version of the app for which the review is submitted | [optional] 
**timestamp** | **str** | date and time when the review was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”; example: 2019-11-15 12:57:46 +00:00 | [optional] 
**id** | **str** | id of the review | [optional] 
**helpful_count** | **int** | number of helpful votes indicates how many users considered the review helpful and voted with the thumbs up icon | [optional] 
**review_text** | **str** | content of the review | [optional] 
**user_profile** | [**AppUserProfileInfo**](AppUserProfileInfo.md) |  | [optional] 
**responses** | [**List[ResponseDataInfo]**](ResponseDataInfo.md) | response from the developer | [optional] 

## Example

```python
from dataforseo_client.models.data_app_google_play_reviews_search_serp_element_item import DataAppGooglePlayReviewsSearchSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataAppGooglePlayReviewsSearchSerpElementItem from a JSON string
data_app_google_play_reviews_search_serp_element_item_instance = DataAppGooglePlayReviewsSearchSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(DataAppGooglePlayReviewsSearchSerpElementItem.to_json())

# convert the object into a dict
data_app_google_play_reviews_search_serp_element_item_dict = data_app_google_play_reviews_search_serp_element_item_instance.to_dict()
# create an instance of DataAppGooglePlayReviewsSearchSerpElementItem from a dict
data_app_google_play_reviews_search_serp_element_item_from_dict = DataAppGooglePlayReviewsSearchSerpElementItem.from_dict(data_app_google_play_reviews_search_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


