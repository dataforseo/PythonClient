# TwitterSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the row | [optional] 
**url** | **str** | source URL | [optional] 
**items** | [**List[TwitterElement]**](TwitterElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.twitter_serp_element_item import TwitterSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterSerpElementItem from a JSON string
twitter_serp_element_item_instance = TwitterSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(TwitterSerpElementItem.to_json())

# convert the object into a dict
twitter_serp_element_item_dict = twitter_serp_element_item_instance.to_dict()
# create an instance of TwitterSerpElementItem from a dict
twitter_serp_element_item_from_dict = TwitterSerpElementItem.from_dict(twitter_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


