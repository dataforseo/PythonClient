# DataforseoLabsBingDomainIntersectionLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type search engine type specified in a POST request; for this endpoint, the field equals bing | [optional] 
**keyword_data** | [**KeywordDataKeywordDataInfo**](KeywordDataKeywordDataInfo.md) |  | [optional] 
**first_domain_serp_element** | [**BaseDataforseoLabsSerpElementItem**](BaseDataforseoLabsSerpElementItem.md) |  | [optional] 
**second_domain_serp_element** | [**BaseDataforseoLabsSerpElementItem**](BaseDataforseoLabsSerpElementItem.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_bing_domain_intersection_live_item import DataforseoLabsBingDomainIntersectionLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsBingDomainIntersectionLiveItem from a JSON string
dataforseo_labs_bing_domain_intersection_live_item_instance = DataforseoLabsBingDomainIntersectionLiveItem.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsBingDomainIntersectionLiveItem.to_json()

# convert the object into a dict
dataforseo_labs_bing_domain_intersection_live_item_dict = dataforseo_labs_bing_domain_intersection_live_item_instance.to_dict()
# create an instance of DataforseoLabsBingDomainIntersectionLiveItem from a dict
dataforseo_labs_bing_domain_intersection_live_item_form_dict = dataforseo_labs_bing_domain_intersection_live_item.from_dict(dataforseo_labs_bing_domain_intersection_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


