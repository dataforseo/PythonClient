# AdLinkElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of the element | [optional] 
**description** | **str** | description of the results element in SERP | [optional] 
**url** | **str** | URL of element | [optional] 
**domain** | **str** | domain where a link points | [optional] 
**ad_aclk** | **str** | the identifier of the ad | [optional] 

## Example

```python
from dataforseo_client.models.ad_link_element import AdLinkElement

# TODO update the JSON string below
json = "{}"
# create an instance of AdLinkElement from a JSON string
ad_link_element_instance = AdLinkElement.from_json(json)
# print the JSON string representation of the object
print(AdLinkElement.to_json())

# convert the object into a dict
ad_link_element_dict = ad_link_element_instance.to_dict()
# create an instance of AdLinkElement from a dict
ad_link_element_from_dict = AdLinkElement.from_dict(ad_link_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


