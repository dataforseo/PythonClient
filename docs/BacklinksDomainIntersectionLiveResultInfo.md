# BacklinksDomainIntersectionLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targets** | **Dict[str, Optional[str]]** | target domains, subdomains or webpages in a POST array | [optional] 
**total_count** | **int** | total amount of results relevant to your request | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[BacklinksDomainIntersectionLiveItem]**](BacklinksDomainIntersectionLiveItem.md) | contains domain that link to all targets from the POST array | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_domain_intersection_live_result_info import BacklinksDomainIntersectionLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksDomainIntersectionLiveResultInfo from a JSON string
backlinks_domain_intersection_live_result_info_instance = BacklinksDomainIntersectionLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(BacklinksDomainIntersectionLiveResultInfo.to_json())

# convert the object into a dict
backlinks_domain_intersection_live_result_info_dict = backlinks_domain_intersection_live_result_info_instance.to_dict()
# create an instance of BacklinksDomainIntersectionLiveResultInfo from a dict
backlinks_domain_intersection_live_result_info_form_dict = backlinks_domain_intersection_live_result_info.from_dict(backlinks_domain_intersection_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


