# ItemsRankedSerpElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**serp_item** | [**DataAppAppStoreSearchOrganicSerpElementItem**](DataAppAppStoreSearchOrganicSerpElementItem.md) |  | [optional] 
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional] 
**se_results_count** | **str** | number of search results for the returned keyword | [optional] 
**last_updated_time** | **str** | date and time when SERP data was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**previous_updated_time** | **str** | previous to the most recent date and time when SERP data was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-10-15 12:57:46 +00:00; in this case, will equal null | [optional] 

## Example

```python
from dataforseo_client.models.items_ranked_serp_element import ItemsRankedSerpElement

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsRankedSerpElement from a JSON string
items_ranked_serp_element_instance = ItemsRankedSerpElement.from_json(json)
# print the JSON string representation of the object
print ItemsRankedSerpElement.to_json()

# convert the object into a dict
items_ranked_serp_element_dict = items_ranked_serp_element_instance.to_dict()
# create an instance of ItemsRankedSerpElement from a dict
items_ranked_serp_element_form_dict = items_ranked_serp_element.from_dict(items_ranked_serp_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


