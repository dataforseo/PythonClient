# StoresCountInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **str** | number of stores that offer the product | [optional] 
**displayed_text** | **str** | text displayed on the Google Shopping page | [optional] 
**count_from_text** | **bool** | whether the number of stores is taken from text indicates whether the number of stores is taken from displayed_text; if the API finds the exact number of stores in the HTML code of the Google Shopping page, this parameter is false; if the API cannot find the number of stores in the HTML code of the page, it takes the number from the displayed_text; in this case, the parameter is true | [optional] 

## Example

```python
from dataforseo_client.models.stores_count_info import StoresCountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StoresCountInfo from a JSON string
stores_count_info_instance = StoresCountInfo.from_json(json)
# print the JSON string representation of the object
print StoresCountInfo.to_json()

# convert the object into a dict
stores_count_info_dict = stores_count_info_instance.to_dict()
# create an instance of StoresCountInfo from a dict
stores_count_info_form_dict = stores_count_info.from_dict(stores_count_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


