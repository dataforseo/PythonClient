# DemographyComparison


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **Dict[str, Optional[List[Optional[int]]]]** | comparison of keyword popularity data by age | [optional] 
**gender** | **Dict[str, Optional[List[Optional[int]]]]** | comparison of keyword popularity data by gender | [optional] 

## Example

```python
from dataforseo_client.models.demography_comparison import DemographyComparison

# TODO update the JSON string below
json = "{}"
# create an instance of DemographyComparison from a JSON string
demography_comparison_instance = DemographyComparison.from_json(json)
# print the JSON string representation of the object
print DemographyComparison.to_json()

# convert the object into a dict
demography_comparison_dict = demography_comparison_instance.to_dict()
# create an instance of DemographyComparison from a dict
demography_comparison_form_dict = demography_comparison.from_dict(demography_comparison_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


