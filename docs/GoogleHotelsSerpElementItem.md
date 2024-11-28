# GoogleHotelsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** | unique hotel identifier unique hotel identifier assigned by Google; example: \&quot;CgoIjaeSlI6CnNpVEAE\&quot; | [optional] 
**url** | **str** | source URL | [optional] 
**cid** | **str** | google-defined client id | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.google_hotels_serp_element_item import GoogleHotelsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleHotelsSerpElementItem from a JSON string
google_hotels_serp_element_item_instance = GoogleHotelsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(GoogleHotelsSerpElementItem.to_json())

# convert the object into a dict
google_hotels_serp_element_item_dict = google_hotels_serp_element_item_instance.to_dict()
# create an instance of GoogleHotelsSerpElementItem from a dict
google_hotels_serp_element_item_from_dict = GoogleHotelsSerpElementItem.from_dict(google_hotels_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


