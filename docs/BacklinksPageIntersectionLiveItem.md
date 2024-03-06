[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksPageIntersectionLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_intersection** | **Dict[str, List[BacklinksPageIntersectionInfo]]** | contains data on pages that link to the corresponding targets specified in the POST array data is provided in separate objects corresponding to pages specified in the targets object | [optional]
**summary** | [**Summary**](Summary.md) |  | [optional]

## Example

```python
from dataforseo_client.models.backlinks_page_intersection_live_item import BacklinksPageIntersectionLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksPageIntersectionLiveItem from a JSON string
backlinks_page_intersection_live_item_instance = BacklinksPageIntersectionLiveItem.from_json(json)
# print the JSON string representation of the object
print BacklinksPageIntersectionLiveItem.to_json()

# convert the object into a dict
backlinks_page_intersection_live_item_dict = backlinks_page_intersection_live_item_instance.to_dict()
# create an instance of BacklinksPageIntersectionLiveItem from a dict
backlinks_page_intersection_live_item_form_dict = backlinks_page_intersection_live_item.from_dict(backlinks_page_intersection_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")