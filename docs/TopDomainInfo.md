[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# TopDomainInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional]
**count** | **int** |  | [optional]

## Example

```python
from dataforseo_client.models.top_domain_info import TopDomainInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TopDomainInfo from a JSON string
top_domain_info_instance = TopDomainInfo.from_json(json)
# print the JSON string representation of the object
print TopDomainInfo.to_json()

# convert the object into a dict
top_domain_info_dict = top_domain_info_instance.to_dict()
# create an instance of TopDomainInfo from a dict
top_domain_info_form_dict = top_domain_info.from_dict(top_domain_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")