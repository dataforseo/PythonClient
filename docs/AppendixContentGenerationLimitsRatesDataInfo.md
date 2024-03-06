[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppendixContentGenerationLimitsRatesDataInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generate** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]
**generate_meta_tags** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]
**generate_text** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]
**paraphrase** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]
**check_grammar** | [**AppendixContentGenerationDayLimitsRatesDataInfo**](AppendixContentGenerationDayLimitsRatesDataInfo.md) |  | [optional]
**text_summary** | [**AppendixContentGenerationDayLimitsRatesDataInfo**](AppendixContentGenerationDayLimitsRatesDataInfo.md) |  | [optional]
**generate_sub_topics** | [**AppendixInfo**](AppendixInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.appendix_content_generation_limits_rates_data_info import AppendixContentGenerationLimitsRatesDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixContentGenerationLimitsRatesDataInfo from a JSON string
appendix_content_generation_limits_rates_data_info_instance = AppendixContentGenerationLimitsRatesDataInfo.from_json(json)
# print the JSON string representation of the object
print AppendixContentGenerationLimitsRatesDataInfo.to_json()

# convert the object into a dict
appendix_content_generation_limits_rates_data_info_dict = appendix_content_generation_limits_rates_data_info_instance.to_dict()
# create an instance of AppendixContentGenerationLimitsRatesDataInfo from a dict
appendix_content_generation_limits_rates_data_info_form_dict = appendix_content_generation_limits_rates_data_info.from_dict(appendix_content_generation_limits_rates_data_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")