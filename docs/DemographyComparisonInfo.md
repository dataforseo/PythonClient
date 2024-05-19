# DemographyComparisonInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **Dict[str, Optional[List[Optional[int]]]]** | type of element | [optional] 
**gender** | **Dict[str, Optional[List[Optional[int]]]]** | type of element | [optional] 

## Example

```python
from dataforseo_client.models.demography_comparison_info import DemographyComparisonInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DemographyComparisonInfo from a JSON string
demography_comparison_info_instance = DemographyComparisonInfo.from_json(json)
# print the JSON string representation of the object
print DemographyComparisonInfo.to_json()

# convert the object into a dict
demography_comparison_info_dict = demography_comparison_info_instance.to_dict()
# create an instance of DemographyComparisonInfo from a dict
demography_comparison_info_form_dict = demography_comparison_info.from_dict(demography_comparison_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


