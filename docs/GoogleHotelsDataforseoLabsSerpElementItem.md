# GoogleHotelsDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**hotel_identifier** | **str** | unique hotel identifier unique hotel identifier assigned by Google; example: \&quot;CgoIjaeSlI6CnNpVEAE\&quot; | [optional] 
**url** | **str** | relevant URL of the Ad element in SERP | [optional] 

## Example

```python
from dataforseo_client.models.google_hotels_dataforseo_labs_serp_element_item import GoogleHotelsDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleHotelsDataforseoLabsSerpElementItem from a JSON string
google_hotels_dataforseo_labs_serp_element_item_instance = GoogleHotelsDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print GoogleHotelsDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
google_hotels_dataforseo_labs_serp_element_item_dict = google_hotels_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of GoogleHotelsDataforseoLabsSerpElementItem from a dict
google_hotels_dataforseo_labs_serp_element_item_form_dict = google_hotels_dataforseo_labs_serp_element_item.from_dict(google_hotels_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


