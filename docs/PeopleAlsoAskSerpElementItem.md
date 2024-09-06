# PeopleAlsoAskSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PeopleAlsoAskElement]**](PeopleAlsoAskElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.people_also_ask_serp_element_item import PeopleAlsoAskSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleAlsoAskSerpElementItem from a JSON string
people_also_ask_serp_element_item_instance = PeopleAlsoAskSerpElementItem.from_json(json)
# print the JSON string representation of the object
print PeopleAlsoAskSerpElementItem.to_json()

# convert the object into a dict
people_also_ask_serp_element_item_dict = people_also_ask_serp_element_item_instance.to_dict()
# create an instance of PeopleAlsoAskSerpElementItem from a dict
people_also_ask_serp_element_item_form_dict = people_also_ask_serp_element_item.from_dict(people_also_ask_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


