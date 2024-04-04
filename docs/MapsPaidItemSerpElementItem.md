# MapsPaidItemSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**domain** | **str** | domain in the SERP element | [optional] 
**title** | **str** | title of the result in SERP | [optional] 
**url** | **str** | relevant URL in SERP | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**rating_distribution** | **Dict[str, Optional[int]]** | the distribution of ratings of the business entity the object displays the number of 1-star to 5-star ratings, as reviewed by users | [optional] 

## Example

```python
from dataforseo_client.models.maps_paid_item_serp_element_item import MapsPaidItemSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of MapsPaidItemSerpElementItem from a JSON string
maps_paid_item_serp_element_item_instance = MapsPaidItemSerpElementItem.from_json(json)
# print the JSON string representation of the object
print MapsPaidItemSerpElementItem.to_json()

# convert the object into a dict
maps_paid_item_serp_element_item_dict = maps_paid_item_serp_element_item_instance.to_dict()
# create an instance of MapsPaidItemSerpElementItem from a dict
maps_paid_item_serp_element_item_form_dict = maps_paid_item_serp_element_item.from_dict(maps_paid_item_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


