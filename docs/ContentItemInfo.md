[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ContentItemInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | content text | [optional]
**url** | **str** | page URL displayed in case the text is a link anchor | [optional]

## Example

```python
from dataforseo_client.models.content_item_info import ContentItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentItemInfo from a JSON string
content_item_info_instance = ContentItemInfo.from_json(json)
# print the JSON string representation of the object
print ContentItemInfo.to_json()

# convert the object into a dict
content_item_info_dict = content_item_info_instance.to_dict()
# create an instance of ContentItemInfo from a dict
content_item_info_form_dict = content_item_info.from_dict(content_item_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")