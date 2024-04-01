# ReviewResponseItemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | the title of response | [optional] 
**text** | **str** | the content of response | [optional] 
**timestamp** | **str** | the time of publication | [optional] 

## Example

```python
from dataforseo_client.models.review_response_item_info import ReviewResponseItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewResponseItemInfo from a JSON string
review_response_item_info_instance = ReviewResponseItemInfo.from_json(json)
# print the JSON string representation of the object
print(ReviewResponseItemInfo.to_json())

# convert the object into a dict
review_response_item_info_dict = review_response_item_info_instance.to_dict()
# create an instance of ReviewResponseItemInfo from a dict
review_response_item_info_form_dict = review_response_item_info.from_dict(review_response_item_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


