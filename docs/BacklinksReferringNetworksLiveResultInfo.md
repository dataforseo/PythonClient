[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksReferringNetworksLiveResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | target in a POST array | [optional]
**total_count** | **int** | total number of relevant items in the database | [optional]
**items_count** | **int** | number of items in the items array | [optional]
**items** | [**List[BacklinksReferringNetworksLiveItem]**](BacklinksReferringNetworksLiveItem.md) | items array | [optional]

## Example

```python
from dataforseo_client.models.backlinks_referring_networks_live_result_info import BacklinksReferringNetworksLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksReferringNetworksLiveResultInfo from a JSON string
backlinks_referring_networks_live_result_info_instance = BacklinksReferringNetworksLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksReferringNetworksLiveResultInfo.to_json()

# convert the object into a dict
backlinks_referring_networks_live_result_info_dict = backlinks_referring_networks_live_result_info_instance.to_dict()
# create an instance of BacklinksReferringNetworksLiveResultInfo from a dict
backlinks_referring_networks_live_result_info_form_dict = backlinks_referring_networks_live_result_info.from_dict(backlinks_referring_networks_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")