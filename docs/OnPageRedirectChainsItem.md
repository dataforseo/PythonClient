# OnPageRedirectChainsItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_redirect_loop** | **bool** | indicates if redirects in chain start and end at the same URL if true, the last URL from the chain redirects back to the original URL | [optional] 
**chain** | [**List[BaseOnPageLinkItemInfo]**](BaseOnPageLinkItemInfo.md) | contains links that form a chain | [optional] 

## Example

```python
from dataforseo_client.models.on_page_redirect_chains_item import OnPageRedirectChainsItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageRedirectChainsItem from a JSON string
on_page_redirect_chains_item_instance = OnPageRedirectChainsItem.from_json(json)
# print the JSON string representation of the object
print(OnPageRedirectChainsItem.to_json())

# convert the object into a dict
on_page_redirect_chains_item_dict = on_page_redirect_chains_item_instance.to_dict()
# create an instance of OnPageRedirectChainsItem from a dict
on_page_redirect_chains_item_from_dict = OnPageRedirectChainsItem.from_dict(on_page_redirect_chains_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


