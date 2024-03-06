[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksAvailableFiltersResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_duplicates** | **Dict[str, Optional[str]]** |  | [optional]
**backlinks** | **Dict[str, Optional[str]]** |  | [optional]
**domain_pages** | **Dict[str, Optional[str]]** |  | [optional]
**anchors** | **Dict[str, Optional[str]]** |  | [optional]
**referring_domains** | **Dict[str, Optional[str]]** |  | [optional]
**domain_intersection** | **Dict[str, Optional[str]]** |  | [optional]
**page_intersection** | **Dict[str, Optional[str]]** |  | [optional]
**referring_networks** | **Dict[str, Optional[str]]** |  | [optional]
**domain_pages_summary** | **Dict[str, Optional[str]]** |  | [optional]
**competitors** | **Dict[str, Optional[str]]** |  | [optional]

## Example

```python
from dataforseo_client.models.backlinks_available_filters_result_info import BacklinksAvailableFiltersResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksAvailableFiltersResultInfo from a JSON string
backlinks_available_filters_result_info_instance = BacklinksAvailableFiltersResultInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksAvailableFiltersResultInfo.to_json()

# convert the object into a dict
backlinks_available_filters_result_info_dict = backlinks_available_filters_result_info_instance.to_dict()
# create an instance of BacklinksAvailableFiltersResultInfo from a dict
backlinks_available_filters_result_info_form_dict = backlinks_available_filters_result_info.from_dict(backlinks_available_filters_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")