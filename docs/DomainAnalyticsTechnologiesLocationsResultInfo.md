# DomainAnalyticsTechnologiesLocationsResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_name** | **str** | full name of the location | [optional] 
**country_iso_code** | **str** | ISO country code of the location | [optional] 

## Example

```python
from dataforseo_client.models.domain_analytics_technologies_locations_result_info import DomainAnalyticsTechnologiesLocationsResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsTechnologiesLocationsResultInfo from a JSON string
domain_analytics_technologies_locations_result_info_instance = DomainAnalyticsTechnologiesLocationsResultInfo.from_json(json)
# print the JSON string representation of the object
print(DomainAnalyticsTechnologiesLocationsResultInfo.to_json())

# convert the object into a dict
domain_analytics_technologies_locations_result_info_dict = domain_analytics_technologies_locations_result_info_instance.to_dict()
# create an instance of DomainAnalyticsTechnologiesLocationsResultInfo from a dict
domain_analytics_technologies_locations_result_info_from_dict = DomainAnalyticsTechnologiesLocationsResultInfo.from_dict(domain_analytics_technologies_locations_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


