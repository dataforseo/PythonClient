[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksCompetitorsLiveResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | total number of relevant items in the database | [optional]
**items_count** | **int** | number of items in the items array | [optional]
**items** | [**List[BacklinksCompetitorsLiveItem]**](BacklinksCompetitorsLiveItem.md) | items array | [optional]

## Example

```python
from dataforseo_client.models.backlinks_competitors_live_result_info import BacklinksCompetitorsLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksCompetitorsLiveResultInfo from a JSON string
backlinks_competitors_live_result_info_instance = BacklinksCompetitorsLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksCompetitorsLiveResultInfo.to_json()

# convert the object into a dict
backlinks_competitors_live_result_info_dict = backlinks_competitors_live_result_info_instance.to_dict()
# create an instance of BacklinksCompetitorsLiveResultInfo from a dict
backlinks_competitors_live_result_info_form_dict = backlinks_competitors_live_result_info.from_dict(backlinks_competitors_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")