# ThirdPartyReviewsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**reviews_count** | **int** | the number of reviews | [optional] 
**title** | **str** | title of the row | [optional] 
**url** | **str** | source URL | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.third_party_reviews_serp_element_item import ThirdPartyReviewsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyReviewsSerpElementItem from a JSON string
third_party_reviews_serp_element_item_instance = ThirdPartyReviewsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyReviewsSerpElementItem.to_json())

# convert the object into a dict
third_party_reviews_serp_element_item_dict = third_party_reviews_serp_element_item_instance.to_dict()
# create an instance of ThirdPartyReviewsSerpElementItem from a dict
third_party_reviews_serp_element_item_from_dict = ThirdPartyReviewsSerpElementItem.from_dict(third_party_reviews_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


