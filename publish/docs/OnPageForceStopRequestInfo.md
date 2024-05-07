# OnPageForceStopRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the task required field you can get this ID in the response of the Task POST endpoint example: “07131248-1535-0216-1000-17384017ad04” note: you can set up to 1000 id values as separate objects in the POST array | [optional] 

## Example

```python
from dataforseo_client.models.on_page_force_stop_request_info import OnPageForceStopRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageForceStopRequestInfo from a JSON string
on_page_force_stop_request_info_instance = OnPageForceStopRequestInfo.from_json(json)
# print the JSON string representation of the object
print OnPageForceStopRequestInfo.to_json()

# convert the object into a dict
on_page_force_stop_request_info_dict = on_page_force_stop_request_info_instance.to_dict()
# create an instance of OnPageForceStopRequestInfo from a dict
on_page_force_stop_request_info_form_dict = on_page_force_stop_request_info.from_dict(on_page_force_stop_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


