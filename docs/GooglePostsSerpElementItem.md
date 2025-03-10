# GooglePostsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**posts_id** | **str** | the identifier of the google_posts feature | [optional] 
**feature** | **str** | the additional feature of the review | [optional] 
**cid** | **str** | google-defined client id | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.google_posts_serp_element_item import GooglePostsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GooglePostsSerpElementItem from a JSON string
google_posts_serp_element_item_instance = GooglePostsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(GooglePostsSerpElementItem.to_json())

# convert the object into a dict
google_posts_serp_element_item_dict = google_posts_serp_element_item_instance.to_dict()
# create an instance of GooglePostsSerpElementItem from a dict
google_posts_serp_element_item_from_dict = GooglePostsSerpElementItem.from_dict(google_posts_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


