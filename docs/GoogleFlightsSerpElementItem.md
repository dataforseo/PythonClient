# GoogleFlightsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the row | [optional] 
**url** | **str** | source URL | [optional] 
**items** | [**List[GoogleFlightsElement]**](GoogleFlightsElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.google_flights_serp_element_item import GoogleFlightsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleFlightsSerpElementItem from a JSON string
google_flights_serp_element_item_instance = GoogleFlightsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(GoogleFlightsSerpElementItem.to_json())

# convert the object into a dict
google_flights_serp_element_item_dict = google_flights_serp_element_item_instance.to_dict()
# create an instance of GoogleFlightsSerpElementItem from a dict
google_flights_serp_element_item_from_dict = GoogleFlightsSerpElementItem.from_dict(google_flights_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


