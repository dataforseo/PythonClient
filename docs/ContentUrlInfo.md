# ContentUrlInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | other URL found in the content element | [optional] 
**anchor_text** | **str** | text of the URL’s anchor | [optional] 

## Example

```python
from dataforseo_client.models.content_url_info import ContentUrlInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentUrlInfo from a JSON string
content_url_info_instance = ContentUrlInfo.from_json(json)
# print the JSON string representation of the object
print(ContentUrlInfo.to_json())

# convert the object into a dict
content_url_info_dict = content_url_info_instance.to_dict()
# create an instance of ContentUrlInfo from a dict
content_url_info_from_dict = ContentUrlInfo.from_dict(content_url_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


