# PodcastsElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**url** | **str** | URL | [optional] 
**description** | **str** | description | [optional] 
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**time_to_play** | **str** | the total time it will take to play an episode | [optional] 

## Example

```python
from dataforseo_client.models.podcasts_element import PodcastsElement

# TODO update the JSON string below
json = "{}"
# create an instance of PodcastsElement from a JSON string
podcasts_element_instance = PodcastsElement.from_json(json)
# print the JSON string representation of the object
print(PodcastsElement.to_json())

# convert the object into a dict
podcasts_element_dict = podcasts_element_instance.to_dict()
# create an instance of PodcastsElement from a dict
podcasts_element_form_dict = podcasts_element.from_dict(podcasts_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


