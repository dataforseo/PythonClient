# DataforseoTrendsDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | relevant keyword for which demographic data is provided | [optional] 
**values** | [**List[DemographyItemValueInfo]**](DemographyItemValueInfo.md) | contains age range and corresponding keyword popularity values | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_trends_data_info import DataforseoTrendsDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoTrendsDataInfo from a JSON string
dataforseo_trends_data_info_instance = DataforseoTrendsDataInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoTrendsDataInfo.to_json()

# convert the object into a dict
dataforseo_trends_data_info_dict = dataforseo_trends_data_info_instance.to_dict()
# create an instance of DataforseoTrendsDataInfo from a dict
dataforseo_trends_data_info_form_dict = dataforseo_trends_data_info.from_dict(dataforseo_trends_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


