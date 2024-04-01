# TechnologyCategoryInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the technology category example: crm, cart_abandonment | [optional] 
**path** | **str** | path to the technology category example: user_generated_content.content_curation | [optional] 
**title** | **str** | title of the technology category | [optional] 
**technologies** | **List[Optional[str]]** | list of technologies in this category example: \&quot;Salesforce\&quot;, \&quot;CareCart\&quot; | [optional] 

## Example

```python
from dataforseo_client.models.technology_category_info import TechnologyCategoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TechnologyCategoryInfo from a JSON string
technology_category_info_instance = TechnologyCategoryInfo.from_json(json)
# print the JSON string representation of the object
print(TechnologyCategoryInfo.to_json())

# convert the object into a dict
technology_category_info_dict = technology_category_info_instance.to_dict()
# create an instance of TechnologyCategoryInfo from a dict
technology_category_info_form_dict = technology_category_info.from_dict(technology_category_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


