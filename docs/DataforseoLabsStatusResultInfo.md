# DataforseoLabsStatusResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google** | [**DataforseoLabsStatusInfo**](DataforseoLabsStatusInfo.md) |  | [optional] 
**bing** | [**DataforseoLabsStatusInfo**](DataforseoLabsStatusInfo.md) |  | [optional] 
**amazon** | [**DataforseoLabsStatusInfo**](DataforseoLabsStatusInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_status_result_info import DataforseoLabsStatusResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsStatusResultInfo from a JSON string
dataforseo_labs_status_result_info_instance = DataforseoLabsStatusResultInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsStatusResultInfo.to_json())

# convert the object into a dict
dataforseo_labs_status_result_info_dict = dataforseo_labs_status_result_info_instance.to_dict()
# create an instance of DataforseoLabsStatusResultInfo from a dict
dataforseo_labs_status_result_info_form_dict = dataforseo_labs_status_result_info.from_dict(dataforseo_labs_status_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


