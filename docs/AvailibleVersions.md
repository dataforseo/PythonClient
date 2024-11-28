# AvailibleVersions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | lighthouse version | [optional] 
**default** | **bool** | the version is used by default if false, the version is not used by default and should be specified in the corresponding field of the POST request if necessary | [optional] 

## Example

```python
from dataforseo_client.models.availible_versions import AvailibleVersions

# TODO update the JSON string below
json = "{}"
# create an instance of AvailibleVersions from a JSON string
availible_versions_instance = AvailibleVersions.from_json(json)
# print the JSON string representation of the object
print(AvailibleVersions.to_json())

# convert the object into a dict
availible_versions_dict = availible_versions_instance.to_dict()
# create an instance of AvailibleVersions from a dict
availible_versions_from_dict = AvailibleVersions.from_dict(availible_versions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


