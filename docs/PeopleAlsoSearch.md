# PeopleAlsoSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cid** | **str** | google-defined client id unique id of a local establishment learn more about the identifier in this help center article | [optional] 
**feature_id** | **str** | the unique identifier of the element in SERP learn more about the identifier in this help center article | [optional] 
**title** | **str** | title of the element in SERP the name of the business entity for which the results are collected | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.people_also_search import PeopleAlsoSearch

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleAlsoSearch from a JSON string
people_also_search_instance = PeopleAlsoSearch.from_json(json)
# print the JSON string representation of the object
print PeopleAlsoSearch.to_json()

# convert the object into a dict
people_also_search_dict = people_also_search_instance.to_dict()
# create an instance of PeopleAlsoSearch from a dict
people_also_search_form_dict = people_also_search.from_dict(people_also_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


