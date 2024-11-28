# CommercialUnitsElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**url** | **str** | URL | [optional] 
**domain** | **str** | website domain | [optional] 
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional] 
**source** | **str** | source of the element indicates the source of information included in the top_stories_element | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.commercial_units_element import CommercialUnitsElement

# TODO update the JSON string below
json = "{}"
# create an instance of CommercialUnitsElement from a JSON string
commercial_units_element_instance = CommercialUnitsElement.from_json(json)
# print the JSON string representation of the object
print(CommercialUnitsElement.to_json())

# convert the object into a dict
commercial_units_element_dict = commercial_units_element_instance.to_dict()
# create an instance of CommercialUnitsElement from a dict
commercial_units_element_from_dict = CommercialUnitsElement.from_dict(commercial_units_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


