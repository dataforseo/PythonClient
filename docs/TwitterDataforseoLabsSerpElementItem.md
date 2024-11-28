# TwitterDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**title** | **str** | title of the result in SERP | [optional] 
**url** | **str** | relevant URL of the Ad element in SERP | [optional] 
**items** | [**List[TwitterElement]**](TwitterElement.md) | elements of search results found in SERP | [optional] 

## Example

```python
from dataforseo_client.models.twitter_dataforseo_labs_serp_element_item import TwitterDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterDataforseoLabsSerpElementItem from a JSON string
twitter_dataforseo_labs_serp_element_item_instance = TwitterDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(TwitterDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
twitter_dataforseo_labs_serp_element_item_dict = twitter_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of TwitterDataforseoLabsSerpElementItem from a dict
twitter_dataforseo_labs_serp_element_item_from_dict = TwitterDataforseoLabsSerpElementItem.from_dict(twitter_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


