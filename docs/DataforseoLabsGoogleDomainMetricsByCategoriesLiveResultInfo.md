[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DataforseoLabsGoogleDomainMetricsByCategoriesLiveResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional]
**categories** | **List[int]** | categories in a POST array | [optional]
**location_code** | **int** | location code in a POST array | [optional]
**language_code** | **str** | language code in a POST array | [optional]
**total_count** | **int** | total amount of results in our database relevant to your request | [optional]
**items_count** | **int** | the number of results returned in the items array | [optional]
**items** | [**List[DataforseoLabsGoogleDomainMetricsByCategoriesLiveItem]**](DataforseoLabsGoogleDomainMetricsByCategoriesLiveItem.md) | contains historical ranking and traffic data | [optional]

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_domain_metrics_by_categories_live_result_info import DataforseoLabsGoogleDomainMetricsByCategoriesLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleDomainMetricsByCategoriesLiveResultInfo from a JSON string
dataforseo_labs_google_domain_metrics_by_categories_live_result_info_instance = DataforseoLabsGoogleDomainMetricsByCategoriesLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleDomainMetricsByCategoriesLiveResultInfo.to_json()

# convert the object into a dict
dataforseo_labs_google_domain_metrics_by_categories_live_result_info_dict = dataforseo_labs_google_domain_metrics_by_categories_live_result_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleDomainMetricsByCategoriesLiveResultInfo from a dict
dataforseo_labs_google_domain_metrics_by_categories_live_result_info_form_dict = dataforseo_labs_google_domain_metrics_by_categories_live_result_info.from_dict(dataforseo_labs_google_domain_metrics_by_categories_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")