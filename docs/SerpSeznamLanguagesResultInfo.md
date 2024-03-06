[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# SerpSeznamLanguagesResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_name** | **str** | language name | [optional]
**language_code** | **str** | language code according to ISO 639-1 | [optional]

## Example

```python
from dataforseo_client.models.serp_seznam_languages_result_info import SerpSeznamLanguagesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpSeznamLanguagesResultInfo from a JSON string
serp_seznam_languages_result_info_instance = SerpSeznamLanguagesResultInfo.from_json(json)
# print the JSON string representation of the object
print SerpSeznamLanguagesResultInfo.to_json()

# convert the object into a dict
serp_seznam_languages_result_info_dict = serp_seznam_languages_result_info_instance.to_dict()
# create an instance of SerpSeznamLanguagesResultInfo from a dict
serp_seznam_languages_result_info_form_dict = serp_seznam_languages_result_info.from_dict(serp_seznam_languages_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")