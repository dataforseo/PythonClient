# BusinessDataTripadvisorLanguagesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_name** | **str** | language name | [optional] 
**language_code** | **str** | language code according to ISO 639-1 | [optional] 

## Example

```python
from dataforseo_client.models.business_data_tripadvisor_languages_result_info import BusinessDataTripadvisorLanguagesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataTripadvisorLanguagesResultInfo from a JSON string
business_data_tripadvisor_languages_result_info_instance = BusinessDataTripadvisorLanguagesResultInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataTripadvisorLanguagesResultInfo.to_json())

# convert the object into a dict
business_data_tripadvisor_languages_result_info_dict = business_data_tripadvisor_languages_result_info_instance.to_dict()
# create an instance of BusinessDataTripadvisorLanguagesResultInfo from a dict
business_data_tripadvisor_languages_result_info_form_dict = business_data_tripadvisor_languages_result_info.from_dict(business_data_tripadvisor_languages_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


