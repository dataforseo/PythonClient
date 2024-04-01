# AutocompleteSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**relevance** | **int** | relevance of suggested keyword represents the relevant of the autocomplete suggestion to the target keyword can take values from 500 to 2000 the higher the value, the more relevant is the suggestion Note: only available for the following client: chrome/chrome-omni | [optional] 
**suggestion** | **str** | google autocomplete keyword suggestion | [optional] 
**suggestion_type** | **str** | google autocomplete suggestion type Note: only available for the following client: chrome/chrome-omni | [optional] 
**search_query_url** | **str** | url to search results url to search results relevant to the google autocomplete suggestion | [optional] 
**highlighted** | **List[Optional[str]]** |  | [optional] 

## Example

```python
from dataforseo_client.models.autocomplete_serp_element_item import AutocompleteSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteSerpElementItem from a JSON string
autocomplete_serp_element_item_instance = AutocompleteSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(AutocompleteSerpElementItem.to_json())

# convert the object into a dict
autocomplete_serp_element_item_dict = autocomplete_serp_element_item_instance.to_dict()
# create an instance of AutocompleteSerpElementItem from a dict
autocomplete_serp_element_item_form_dict = autocomplete_serp_element_item.from_dict(autocomplete_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


