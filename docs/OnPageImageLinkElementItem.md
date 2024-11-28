# OnPageImageLinkElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_attribute** | **List[Optional[str]]** | link attribute added to external link indicates link attributes added to the link_to on the page_from example: [\&quot;ugc\&quot;,\&quot;noopener\&quot;] | [optional] 
**text** | **str** | anchor text | [optional] 
**image_alt** | **str** | alternative text for the image | [optional] 
**image_src** | **str** | url of the image | [optional] 
**page_to_status_code** | **int** | status code of the referenced page status code of the page to which the link is pointing | [optional] 

## Example

```python
from dataforseo_client.models.on_page_image_link_element_item import OnPageImageLinkElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageImageLinkElementItem from a JSON string
on_page_image_link_element_item_instance = OnPageImageLinkElementItem.from_json(json)
# print the JSON string representation of the object
print(OnPageImageLinkElementItem.to_json())

# convert the object into a dict
on_page_image_link_element_item_dict = on_page_image_link_element_item_instance.to_dict()
# create an instance of OnPageImageLinkElementItem from a dict
on_page_image_link_element_item_from_dict = OnPageImageLinkElementItem.from_dict(on_page_image_link_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


