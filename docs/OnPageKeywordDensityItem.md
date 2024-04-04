# OnPageKeywordDensityItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | returned keyword | [optional] 
**frequency** | **int** | keyword frequency number of times the keyword appears on the website (or webpage if you specified a url) | [optional] 
**density** | **int** | keyword density calculated as a ratio of frequency to the total count of keywords with the set keyword_length on the web page or website | [optional] 

## Example

```python
from dataforseo_client.models.on_page_keyword_density_item import OnPageKeywordDensityItem

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageKeywordDensityItem from a JSON string
on_page_keyword_density_item_instance = OnPageKeywordDensityItem.from_json(json)
# print the JSON string representation of the object
print OnPageKeywordDensityItem.to_json()

# convert the object into a dict
on_page_keyword_density_item_dict = on_page_keyword_density_item_instance.to_dict()
# create an instance of OnPageKeywordDensityItem from a dict
on_page_keyword_density_item_form_dict = on_page_keyword_density_item.from_dict(on_page_keyword_density_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


