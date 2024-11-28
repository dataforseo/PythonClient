# DataforseoTrendsDemographyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | the alignment of the element can take the following values: 1, 2, 3, 4, etc. | [optional] 
**type** | **str** | type of element | [optional] 
**keywords** | **List[Optional[str]]** | relevant keywords the data included in the demography and demography_comparison is based on the keywords listed in this array | [optional] 
**demography** | [**Demography**](Demography.md) |  | [optional] 
**demography_comparison** | [**DemographyComparisonInfo**](DemographyComparisonInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_trends_demography_info import DataforseoTrendsDemographyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoTrendsDemographyInfo from a JSON string
dataforseo_trends_demography_info_instance = DataforseoTrendsDemographyInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoTrendsDemographyInfo.to_json())

# convert the object into a dict
dataforseo_trends_demography_info_dict = dataforseo_trends_demography_info_instance.to_dict()
# create an instance of DataforseoTrendsDemographyInfo from a dict
dataforseo_trends_demography_info_from_dict = DataforseoTrendsDemographyInfo.from_dict(dataforseo_trends_demography_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


