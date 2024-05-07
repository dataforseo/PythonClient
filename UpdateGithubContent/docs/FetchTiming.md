# FetchTiming


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_time** | **int** | indicates how many milliseconds it took to fetch a resource | [optional] 
**fetch_start** | **int** | time to start downloading the resource the amount of time a browser needs to start downloading a resource | [optional] 
**fetch_end** | **int** | time to complete downloading the resource the amount of time a browser needs to complete downloading a resource | [optional] 

## Example

```python
from dataforseo_client.models.fetch_timing import FetchTiming

# TODO update the JSON string below
json = "{}"
# create an instance of FetchTiming from a JSON string
fetch_timing_instance = FetchTiming.from_json(json)
# print the JSON string representation of the object
print FetchTiming.to_json()

# convert the object into a dict
fetch_timing_dict = fetch_timing_instance.to_dict()
# create an instance of FetchTiming from a dict
fetch_timing_form_dict = fetch_timing.from_dict(fetch_timing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


