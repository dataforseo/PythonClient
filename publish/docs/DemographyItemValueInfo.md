# DemographyItemValueInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**value** | **int** | keyword popularity rate within the specified age range using this value you can understand how popular a keyword is within each age range; calculation: we determine the highest popularity value for the relevant keyword across all age groups, and then express all other values as a percentage of that highest value (100); a value of 100 is the highest popularity for the term a value of 0 means there was not enough data for this term | [optional] 

## Example

```python
from dataforseo_client.models.demography_item_value_info import DemographyItemValueInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DemographyItemValueInfo from a JSON string
demography_item_value_info_instance = DemographyItemValueInfo.from_json(json)
# print the JSON string representation of the object
print DemographyItemValueInfo.to_json()

# convert the object into a dict
demography_item_value_info_dict = demography_item_value_info_instance.to_dict()
# create an instance of DemographyItemValueInfo from a dict
demography_item_value_info_form_dict = demography_item_value_info.from_dict(demography_item_value_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


