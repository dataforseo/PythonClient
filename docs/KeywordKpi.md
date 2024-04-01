# KeywordKpi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desktop** | [**List[KeywordKpiInfo]**](KeywordKpiInfo.md) | keyword data aggregated for desktop devices if there is no data, then the value is null | [optional] 
**mobile** | [**List[KeywordKpiInfo]**](KeywordKpiInfo.md) | keyword data aggregated for mobile devices if there is no data, then the value is null | [optional] 
**tablet** | [**List[KeywordKpiInfo]**](KeywordKpiInfo.md) | keyword data aggregated for tablet devices if there is no data, then the value is null | [optional] 

## Example

```python
from dataforseo_client.models.keyword_kpi import KeywordKpi

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordKpi from a JSON string
keyword_kpi_instance = KeywordKpi.from_json(json)
# print the JSON string representation of the object
print(KeywordKpi.to_json())

# convert the object into a dict
keyword_kpi_dict = keyword_kpi_instance.to_dict()
# create an instance of KeywordKpi from a dict
keyword_kpi_form_dict = keyword_kpi.from_dict(keyword_kpi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


