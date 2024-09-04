# SerpGoogleAutocompleteeAdvancedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**relevance** | **int** | relevance of suggested keyword represents the relevant of the autocomplete suggestion to the target keyword can take values from 500 to 2000 the higher the value, the more relevant is the suggestion Note: only available for the following client: chrome/chrome-omni | [optional] 
**suggestion** | **str** | google autocomplete keyword suggestion | [optional] 
**suggestion_type** | **str** | google autocomplete suggestion type Note: only available for the following client: chrome/chrome-omni | [optional] 
**search_query_url** | **str** | url to search results url to search results relevant to the google autocomplete suggestion | [optional] 
**thumbnail_url** | **str** | url of the thumbnail image url of the thumbnail image of the google autocomplete suggestion Note: only available for the following client: gws-wiz gws-wiz-serp | [optional] 
**highlighted** | **List[Optional[str]]** | keywords highlighted in autocomplete contains a list of google autocomplete suggestions that are highlighted in the search bar; Note: array is only available for the following client: gws-wiz psy-ab gws-wiz-local | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_autocompletee_advanced_item import SerpGoogleAutocompleteeAdvancedItem

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleAutocompleteeAdvancedItem from a JSON string
serp_google_autocompletee_advanced_item_instance = SerpGoogleAutocompleteeAdvancedItem.from_json(json)
# print the JSON string representation of the object
print SerpGoogleAutocompleteeAdvancedItem.to_json()

# convert the object into a dict
serp_google_autocompletee_advanced_item_dict = serp_google_autocompletee_advanced_item_instance.to_dict()
# create an instance of SerpGoogleAutocompleteeAdvancedItem from a dict
serp_google_autocompletee_advanced_item_form_dict = serp_google_autocompletee_advanced_item.from_dict(serp_google_autocompletee_advanced_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


