[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksIndexResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_backlinks** | **int** | total number of backlinks our database contains for the moment of checking | [optional]
**total_pages** | **int** | total number of pages our database contains for the moment of checking | [optional]
**total_domains** | **int** | total number of domains our database contains for the moment of checking | [optional]
**index_history** | [**List[IndexHistory]**](IndexHistory.md) | index volume data for the past 12 months | [optional]

## Example

```python
from dataforseo_client.models.backlinks_index_result_info import BacklinksIndexResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksIndexResultInfo from a JSON string
backlinks_index_result_info_instance = BacklinksIndexResultInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksIndexResultInfo.to_json()

# convert the object into a dict
backlinks_index_result_info_dict = backlinks_index_result_info_instance.to_dict()
# create an instance of BacklinksIndexResultInfo from a dict
backlinks_index_result_info_form_dict = backlinks_index_result_info.from_dict(backlinks_index_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")