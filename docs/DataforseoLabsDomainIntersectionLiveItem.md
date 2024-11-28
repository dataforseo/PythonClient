# DataforseoLabsDomainIntersectionLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**keyword_data** | [**KeywordDataInfo**](KeywordDataInfo.md) |  | [optional] 
**first_domain_serp_element** | [**BaseDataforseoLabsSerpElementItem**](BaseDataforseoLabsSerpElementItem.md) |  | [optional] 
**second_domain_serp_element** | [**BaseDataforseoLabsSerpElementItem**](BaseDataforseoLabsSerpElementItem.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_domain_intersection_live_item import DataforseoLabsDomainIntersectionLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsDomainIntersectionLiveItem from a JSON string
dataforseo_labs_domain_intersection_live_item_instance = DataforseoLabsDomainIntersectionLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsDomainIntersectionLiveItem.to_json())

# convert the object into a dict
dataforseo_labs_domain_intersection_live_item_dict = dataforseo_labs_domain_intersection_live_item_instance.to_dict()
# create an instance of DataforseoLabsDomainIntersectionLiveItem from a dict
dataforseo_labs_domain_intersection_live_item_from_dict = DataforseoLabsDomainIntersectionLiveItem.from_dict(dataforseo_labs_domain_intersection_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


