# ReviewMentionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the evaluated criterion | [optional] 
**positive_score** | **float** | positive score by criterion | [optional] 
**positive_count** | **int** | count of positive reviews by criterion | [optional] 
**negative_count** | **int** | count of negative reviews by criterion | [optional] 
**total_count** | **int** | count of all reviews by criterion | [optional] 
**visible_by_default** | **bool** | element is visible by default indicates whether the review element is visible by default | [optional] 

## Example

```python
from dataforseo_client.models.review_mention_info import ReviewMentionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewMentionInfo from a JSON string
review_mention_info_instance = ReviewMentionInfo.from_json(json)
# print the JSON string representation of the object
print(ReviewMentionInfo.to_json())

# convert the object into a dict
review_mention_info_dict = review_mention_info_instance.to_dict()
# create an instance of ReviewMentionInfo from a dict
review_mention_info_form_dict = review_mention_info.from_dict(review_mention_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


