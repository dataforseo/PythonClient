# Demography


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | [**List[DataforseoTrendsDataInfo]**](DataforseoTrendsDataInfo.md) | distribution of keyword popularity by age | [optional] 
**gender** | [**List[DataforseoTrendsDataInfo]**](DataforseoTrendsDataInfo.md) | distribution of keyword popularity by gender | [optional] 

## Example

```python
from dataforseo_client.models.demography import Demography

# TODO update the JSON string below
json = "{}"
# create an instance of Demography from a JSON string
demography_instance = Demography.from_json(json)
# print the JSON string representation of the object
print(Demography.to_json())

# convert the object into a dict
demography_dict = demography_instance.to_dict()
# create an instance of Demography from a dict
demography_from_dict = Demography.from_dict(demography_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


