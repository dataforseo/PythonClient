[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# OnPageLighthouseAuditsResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audits** | **List[Optional[str]]** | the list of available lighthouse audits an array containing the titles of available audits Note: the titles can change depending on if the audit passed or failed and may contain markdown code | [optional]

## Example

```python
from dataforseo_client.models.on_page_lighthouse_audits_result_info import OnPageLighthouseAuditsResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageLighthouseAuditsResultInfo from a JSON string
on_page_lighthouse_audits_result_info_instance = OnPageLighthouseAuditsResultInfo.from_json(json)
# print the JSON string representation of the object
print OnPageLighthouseAuditsResultInfo.to_json()

# convert the object into a dict
on_page_lighthouse_audits_result_info_dict = on_page_lighthouse_audits_result_info_instance.to_dict()
# create an instance of OnPageLighthouseAuditsResultInfo from a dict
on_page_lighthouse_audits_result_info_form_dict = on_page_lighthouse_audits_result_info.from_dict(on_page_lighthouse_audits_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")