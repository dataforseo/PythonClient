# PeopleAlsoSearchDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**title** | **str** | title of the result in SERP | [optional] 
**items** | **List[Optional[str]]** | additional items present in the element if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.people_also_search_dataforseo_labs_serp_element_item import PeopleAlsoSearchDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleAlsoSearchDataforseoLabsSerpElementItem from a JSON string
people_also_search_dataforseo_labs_serp_element_item_instance = PeopleAlsoSearchDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(PeopleAlsoSearchDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
people_also_search_dataforseo_labs_serp_element_item_dict = people_also_search_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of PeopleAlsoSearchDataforseoLabsSerpElementItem from a dict
people_also_search_dataforseo_labs_serp_element_item_from_dict = PeopleAlsoSearchDataforseoLabsSerpElementItem.from_dict(people_also_search_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


