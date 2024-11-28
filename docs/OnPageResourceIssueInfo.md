# OnPageResourceIssueInfo

resource errors and warnings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[OnPageResourceIssueItemInfo]**](OnPageResourceIssueItemInfo.md) | resource errors | [optional] 
**warnings** | [**List[OnPageResourceIssueItemInfo]**](OnPageResourceIssueItemInfo.md) | resource warnings | [optional] 

## Example

```python
from dataforseo_client.models.on_page_resource_issue_info import OnPageResourceIssueInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageResourceIssueInfo from a JSON string
on_page_resource_issue_info_instance = OnPageResourceIssueInfo.from_json(json)
# print the JSON string representation of the object
print(OnPageResourceIssueInfo.to_json())

# convert the object into a dict
on_page_resource_issue_info_dict = on_page_resource_issue_info_instance.to_dict()
# create an instance of OnPageResourceIssueInfo from a dict
on_page_resource_issue_info_from_dict = OnPageResourceIssueInfo.from_dict(on_page_resource_issue_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


