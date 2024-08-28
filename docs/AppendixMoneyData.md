# AppendixMoneyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | total amount of money deposited to your account | [optional] 
**balance** | **float** | amount of money left in your account | [optional] 
**limits** | [**AppendixLimitsMoneyData**](AppendixLimitsMoneyData.md) |  | [optional] 
**statistics** | [**AppendixStatisticsMoneyData**](AppendixStatisticsMoneyData.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_money_data import AppendixMoneyData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixMoneyData from a JSON string
appendix_money_data_instance = AppendixMoneyData.from_json(json)
# print the JSON string representation of the object
print AppendixMoneyData.to_json()

# convert the object into a dict
appendix_money_data_dict = appendix_money_data_instance.to_dict()
# create an instance of AppendixMoneyData from a dict
appendix_money_data_form_dict = appendix_money_data.from_dict(appendix_money_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


