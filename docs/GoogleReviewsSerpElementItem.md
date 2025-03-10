# GoogleReviewsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**reviews_count** | **int** | the number of reviews | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**place_id** | **str** | the identifier of a place | [optional] 
**feature** | **str** | the additional feature of the review | [optional] 
**cid** | **str** | google-defined client id | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.google_reviews_serp_element_item import GoogleReviewsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleReviewsSerpElementItem from a JSON string
google_reviews_serp_element_item_instance = GoogleReviewsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(GoogleReviewsSerpElementItem.to_json())

# convert the object into a dict
google_reviews_serp_element_item_dict = google_reviews_serp_element_item_instance.to_dict()
# create an instance of GoogleReviewsSerpElementItem from a dict
google_reviews_serp_element_item_from_dict = GoogleReviewsSerpElementItem.from_dict(google_reviews_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


