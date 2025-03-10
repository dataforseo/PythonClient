# GooglePostsDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posts_id** | **str** | the identifier of the google_posts feature | [optional] 
**feature** | **str** | the additional feature of the review | [optional] 
**cid** | **str** | google-defined client id unique id of a local establishment; can be used with Google Reviews API to get a full list of reviews | [optional] 

## Example

```python
from dataforseo_client.models.google_posts_dataforseo_labs_serp_element_item import GooglePostsDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GooglePostsDataforseoLabsSerpElementItem from a JSON string
google_posts_dataforseo_labs_serp_element_item_instance = GooglePostsDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(GooglePostsDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
google_posts_dataforseo_labs_serp_element_item_dict = google_posts_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of GooglePostsDataforseoLabsSerpElementItem from a dict
google_posts_dataforseo_labs_serp_element_item_from_dict = GooglePostsDataforseoLabsSerpElementItem.from_dict(google_posts_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


