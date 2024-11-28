# ContentAnalysisCategoriesInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **List[Optional[int]]** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from dataforseo_client.models.content_analysis_categories_info import ContentAnalysisCategoriesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAnalysisCategoriesInfo from a JSON string
content_analysis_categories_info_instance = ContentAnalysisCategoriesInfo.from_json(json)
# print the JSON string representation of the object
print(ContentAnalysisCategoriesInfo.to_json())

# convert the object into a dict
content_analysis_categories_info_dict = content_analysis_categories_info_instance.to_dict()
# create an instance of ContentAnalysisCategoriesInfo from a dict
content_analysis_categories_info_from_dict = ContentAnalysisCategoriesInfo.from_dict(content_analysis_categories_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


