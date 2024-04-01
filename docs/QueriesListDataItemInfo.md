# QueriesListDataItemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | related query | [optional] 
**value** | **str** | search term popularity represents the popularity of the topic. Scoring is on a relative scale where a value of 100 is the most commonly searched topic and a value of 50 is a topic searched half as often as the most popular term, and so on. | [optional] 

## Example

```python
from dataforseo_client.models.queries_list_data_item_info import QueriesListDataItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of QueriesListDataItemInfo from a JSON string
queries_list_data_item_info_instance = QueriesListDataItemInfo.from_json(json)
# print the JSON string representation of the object
print(QueriesListDataItemInfo.to_json())

# convert the object into a dict
queries_list_data_item_info_dict = queries_list_data_item_info_instance.to_dict()
# create an instance of QueriesListDataItemInfo from a dict
queries_list_data_item_info_form_dict = queries_list_data_item_info.from_dict(queries_list_data_item_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


