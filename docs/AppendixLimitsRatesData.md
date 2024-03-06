[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppendixLimitsRatesData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | [**AppendixDayLimitsRatesData**](AppendixDayLimitsRatesData.md) |  | [optional]
**minute** | [**AppendixDataInfo**](AppendixDataInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.appendix_limits_rates_data import AppendixLimitsRatesData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixLimitsRatesData from a JSON string
appendix_limits_rates_data_instance = AppendixLimitsRatesData.from_json(json)
# print the JSON string representation of the object
print AppendixLimitsRatesData.to_json()

# convert the object into a dict
appendix_limits_rates_data_dict = appendix_limits_rates_data_instance.to_dict()
# create an instance of AppendixLimitsRatesData from a dict
appendix_limits_rates_data_form_dict = appendix_limits_rates_data.from_dict(appendix_limits_rates_data_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")