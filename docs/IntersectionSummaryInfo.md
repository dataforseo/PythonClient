# IntersectionSummaryInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intersections_count** | **int** | total number of intersections | [optional] 

## Example

```python
from dataforseo_client.models.intersection_summary_info import IntersectionSummaryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of IntersectionSummaryInfo from a JSON string
intersection_summary_info_instance = IntersectionSummaryInfo.from_json(json)
# print the JSON string representation of the object
print IntersectionSummaryInfo.to_json()

# convert the object into a dict
intersection_summary_info_dict = intersection_summary_info_instance.to_dict()
# create an instance of IntersectionSummaryInfo from a dict
intersection_summary_info_form_dict = intersection_summary_info.from_dict(intersection_summary_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


