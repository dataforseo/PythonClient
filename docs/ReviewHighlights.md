# ReviewHighlights


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | **str** | reviewed feature | [optional] 
**assessment** | **str** | feature assessment | [optional] 

## Example

```python
from dataforseo_client.models.review_highlights import ReviewHighlights

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewHighlights from a JSON string
review_highlights_instance = ReviewHighlights.from_json(json)
# print the JSON string representation of the object
print ReviewHighlights.to_json()

# convert the object into a dict
review_highlights_dict = review_highlights_instance.to_dict()
# create an instance of ReviewHighlights from a dict
review_highlights_form_dict = review_highlights.from_dict(review_highlights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


