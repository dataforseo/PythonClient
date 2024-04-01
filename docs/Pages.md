# Pages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**similarity** | **int** | content similarity score by default, the content is considered duplicate if the value is greater than or equals 6 can take values from 0 to 10 | [optional] 
**page** | [**List[BaseOnPageResourceItemInfo]**](BaseOnPageResourceItemInfo.md) | information about the page with duplicate content | [optional] 

## Example

```python
from dataforseo_client.models.pages import Pages

# TODO update the JSON string below
json = "{}"
# create an instance of Pages from a JSON string
pages_instance = Pages.from_json(json)
# print the JSON string representation of the object
print(Pages.to_json())

# convert the object into a dict
pages_dict = pages_instance.to_dict()
# create an instance of Pages from a dict
pages_form_dict = pages.from_dict(pages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


