[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# OnPageRedirectLinkElementItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**is_link_relation_conflict** | **bool** | indicates that the link may have a conflict with another link if true, at least one link pointing to the URL in link_to has a rel&#x3D;\&quot;nofollow\&quot; attribute and at least one is dofollow | [optional]

## Example

```python
from dataforseo_client.models.on_page_redirect_link_element_item import OnPageRedirectLinkElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageRedirectLinkElementItem from a JSON string
on_page_redirect_link_element_item_instance = OnPageRedirectLinkElementItem.from_json(json)
# print the JSON string representation of the object
print OnPageRedirectLinkElementItem.to_json()

# convert the object into a dict
on_page_redirect_link_element_item_dict = on_page_redirect_link_element_item_instance.to_dict()
# create an instance of OnPageRedirectLinkElementItem from a dict
on_page_redirect_link_element_item_form_dict = on_page_redirect_link_element_item.from_dict(on_page_redirect_link_element_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")