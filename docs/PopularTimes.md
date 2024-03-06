[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# PopularTimes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**popular_times_by_days** | **Dict[str, Optional[List[BusyWorkingTimeInfo]]]** | popular hours information about busy hours of the local establishment on each day of the week | [optional]

## Example

```python
from dataforseo_client.models.popular_times import PopularTimes

# TODO update the JSON string below
json = "{}"
# create an instance of PopularTimes from a JSON string
popular_times_instance = PopularTimes.from_json(json)
# print the JSON string representation of the object
print PopularTimes.to_json()

# convert the object into a dict
popular_times_dict = popular_times_instance.to_dict()
# create an instance of PopularTimes from a dict
popular_times_form_dict = popular_times.from_dict(popular_times_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")