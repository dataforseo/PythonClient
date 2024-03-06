[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppendixSerpPriceDataInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional]
**advanced** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional]
**regular** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.appendix_serp_price_data_info import AppendixSerpPriceDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixSerpPriceDataInfo from a JSON string
appendix_serp_price_data_info_instance = AppendixSerpPriceDataInfo.from_json(json)
# print the JSON string representation of the object
print AppendixSerpPriceDataInfo.to_json()

# convert the object into a dict
appendix_serp_price_data_info_dict = appendix_serp_price_data_info_instance.to_dict()
# create an instance of AppendixSerpPriceDataInfo from a dict
appendix_serp_price_data_info_form_dict = appendix_serp_price_data_info.from_dict(appendix_serp_price_data_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")