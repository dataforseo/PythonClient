# ContentAnalysisCategoriesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_code** | **int** | category code | [optional] 
**category_name** | **str** | full name of the category | [optional] 
**category_code_parent** | **int** | the code of the superordinate category example: \&quot;category_code\&quot;: 10178, \&quot;category_name\&quot;: \&quot;Apparel Accessories\&quot;, \&quot;category_code_parent\&quot;: 10021 where category_code_parent corresponds to: \&quot;category_code\&quot;: 10178, \&quot;category_name\&quot;: \&quot;Apparel Accessories\&quot; | [optional] 

## Example

```python
from dataforseo_client.models.content_analysis_categories_result_info import ContentAnalysisCategoriesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAnalysisCategoriesResultInfo from a JSON string
content_analysis_categories_result_info_instance = ContentAnalysisCategoriesResultInfo.from_json(json)
# print the JSON string representation of the object
print(ContentAnalysisCategoriesResultInfo.to_json())

# convert the object into a dict
content_analysis_categories_result_info_dict = content_analysis_categories_result_info_instance.to_dict()
# create an instance of ContentAnalysisCategoriesResultInfo from a dict
content_analysis_categories_result_info_from_dict = ContentAnalysisCategoriesResultInfo.from_dict(content_analysis_categories_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


