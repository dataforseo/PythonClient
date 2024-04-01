# DataforseoTrendsDemographyElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | the alignment of the element can take the following values: 1, 2, 3, 4, etc. | [optional] 
**keywords** | **List[Optional[str]]** | relevant keywords the data included in the interests and interests_comparison is based on the keywords listed in this array | [optional] 
**demography** | [**Demography**](Demography.md) |  | [optional] 
**demography_comparison** | **object** | comparison of demographic data on keyword popularity for the specified parameters conains keyword popularity data by age and gender if you specified a single keyword, the value will be null | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_trends_demography_element_item import DataforseoTrendsDemographyElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoTrendsDemographyElementItem from a JSON string
dataforseo_trends_demography_element_item_instance = DataforseoTrendsDemographyElementItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoTrendsDemographyElementItem.to_json())

# convert the object into a dict
dataforseo_trends_demography_element_item_dict = dataforseo_trends_demography_element_item_instance.to_dict()
# create an instance of DataforseoTrendsDemographyElementItem from a dict
dataforseo_trends_demography_element_item_form_dict = dataforseo_trends_demography_element_item.from_dict(dataforseo_trends_demography_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


