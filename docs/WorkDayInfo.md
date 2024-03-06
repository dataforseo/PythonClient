[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# WorkDayInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open** | [**WorkTimeInfo**](WorkTimeInfo.md) |  | [optional]
**close** | [**WorkTimeInfo**](WorkTimeInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.work_day_info import WorkDayInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WorkDayInfo from a JSON string
work_day_info_instance = WorkDayInfo.from_json(json)
# print the JSON string representation of the object
print WorkDayInfo.to_json()

# convert the object into a dict
work_day_info_dict = work_day_info_instance.to_dict()
# create an instance of WorkDayInfo from a dict
work_day_info_form_dict = work_day_info.from_dict(work_day_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")