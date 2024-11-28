# GpsCoordinatesLocationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | latitude coordinate of the hotel in google maps example: \&quot;latitude\&quot;: 51.584091 | [optional] 
**longitude** | **float** | longitude coordinate of the hotel in google maps example: \&quot;longitude\&quot;: -0.31365919999999997 | [optional] 

## Example

```python
from dataforseo_client.models.gps_coordinates_location_info import GpsCoordinatesLocationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GpsCoordinatesLocationInfo from a JSON string
gps_coordinates_location_info_instance = GpsCoordinatesLocationInfo.from_json(json)
# print the JSON string representation of the object
print(GpsCoordinatesLocationInfo.to_json())

# convert the object into a dict
gps_coordinates_location_info_dict = gps_coordinates_location_info_instance.to_dict()
# create an instance of GpsCoordinatesLocationInfo from a dict
gps_coordinates_location_info_from_dict = GpsCoordinatesLocationInfo.from_dict(gps_coordinates_location_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


