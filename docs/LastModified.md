[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# LastModified

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | **str** | date and time when the header was last modified in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 if there is no data, the value will be null | [optional]
**sitemap** | **str** | date and time when the sitemap was last modified in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 if there is no data, the value will be null | [optional]
**meta_tag** | **str** | date and time when the meta tag was last modified in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 if there is no data, the value will be null | [optional]

## Example

```python
from dataforseo_client.models.last_modified import LastModified

# TODO update the JSON string below
json = "{}"
# create an instance of LastModified from a JSON string
last_modified_instance = LastModified.from_json(json)
# print the JSON string representation of the object
print LastModified.to_json()

# convert the object into a dict
last_modified_dict = last_modified_instance.to_dict()
# create an instance of LastModified from a dict
last_modified_form_dict = last_modified.from_dict(last_modified_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")