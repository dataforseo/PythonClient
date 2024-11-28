# CommercialUnitsDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**items** | [**List[CommercialUnitsElement]**](CommercialUnitsElement.md) | elements of search results found in SERP | [optional] 

## Example

```python
from dataforseo_client.models.commercial_units_dataforseo_labs_serp_element_item import CommercialUnitsDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of CommercialUnitsDataforseoLabsSerpElementItem from a JSON string
commercial_units_dataforseo_labs_serp_element_item_instance = CommercialUnitsDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(CommercialUnitsDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
commercial_units_dataforseo_labs_serp_element_item_dict = commercial_units_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of CommercialUnitsDataforseoLabsSerpElementItem from a dict
commercial_units_dataforseo_labs_serp_element_item_from_dict = CommercialUnitsDataforseoLabsSerpElementItem.from_dict(commercial_units_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


