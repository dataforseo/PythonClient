# QueriesListDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top** | [**List[QueriesListDataItemInfo]**](QueriesListDataItemInfo.md) | the most popular related topics represents the list of the most popular related topics | [optional] 
**rising** | [**List[QueriesListDataItemInfo]**](QueriesListDataItemInfo.md) | emerging related topics represents the list of related topics with the biggest increase in search frequency since the last time period | [optional] 

## Example

```python
from dataforseo_client.models.queries_list_data_info import QueriesListDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of QueriesListDataInfo from a JSON string
queries_list_data_info_instance = QueriesListDataInfo.from_json(json)
# print the JSON string representation of the object
print(QueriesListDataInfo.to_json())

# convert the object into a dict
queries_list_data_info_dict = queries_list_data_info_instance.to_dict()
# create an instance of QueriesListDataInfo from a dict
queries_list_data_info_from_dict = QueriesListDataInfo.from_dict(queries_list_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


