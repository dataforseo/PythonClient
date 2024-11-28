# DataforseoLabsAvailableFiltersResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related_keywords** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**keyword_suggestions** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**ranked_keywords** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**keyword_ideas** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**serp_competitors** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**relevant_pages** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**subdomains** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**competitors_domain** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**categories_for_domain** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**keywords_for_categories** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**domain_intersection** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**page_intersection** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**domain_whois_overview** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**top_searches** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**domain_metrics_by_categories** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**keywords_for_site** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**product_competitors** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**product_keyword_intersections** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**app_intersection** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**app_competitors** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**keywords_for_app** | **Dict[str, Optional[Dict[str, Optional[str]]]]** |  | [optional] 
**database_rows_count** | **Dict[str, Optional[str]]** |  | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_available_filters_result_info import DataforseoLabsAvailableFiltersResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsAvailableFiltersResultInfo from a JSON string
dataforseo_labs_available_filters_result_info_instance = DataforseoLabsAvailableFiltersResultInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsAvailableFiltersResultInfo.to_json())

# convert the object into a dict
dataforseo_labs_available_filters_result_info_dict = dataforseo_labs_available_filters_result_info_instance.to_dict()
# create an instance of DataforseoLabsAvailableFiltersResultInfo from a dict
dataforseo_labs_available_filters_result_info_from_dict = DataforseoLabsAvailableFiltersResultInfo.from_dict(dataforseo_labs_available_filters_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


