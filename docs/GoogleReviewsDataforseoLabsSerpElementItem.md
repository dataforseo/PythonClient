# GoogleReviewsDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reviews_count** | **int** | the number of reviews | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**place_id** | **str** | the identifier of a place | [optional] 
**feature** | **str** | the additional feature of the review | [optional] 
**cid** | **str** | google-defined client id | [optional] 

## Example

```python
from dataforseo_client.models.google_reviews_dataforseo_labs_serp_element_item import GoogleReviewsDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleReviewsDataforseoLabsSerpElementItem from a JSON string
google_reviews_dataforseo_labs_serp_element_item_instance = GoogleReviewsDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print GoogleReviewsDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
google_reviews_dataforseo_labs_serp_element_item_dict = google_reviews_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of GoogleReviewsDataforseoLabsSerpElementItem from a dict
google_reviews_dataforseo_labs_serp_element_item_form_dict = google_reviews_dataforseo_labs_serp_element_item.from_dict(google_reviews_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


