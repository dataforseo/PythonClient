# BacklinksDomainPagesSummaryLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | target in the post array | [optional] 
**total_count** | **int** | total number of relevant items in the database | [optional] 
**items_count** | **int** | number of items in the results array | [optional] 
**items** | [**List[BacklinksDomainPagesSummaryLiveItem]**](BacklinksDomainPagesSummaryLiveItem.md) | items array | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_domain_pages_summary_live_result_info import BacklinksDomainPagesSummaryLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksDomainPagesSummaryLiveResultInfo from a JSON string
backlinks_domain_pages_summary_live_result_info_instance = BacklinksDomainPagesSummaryLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(BacklinksDomainPagesSummaryLiveResultInfo.to_json())

# convert the object into a dict
backlinks_domain_pages_summary_live_result_info_dict = backlinks_domain_pages_summary_live_result_info_instance.to_dict()
# create an instance of BacklinksDomainPagesSummaryLiveResultInfo from a dict
backlinks_domain_pages_summary_live_result_info_from_dict = BacklinksDomainPagesSummaryLiveResultInfo.from_dict(backlinks_domain_pages_summary_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


