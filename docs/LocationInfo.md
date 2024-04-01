# LocationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the event’s venue | [optional] 
**address** | **str** | address of the event’s venue | [optional] 
**url** | **str** | URL to the event’s venue on google maps | [optional] 
**cid** | **str** | google-defined client id unique id of a local establishment; can be used with Google Reviews API to get a full list of reviews | [optional] 
**feature_id** | **str** | the unique identifier of the element in SERP | [optional] 

## Example

```python
from dataforseo_client.models.location_info import LocationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LocationInfo from a JSON string
location_info_instance = LocationInfo.from_json(json)
# print the JSON string representation of the object
print(LocationInfo.to_json())

# convert the object into a dict
location_info_dict = location_info_instance.to_dict()
# create an instance of LocationInfo from a dict
location_info_form_dict = location_info.from_dict(location_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


