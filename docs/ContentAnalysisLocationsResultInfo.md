# ContentAnalysisLocationsResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_name** | **str** | full name of the location | [optional] 
**country_iso_code** | **str** | ISO country code of the location | [optional] 

## Example

```python
from dataforseo_client.models.content_analysis_locations_result_info import ContentAnalysisLocationsResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAnalysisLocationsResultInfo from a JSON string
content_analysis_locations_result_info_instance = ContentAnalysisLocationsResultInfo.from_json(json)
# print the JSON string representation of the object
print(ContentAnalysisLocationsResultInfo.to_json())

# convert the object into a dict
content_analysis_locations_result_info_dict = content_analysis_locations_result_info_instance.to_dict()
# create an instance of ContentAnalysisLocationsResultInfo from a dict
content_analysis_locations_result_info_form_dict = content_analysis_locations_result_info.from_dict(content_analysis_locations_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


