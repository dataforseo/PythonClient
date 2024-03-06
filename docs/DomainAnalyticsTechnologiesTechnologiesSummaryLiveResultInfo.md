[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DomainAnalyticsTechnologiesTechnologiesSummaryLiveResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | **Dict[str, Optional[int]]** | distribution of websites by country contains country codes and number of websites per country | [optional]
**languages** | **Dict[str, Optional[int]]** | distribution of websites by language contains language codes and number of websites per language | [optional]
**content_languages** | **Dict[str, Optional[int]]** | distribution of websites by content language contains content language codes and number of websites per language | [optional]
**keywords** | **Dict[str, Optional[int]]** | distribution of websites by keywords contains keywords found in the websites’ titles, descriptions or meta keywords, and number of websites using each keyword | [optional]

## Example

```python
from dataforseo_client.models.domain_analytics_technologies_technologies_summary_live_result_info import DomainAnalyticsTechnologiesTechnologiesSummaryLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsTechnologiesTechnologiesSummaryLiveResultInfo from a JSON string
domain_analytics_technologies_technologies_summary_live_result_info_instance = DomainAnalyticsTechnologiesTechnologiesSummaryLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print DomainAnalyticsTechnologiesTechnologiesSummaryLiveResultInfo.to_json()

# convert the object into a dict
domain_analytics_technologies_technologies_summary_live_result_info_dict = domain_analytics_technologies_technologies_summary_live_result_info_instance.to_dict()
# create an instance of DomainAnalyticsTechnologiesTechnologiesSummaryLiveResultInfo from a dict
domain_analytics_technologies_technologies_summary_live_result_info_form_dict = domain_analytics_technologies_technologies_summary_live_result_info.from_dict(domain_analytics_technologies_technologies_summary_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")