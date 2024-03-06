[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppendixRatesData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | [**AppendixLimitsRatesData**](AppendixLimitsRatesData.md) |  | [optional]
**statistics** | [**AppendixStatisticsDataInfo**](AppendixStatisticsDataInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.appendix_rates_data import AppendixRatesData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixRatesData from a JSON string
appendix_rates_data_instance = AppendixRatesData.from_json(json)
# print the JSON string representation of the object
print AppendixRatesData.to_json()

# convert the object into a dict
appendix_rates_data_dict = appendix_rates_data_instance.to_dict()
# create an instance of AppendixRatesData from a dict
appendix_rates_data_form_dict = appendix_rates_data.from_dict(appendix_rates_data_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")