# CommercialUnitsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the row | [optional] 
**items** | [**List[CommercialUnitsElement]**](CommercialUnitsElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.commercial_units_serp_element_item import CommercialUnitsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of CommercialUnitsSerpElementItem from a JSON string
commercial_units_serp_element_item_instance = CommercialUnitsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(CommercialUnitsSerpElementItem.to_json())

# convert the object into a dict
commercial_units_serp_element_item_dict = commercial_units_serp_element_item_instance.to_dict()
# create an instance of CommercialUnitsSerpElementItem from a dict
commercial_units_serp_element_item_from_dict = CommercialUnitsSerpElementItem.from_dict(commercial_units_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


