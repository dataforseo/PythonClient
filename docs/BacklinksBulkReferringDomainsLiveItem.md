# BacklinksBulkReferringDomainsLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain, subdomain or webpage from a POST array | [optional] 
**referring_domains** | **int** | number of referring domains pointing to the target note that we calculate main domains (root domains, like example.com) and their subdomains (e.g. blog.example.com) separately for this metric | [optional] 
**referring_domains_nofollow** | **int** | number of domains pointing at least one nofollow link to the target | [optional] 
**referring_main_domains** | **int** | number of referring main domains pointing to the target the number of primary (root) domains referring to your target | [optional] 
**referring_main_domains_nofollow** | **int** | number of main domains pointing at least one nofollow link to the target | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_bulk_referring_domains_live_item import BacklinksBulkReferringDomainsLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBulkReferringDomainsLiveItem from a JSON string
backlinks_bulk_referring_domains_live_item_instance = BacklinksBulkReferringDomainsLiveItem.from_json(json)
# print the JSON string representation of the object
print(BacklinksBulkReferringDomainsLiveItem.to_json())

# convert the object into a dict
backlinks_bulk_referring_domains_live_item_dict = backlinks_bulk_referring_domains_live_item_instance.to_dict()
# create an instance of BacklinksBulkReferringDomainsLiveItem from a dict
backlinks_bulk_referring_domains_live_item_from_dict = BacklinksBulkReferringDomainsLiveItem.from_dict(backlinks_bulk_referring_domains_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


