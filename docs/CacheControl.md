# CacheControl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cachable** | **bool** | indicates whether the page is cacheable | [optional] 
**ttl** | **int** | time to live the amount of time the browser caches a resource | [optional] 

## Example

```python
from dataforseo_client.models.cache_control import CacheControl

# TODO update the JSON string below
json = "{}"
# create an instance of CacheControl from a JSON string
cache_control_instance = CacheControl.from_json(json)
# print the JSON string representation of the object
print CacheControl.to_json()

# convert the object into a dict
cache_control_dict = cache_control_instance.to_dict()
# create an instance of CacheControl from a dict
cache_control_form_dict = cache_control.from_dict(cache_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


