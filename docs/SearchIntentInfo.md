# SearchIntentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type possible values: google | [optional] 
**main_intent** | **str** | main search intent possible values: informational, navigational, commercial, transactional | [optional] 
**foreign_intent** | **List[Optional[str]]** | supplementary search intents possible values: informational, navigational, commercial, transactional | [optional] 
**last_updated_time** | **str** | date and time when backlink data was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 

## Example

```python
from dataforseo_client.models.search_intent_info import SearchIntentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SearchIntentInfo from a JSON string
search_intent_info_instance = SearchIntentInfo.from_json(json)
# print the JSON string representation of the object
print(SearchIntentInfo.to_json())

# convert the object into a dict
search_intent_info_dict = search_intent_info_instance.to_dict()
# create an instance of SearchIntentInfo from a dict
search_intent_info_from_dict = SearchIntentInfo.from_dict(search_intent_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


