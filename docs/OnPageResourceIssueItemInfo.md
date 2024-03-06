[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# OnPageResourceIssueItemInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line** | **int** | line where the error was found | [optional]
**column** | **int** | column where the error was found | [optional]
**message** | **str** | text message of the error the full list of possible HTML errors can be found here | [optional]
**status_code** | **int** | status code of the error possible values: 0 — Unidentified Error; 501 — Html Parse Error; 1501 — JS Parse Error; 2501 — CSS Parse Error; 3501 — Image Parse Error; 3502 — Image Scale Is Zero; 3503 — Image Size Is Zero; 3504 — Image Format Invalid | [optional]

## Example

```python
from dataforseo_client.models.on_page_resource_issue_item_info import OnPageResourceIssueItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageResourceIssueItemInfo from a JSON string
on_page_resource_issue_item_info_instance = OnPageResourceIssueItemInfo.from_json(json)
# print the JSON string representation of the object
print OnPageResourceIssueItemInfo.to_json()

# convert the object into a dict
on_page_resource_issue_item_info_dict = on_page_resource_issue_item_info_instance.to_dict()
# create an instance of OnPageResourceIssueItemInfo from a dict
on_page_resource_issue_item_info_form_dict = on_page_resource_issue_item_info.from_dict(on_page_resource_issue_item_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")