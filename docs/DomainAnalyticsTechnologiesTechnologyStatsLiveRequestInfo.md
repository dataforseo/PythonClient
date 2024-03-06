[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DomainAnalyticsTechnologiesTechnologyStatsLiveRequestInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**technology** | **str** | target technology required field you can find the full list of technologies you can specify here on this page example: \&quot;Salesforce\&quot; | [optional]
**date_from** | **str** | starting date of the time range optional field minimum value 2022-10-31 if you don’t specify this field, the minimum value will be used by default date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2023-06-01\&quot; | [optional]
**date_to** | **str** | ending date of the time range optional field if you don’t specify this field, the today’s date will be used by default date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2023-01-15\&quot; | [optional]
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional]

## Example

```python
from dataforseo_client.models.domain_analytics_technologies_technology_stats_live_request_info import DomainAnalyticsTechnologiesTechnologyStatsLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsTechnologiesTechnologyStatsLiveRequestInfo from a JSON string
domain_analytics_technologies_technology_stats_live_request_info_instance = DomainAnalyticsTechnologiesTechnologyStatsLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print DomainAnalyticsTechnologiesTechnologyStatsLiveRequestInfo.to_json()

# convert the object into a dict
domain_analytics_technologies_technology_stats_live_request_info_dict = domain_analytics_technologies_technology_stats_live_request_info_instance.to_dict()
# create an instance of DomainAnalyticsTechnologiesTechnologyStatsLiveRequestInfo from a dict
domain_analytics_technologies_technology_stats_live_request_info_form_dict = domain_analytics_technologies_technology_stats_live_request_info.from_dict(domain_analytics_technologies_technology_stats_live_request_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")