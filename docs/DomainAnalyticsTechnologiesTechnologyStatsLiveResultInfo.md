[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DomainAnalyticsTechnologiesTechnologyStatsLiveResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**technology** | **str** | target technology | [optional]
**date_from** | **str** | starting date of the time range | [optional]
**date_to** | **str** | ending date of the time range | [optional]
**items_count** | **int** | number of items in the results array | [optional]
**items** | [**List[DomainAnalyticsTechnologiesTechnologyStatsLiveItem]**](DomainAnalyticsTechnologiesTechnologyStatsLiveItem.md) | items array | [optional]

## Example

```python
from dataforseo_client.models.domain_analytics_technologies_technology_stats_live_result_info import DomainAnalyticsTechnologiesTechnologyStatsLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsTechnologiesTechnologyStatsLiveResultInfo from a JSON string
domain_analytics_technologies_technology_stats_live_result_info_instance = DomainAnalyticsTechnologiesTechnologyStatsLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print DomainAnalyticsTechnologiesTechnologyStatsLiveResultInfo.to_json()

# convert the object into a dict
domain_analytics_technologies_technology_stats_live_result_info_dict = domain_analytics_technologies_technology_stats_live_result_info_instance.to_dict()
# create an instance of DomainAnalyticsTechnologiesTechnologyStatsLiveResultInfo from a dict
domain_analytics_technologies_technology_stats_live_result_info_form_dict = domain_analytics_technologies_technology_stats_live_result_info.from_dict(domain_analytics_technologies_technology_stats_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")