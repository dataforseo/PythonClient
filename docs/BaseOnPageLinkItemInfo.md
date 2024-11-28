# BaseOnPageLinkItemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**domain_from** | **str** | referring domain the link was found on this domain | [optional] 
**domain_to** | **str** | referenced domain the link is pointing to this domain | [optional] 
**page_from** | **str** | referring page relative URL of the page on which the link was found | [optional] 
**page_to** | **str** | referenced page relative URL of the page to which the link is pointing | [optional] 
**link_from** | **str** | referring page absolute URL of the page on which the link was found | [optional] 
**link_to** | **str** | referenced page absolute URL of the page to which the link is pointing | [optional] 
**dofollow** | **bool** | indicates whether the link is dofollow if the value is true, the link doesn’t have a rel&#x3D;\&quot;nofollow\&quot; attribute | [optional] 
**page_from_scheme** | **str** | url scheme of the referring page | [optional] 
**page_to_scheme** | **str** | url scheme of the referenced page | [optional] 
**direction** | **str** | direction of the link possible values: internal, external | [optional] 
**is_broken** | **bool** | link is broken indicates whether a link is directing to a broken page or resource | [optional] 
**is_link_relation_conflict** | **bool** | indicates that the link may have a conflict with another link if true, at least one link pointing to link_to has a rel&#x3D;\&quot;nofollow\&quot; attribute and at least one is dofollow | [optional] 

## Example

```python
from dataforseo_client.models.base_on_page_link_item_info import BaseOnPageLinkItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BaseOnPageLinkItemInfo from a JSON string
base_on_page_link_item_info_instance = BaseOnPageLinkItemInfo.from_json(json)
# print the JSON string representation of the object
print(BaseOnPageLinkItemInfo.to_json())

# convert the object into a dict
base_on_page_link_item_info_dict = base_on_page_link_item_info_instance.to_dict()
# create an instance of BaseOnPageLinkItemInfo from a dict
base_on_page_link_item_info_from_dict = BaseOnPageLinkItemInfo.from_dict(base_on_page_link_item_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


