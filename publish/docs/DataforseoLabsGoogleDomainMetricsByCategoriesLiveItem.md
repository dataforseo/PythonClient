# DataforseoLabsGoogleDomainMetricsByCategoriesLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**top_categories** | **List[Optional[int]]** | categories for which domains are collected | [optional] 
**organic_etv** | **float** | current organic ETV of the domain | [optional] 
**organic_count** | **int** | current total count of organic SERPs that contain the domain | [optional] 
**organic_is_lost** | **int** | current number of lost ranked elements indicates how many ranked elements of the domain were previously presented in SERPs, but weren’t found during the last check | [optional] 
**organic_is_new** | **int** | current number of new ranked elements indicates how many new ranked elements were found for the domain | [optional] 
**domain** | **str** | domain found for the specified category | [optional] 
**main_domain** | **str** | primary domain | [optional] 
**metrics_history** | **Dict[str, Dict[str, MetricsInfo]]** | historical ranking and traffic data of the domain | [optional] 
**metrics_difference** | [**Dict[str, MetricsInfo]**](MetricsInfo.md) | metrics difference between first_date and second_date calculated by subtracting domain metrics as of the greater date from domain metrics as of the smaller date | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_domain_metrics_by_categories_live_item import DataforseoLabsGoogleDomainMetricsByCategoriesLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleDomainMetricsByCategoriesLiveItem from a JSON string
dataforseo_labs_google_domain_metrics_by_categories_live_item_instance = DataforseoLabsGoogleDomainMetricsByCategoriesLiveItem.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleDomainMetricsByCategoriesLiveItem.to_json()

# convert the object into a dict
dataforseo_labs_google_domain_metrics_by_categories_live_item_dict = dataforseo_labs_google_domain_metrics_by_categories_live_item_instance.to_dict()
# create an instance of DataforseoLabsGoogleDomainMetricsByCategoriesLiveItem from a dict
dataforseo_labs_google_domain_metrics_by_categories_live_item_form_dict = dataforseo_labs_google_domain_metrics_by_categories_live_item.from_dict(dataforseo_labs_google_domain_metrics_by_categories_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


