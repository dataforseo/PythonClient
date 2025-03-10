# GoogleHotelsDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** | unique hotel identifier unique hotel identifier assigned by Google; example: \&quot;CgoIjaeSlI6CnNpVEAE\&quot; | [optional] 
**url** | **str** | relevant URL | [optional] 

## Example

```python
from dataforseo_client.models.google_hotels_dataforseo_labs_serp_element_item import GoogleHotelsDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleHotelsDataforseoLabsSerpElementItem from a JSON string
google_hotels_dataforseo_labs_serp_element_item_instance = GoogleHotelsDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(GoogleHotelsDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
google_hotels_dataforseo_labs_serp_element_item_dict = google_hotels_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of GoogleHotelsDataforseoLabsSerpElementItem from a dict
google_hotels_dataforseo_labs_serp_element_item_from_dict = GoogleHotelsDataforseoLabsSerpElementItem.from_dict(google_hotels_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


