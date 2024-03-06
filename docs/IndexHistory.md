[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# IndexHistory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | date for which index volume data is provided in the UTC format: “yyyy-mm-dd” example: 2021-10-01 | [optional]
**total_backlinks** | **int** | total number of backlinks our database contained on the given date | [optional]
**total_pages** | **int** | total number of pages our database contained on the given date | [optional]
**total_domains** | **int** | total number of domains our database contained on the given date | [optional]

## Example

```python
from dataforseo_client.models.index_history import IndexHistory

# TODO update the JSON string below
json = "{}"
# create an instance of IndexHistory from a JSON string
index_history_instance = IndexHistory.from_json(json)
# print the JSON string representation of the object
print IndexHistory.to_json()

# convert the object into a dict
index_history_dict = index_history_instance.to_dict()
# create an instance of IndexHistory from a dict
index_history_form_dict = index_history.from_dict(index_history_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")