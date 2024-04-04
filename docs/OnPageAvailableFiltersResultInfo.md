# OnPageAvailableFiltersResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | **Dict[str, Optional[str]]** |  | [optional] 
**pages** | **Dict[str, Optional[str]]** |  | [optional] 
**non_indexable** | **Dict[str, Optional[str]]** |  | [optional] 
**links** | **Dict[str, Optional[str]]** |  | [optional] 
**pages_by_resource** | **Dict[str, Optional[str]]** |  | [optional] 
**redirect_chains** | **Dict[str, Optional[str]]** |  | [optional] 
**keyword_density** | **Dict[str, Optional[str]]** |  | [optional] 

## Example

```python
from dataforseo_client.models.on_page_available_filters_result_info import OnPageAvailableFiltersResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageAvailableFiltersResultInfo from a JSON string
on_page_available_filters_result_info_instance = OnPageAvailableFiltersResultInfo.from_json(json)
# print the JSON string representation of the object
print OnPageAvailableFiltersResultInfo.to_json()

# convert the object into a dict
on_page_available_filters_result_info_dict = on_page_available_filters_result_info_instance.to_dict()
# create an instance of OnPageAvailableFiltersResultInfo from a dict
on_page_available_filters_result_info_form_dict = on_page_available_filters_result_info.from_dict(on_page_available_filters_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


