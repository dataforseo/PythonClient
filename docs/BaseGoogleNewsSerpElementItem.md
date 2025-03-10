# BaseGoogleNewsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the row | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.base_google_news_serp_element_item import BaseGoogleNewsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of BaseGoogleNewsSerpElementItem from a JSON string
base_google_news_serp_element_item_instance = BaseGoogleNewsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(BaseGoogleNewsSerpElementItem.to_json())

# convert the object into a dict
base_google_news_serp_element_item_dict = base_google_news_serp_element_item_instance.to_dict()
# create an instance of BaseGoogleNewsSerpElementItem from a dict
base_google_news_serp_element_item_from_dict = BaseGoogleNewsSerpElementItem.from_dict(base_google_news_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


