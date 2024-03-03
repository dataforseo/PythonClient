# GoogleFlightsElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**description** | **str** | description of the results element in SERP | [optional] 
**url** | **str** | URL | [optional] 

## Example

```python
from dataforseo_client.models.google_flights_element import GoogleFlightsElement

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleFlightsElement from a JSON string
google_flights_element_instance = GoogleFlightsElement.from_json(json)
# print the JSON string representation of the object
print GoogleFlightsElement.to_json()

# convert the object into a dict
google_flights_element_dict = google_flights_element_instance.to_dict()
# create an instance of GoogleFlightsElement from a dict
google_flights_element_form_dict = google_flights_element.from_dict(google_flights_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


