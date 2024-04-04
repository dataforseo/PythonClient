# SocialMetricsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**like_count** | **int** | likes count | [optional] 

## Example

```python
from dataforseo_client.models.social_metrics_info import SocialMetricsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SocialMetricsInfo from a JSON string
social_metrics_info_instance = SocialMetricsInfo.from_json(json)
# print the JSON string representation of the object
print SocialMetricsInfo.to_json()

# convert the object into a dict
social_metrics_info_dict = social_metrics_info_instance.to_dict()
# create an instance of SocialMetricsInfo from a dict
social_metrics_info_form_dict = social_metrics_info.from_dict(social_metrics_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


