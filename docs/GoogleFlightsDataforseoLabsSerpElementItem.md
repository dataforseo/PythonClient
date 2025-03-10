# GoogleFlightsDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**url** | **str** | relevant URL | [optional] 
**items** | [**List[GoogleFlightsElement]**](GoogleFlightsElement.md) | additional items present in the element if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.google_flights_dataforseo_labs_serp_element_item import GoogleFlightsDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleFlightsDataforseoLabsSerpElementItem from a JSON string
google_flights_dataforseo_labs_serp_element_item_instance = GoogleFlightsDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(GoogleFlightsDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
google_flights_dataforseo_labs_serp_element_item_dict = google_flights_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of GoogleFlightsDataforseoLabsSerpElementItem from a dict
google_flights_dataforseo_labs_serp_element_item_from_dict = GoogleFlightsDataforseoLabsSerpElementItem.from_dict(google_flights_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


