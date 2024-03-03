# AppRankedSerpElementInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**serp_item** | [**BaseAppDataSerpElementItem**](BaseAppDataSerpElementItem.md) |  | [optional] 
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional] 
**se_results_count** | **str** | number of search results for the returned keyword | [optional] 
**last_updated_time** | **str** | date and time when SERP data was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**previous_updated_time** | **str** | previous to the most recent date and time when SERP data was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-10-15 12:57:46 +00:00; in this case, will equal null | [optional] 

## Example

```python
from dataforseo_client.models.app_ranked_serp_element_info import AppRankedSerpElementInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppRankedSerpElementInfo from a JSON string
app_ranked_serp_element_info_instance = AppRankedSerpElementInfo.from_json(json)
# print the JSON string representation of the object
print AppRankedSerpElementInfo.to_json()

# convert the object into a dict
app_ranked_serp_element_info_dict = app_ranked_serp_element_info_instance.to_dict()
# create an instance of AppRankedSerpElementInfo from a dict
app_ranked_serp_element_info_form_dict = app_ranked_serp_element_info.from_dict(app_ranked_serp_element_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


