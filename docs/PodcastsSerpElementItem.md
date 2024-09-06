# PodcastsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PodcastsElement]**](PodcastsElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.podcasts_serp_element_item import PodcastsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of PodcastsSerpElementItem from a JSON string
podcasts_serp_element_item_instance = PodcastsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print PodcastsSerpElementItem.to_json()

# convert the object into a dict
podcasts_serp_element_item_dict = podcasts_serp_element_item_instance.to_dict()
# create an instance of PodcastsSerpElementItem from a dict
podcasts_serp_element_item_form_dict = podcasts_serp_element_item.from_dict(podcasts_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


