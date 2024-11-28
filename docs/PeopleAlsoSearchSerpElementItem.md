# PeopleAlsoSearchSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the row | [optional] 
**items** | **List[Optional[str]]** | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.people_also_search_serp_element_item import PeopleAlsoSearchSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleAlsoSearchSerpElementItem from a JSON string
people_also_search_serp_element_item_instance = PeopleAlsoSearchSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(PeopleAlsoSearchSerpElementItem.to_json())

# convert the object into a dict
people_also_search_serp_element_item_dict = people_also_search_serp_element_item_instance.to_dict()
# create an instance of PeopleAlsoSearchSerpElementItem from a dict
people_also_search_serp_element_item_from_dict = PeopleAlsoSearchSerpElementItem.from_dict(people_also_search_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


