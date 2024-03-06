[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# OnPageContentParsingItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**fetch_time** | **str** | date and time when the content was fethced example: \&quot;2022-11-01 10:02:52 +00:00\&quot; | [optional]
**status_code** | **int** | status code of the page | [optional]
**page_content** | [**PageContentInfo**](PageContentInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.on_page_content_parsing_item import OnPageContentParsingItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageContentParsingItem from a JSON string
on_page_content_parsing_item_instance = OnPageContentParsingItem.from_json(json)
# print the JSON string representation of the object
print OnPageContentParsingItem.to_json()

# convert the object into a dict
on_page_content_parsing_item_dict = on_page_content_parsing_item_instance.to_dict()
# create an instance of OnPageContentParsingItem from a dict
on_page_content_parsing_item_form_dict = on_page_content_parsing_item.from_dict(on_page_content_parsing_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")