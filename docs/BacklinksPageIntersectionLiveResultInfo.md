# BacklinksPageIntersectionLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targets** | **Dict[str, Optional[str]]** | targets from a POST array | [optional] 
**total_count** | **int** | total amount of results relevant the request | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[BacklinksPageIntersectionLiveItem]**](BacklinksPageIntersectionLiveItem.md) | contains relevant backlinks and referring domains data | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_page_intersection_live_result_info import BacklinksPageIntersectionLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksPageIntersectionLiveResultInfo from a JSON string
backlinks_page_intersection_live_result_info_instance = BacklinksPageIntersectionLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksPageIntersectionLiveResultInfo.to_json()

# convert the object into a dict
backlinks_page_intersection_live_result_info_dict = backlinks_page_intersection_live_result_info_instance.to_dict()
# create an instance of BacklinksPageIntersectionLiveResultInfo from a dict
backlinks_page_intersection_live_result_info_form_dict = backlinks_page_intersection_live_result_info.from_dict(backlinks_page_intersection_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


