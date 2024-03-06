[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksDomainIntersectionLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_intersection** | [**Dict[str, BacklinksDomainIntersectionInfo]**](BacklinksDomainIntersectionInfo.md) | contains data on domains that link to the corresponding targets specified in the POST array data is provided in separate objects corresponding to domains, subdomains or pages specified in the targets object | [optional]
**summary** | [**Summary**](Summary.md) |  | [optional]

## Example

```python
from dataforseo_client.models.backlinks_domain_intersection_live_item import BacklinksDomainIntersectionLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksDomainIntersectionLiveItem from a JSON string
backlinks_domain_intersection_live_item_instance = BacklinksDomainIntersectionLiveItem.from_json(json)
# print the JSON string representation of the object
print BacklinksDomainIntersectionLiveItem.to_json()

# convert the object into a dict
backlinks_domain_intersection_live_item_dict = backlinks_domain_intersection_live_item_instance.to_dict()
# create an instance of BacklinksDomainIntersectionLiveItem from a dict
backlinks_domain_intersection_live_item_form_dict = backlinks_domain_intersection_live_item.from_dict(backlinks_domain_intersection_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")