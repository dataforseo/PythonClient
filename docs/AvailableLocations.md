# AvailableLocations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_code** | **str** | location code | [optional] 
**location_name** | **str** | location name | [optional] 
**country_iso_code** | **str** | ISO country code of the location | [optional] 
**location_type** | **str** | location type possible values: Country, Region | [optional] 

## Example

```python
from dataforseo_client.models.available_locations import AvailableLocations

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableLocations from a JSON string
available_locations_instance = AvailableLocations.from_json(json)
# print the JSON string representation of the object
print(AvailableLocations.to_json())

# convert the object into a dict
available_locations_dict = available_locations_instance.to_dict()
# create an instance of AvailableLocations from a dict
available_locations_form_dict = available_locations.from_dict(available_locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


