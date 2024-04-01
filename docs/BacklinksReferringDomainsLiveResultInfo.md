# BacklinksReferringDomainsLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | target in a POST array | [optional] 
**total_count** | **int** | total number of relevant items in the database total number of main domains referring to your target; example.com and blog.example.com are counted as one referring domain | [optional] 
**items_count** | **int** | number of items in the items array | [optional] 
**items** | [**List[BacklinksReferringDomainsLiveItem]**](BacklinksReferringDomainsLiveItem.md) | items array | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_referring_domains_live_result_info import BacklinksReferringDomainsLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksReferringDomainsLiveResultInfo from a JSON string
backlinks_referring_domains_live_result_info_instance = BacklinksReferringDomainsLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(BacklinksReferringDomainsLiveResultInfo.to_json())

# convert the object into a dict
backlinks_referring_domains_live_result_info_dict = backlinks_referring_domains_live_result_info_instance.to_dict()
# create an instance of BacklinksReferringDomainsLiveResultInfo from a dict
backlinks_referring_domains_live_result_info_form_dict = backlinks_referring_domains_live_result_info.from_dict(backlinks_referring_domains_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


