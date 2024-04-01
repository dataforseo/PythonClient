# TrendsMapDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_id** | **str** | Google Trends location identifier you can use this field for matching obtained results with location parameters specified in the request example: US-NY | [optional] 
**geo_name** | **str** | Google Trends location name you can use this field for matching obtained results with location parameters specified in the request | [optional] 
**values** | **List[Optional[object]]** | relative keyword popularity rate in a given location represents the location-specific keyword popularity rate over the given time range if you specify more than one keyword, the values will be averaged to the highest value across all specified keywords a value of 100 is the peak popularity for the term a value of 50 means that the term is half as popular a value of 0 means there was not enough data for this term | [optional] 
**max_value_index** | **int** | max value among comparable terms represents the maximum value if you specified more than two keywords in a POST array if you specified only one keyword, the value will be null | [optional] 

## Example

```python
from dataforseo_client.models.trends_map_data_info import TrendsMapDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TrendsMapDataInfo from a JSON string
trends_map_data_info_instance = TrendsMapDataInfo.from_json(json)
# print the JSON string representation of the object
print(TrendsMapDataInfo.to_json())

# convert the object into a dict
trends_map_data_info_dict = trends_map_data_info_instance.to_dict()
# create an instance of TrendsMapDataInfo from a dict
trends_map_data_info_form_dict = trends_map_data_info.from_dict(trends_map_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


