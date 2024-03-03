# BacklinksAnchorsLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | target in the post array | [optional] 
**total_count** | **int** | total number of relevant items in the database | [optional] 
**items_count** | **int** | number of items in the results array | [optional] 
**items** | [**List[BacklinksAnchorsLiveItem]**](BacklinksAnchorsLiveItem.md) | items array | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_anchors_live_result_info import BacklinksAnchorsLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksAnchorsLiveResultInfo from a JSON string
backlinks_anchors_live_result_info_instance = BacklinksAnchorsLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksAnchorsLiveResultInfo.to_json()

# convert the object into a dict
backlinks_anchors_live_result_info_dict = backlinks_anchors_live_result_info_instance.to_dict()
# create an instance of BacklinksAnchorsLiveResultInfo from a dict
backlinks_anchors_live_result_info_form_dict = backlinks_anchors_live_result_info.from_dict(backlinks_anchors_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


