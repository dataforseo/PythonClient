# DataforseoLabsGoogleDomainWhoisOverviewLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**total_count** | **int** | total amount of results in our database relevant to your request | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[DataforseoLabsGoogleDomainWhoisOverviewLiveItem]**](DataforseoLabsGoogleDomainWhoisOverviewLiveItem.md) | contains ranking and traffic data | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_domain_whois_overview_live_result_info import DataforseoLabsGoogleDomainWhoisOverviewLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleDomainWhoisOverviewLiveResultInfo from a JSON string
dataforseo_labs_google_domain_whois_overview_live_result_info_instance = DataforseoLabsGoogleDomainWhoisOverviewLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleDomainWhoisOverviewLiveResultInfo.to_json())

# convert the object into a dict
dataforseo_labs_google_domain_whois_overview_live_result_info_dict = dataforseo_labs_google_domain_whois_overview_live_result_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleDomainWhoisOverviewLiveResultInfo from a dict
dataforseo_labs_google_domain_whois_overview_live_result_info_from_dict = DataforseoLabsGoogleDomainWhoisOverviewLiveResultInfo.from_dict(dataforseo_labs_google_domain_whois_overview_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


