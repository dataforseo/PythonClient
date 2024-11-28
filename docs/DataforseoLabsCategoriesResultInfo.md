# DataforseoLabsCategoriesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_code** | **int** | category code | [optional] 
**category_name** | **str** | full name of the category | [optional] 
**category_code_parent** | **int** | the code of the superordinate category example: \&quot;category_code\&quot;: 10178, \&quot;category_name\&quot;: \&quot;Apparel Accessories\&quot;, \&quot;category_code_parent\&quot;: 10021 where category_code_parent corresponds to: \&quot;category_code\&quot;: 10021, \&quot;category_name\&quot;: \&quot;Apparel\&quot; \&quot;category_code_parent\&quot;: null | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_categories_result_info import DataforseoLabsCategoriesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsCategoriesResultInfo from a JSON string
dataforseo_labs_categories_result_info_instance = DataforseoLabsCategoriesResultInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsCategoriesResultInfo.to_json())

# convert the object into a dict
dataforseo_labs_categories_result_info_dict = dataforseo_labs_categories_result_info_instance.to_dict()
# create an instance of DataforseoLabsCategoriesResultInfo from a dict
dataforseo_labs_categories_result_info_from_dict = DataforseoLabsCategoriesResultInfo.from_dict(dataforseo_labs_categories_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


