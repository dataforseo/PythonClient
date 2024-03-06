[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# TestSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fatal** | **int** | number of fatal microdata errors | [optional]
**error** | **int** | number of serious microdata errors | [optional]
**warning** | **int** | number of microdata warnings | [optional]
**info** | **int** | number of microdata information flags | [optional]

## Example

```python
from dataforseo_client.models.test_summary import TestSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TestSummary from a JSON string
test_summary_instance = TestSummary.from_json(json)
# print the JSON string representation of the object
print TestSummary.to_json()

# convert the object into a dict
test_summary_dict = test_summary_instance.to_dict()
# create an instance of TestSummary from a dict
test_summary_form_dict = test_summary.from_dict(test_summary_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")