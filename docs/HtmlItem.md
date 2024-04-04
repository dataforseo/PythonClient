# HtmlItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | serial number of the returned HTML page | [optional] 
**var_date** | **str** | date and time when the HTML page was scanned in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**html** | **str** | HTML page | [optional] 

## Example

```python
from dataforseo_client.models.html_item import HtmlItem

# TODO update the JSON string below
json = "{}"
# create an instance of HtmlItem from a JSON string
html_item_instance = HtmlItem.from_json(json)
# print the JSON string representation of the object
print HtmlItem.to_json()

# convert the object into a dict
html_item_dict = html_item_instance.to_dict()
# create an instance of HtmlItem from a dict
html_item_form_dict = html_item.from_dict(html_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


