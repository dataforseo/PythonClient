[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# WorkTimeInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hour** | **int** | hours in the 24-hour format | [optional]
**minute** | **int** | minutes | [optional]

## Example

```python
from dataforseo_client.models.work_time_info import WorkTimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WorkTimeInfo from a JSON string
work_time_info_instance = WorkTimeInfo.from_json(json)
# print the JSON string representation of the object
print WorkTimeInfo.to_json()

# convert the object into a dict
work_time_info_dict = work_time_info_instance.to_dict()
# create an instance of WorkTimeInfo from a dict
work_time_info_form_dict = work_time_info.from_dict(work_time_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")