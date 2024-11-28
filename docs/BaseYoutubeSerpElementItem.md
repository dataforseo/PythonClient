# BaseYoutubeSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP for the target domain absolute position among all the elements in SERP | [optional] 

## Example

```python
from dataforseo_client.models.base_youtube_serp_element_item import BaseYoutubeSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of BaseYoutubeSerpElementItem from a JSON string
base_youtube_serp_element_item_instance = BaseYoutubeSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(BaseYoutubeSerpElementItem.to_json())

# convert the object into a dict
base_youtube_serp_element_item_dict = base_youtube_serp_element_item_instance.to_dict()
# create an instance of BaseYoutubeSerpElementItem from a dict
base_youtube_serp_element_item_from_dict = BaseYoutubeSerpElementItem.from_dict(base_youtube_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


