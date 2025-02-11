# Urls


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | other URL found in the content element | [optional] 
**anchor_text** | **str** | text of the URL’s anchor | [optional] 

## Example

```python
from dataforseo_client.models.urls import Urls

# TODO update the JSON string below
json = "{}"
# create an instance of Urls from a JSON string
urls_instance = Urls.from_json(json)
# print the JSON string representation of the object
print(Urls.to_json())

# convert the object into a dict
urls_dict = urls_instance.to_dict()
# create an instance of Urls from a dict
urls_from_dict = Urls.from_dict(urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


