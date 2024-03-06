[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksBulkNewLostReferringDomainsLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain, subdomain or webpage from a POST array | [optional]
**new_referring_domains** | **int** | number of new referring domains number of new referring domains pointing to the target | [optional]
**lost_referring_domains** | **int** | number of lost referring domains number of lost referring domains of the target | [optional]
**new_referring_main_domains** | **int** | number of new referring main domains pointing to the target | [optional]
**lost_referring_main_domains** | **int** | number of lost referring main domains pointing to the target | [optional]

## Example

```python
from dataforseo_client.models.backlinks_bulk_new_lost_referring_domains_live_item import BacklinksBulkNewLostReferringDomainsLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBulkNewLostReferringDomainsLiveItem from a JSON string
backlinks_bulk_new_lost_referring_domains_live_item_instance = BacklinksBulkNewLostReferringDomainsLiveItem.from_json(json)
# print the JSON string representation of the object
print BacklinksBulkNewLostReferringDomainsLiveItem.to_json()

# convert the object into a dict
backlinks_bulk_new_lost_referring_domains_live_item_dict = backlinks_bulk_new_lost_referring_domains_live_item_instance.to_dict()
# create an instance of BacklinksBulkNewLostReferringDomainsLiveItem from a dict
backlinks_bulk_new_lost_referring_domains_live_item_form_dict = backlinks_bulk_new_lost_referring_domains_live_item.from_dict(backlinks_bulk_new_lost_referring_domains_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")