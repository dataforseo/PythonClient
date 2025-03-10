# LocalPackDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**description** | **str** | description of the results element in SERP | [optional] 
**domain** | **str** | domain where a link points | [optional] 
**phone** | **str** | phone number | [optional] 
**url** | **str** | relevant URL | [optional] 
**is_paid** | **bool** | indicates whether the element is an ad | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**main_domain** | **str** | primary domain name in SERP | [optional] 
**relative_url** | **str** | URL in SERP that does not specify the HTTPs protocol and domain name | [optional] 
**etv** | **float** | estimated traffic volume estimated organic monthly traffic to the domain calculated as the product of CTR (click-through-rate) and search volume values of the returned keyword learn more about how the metric is calculated in this help center article | [optional] 
**impressions_etv** | **float** | estimated traffic volume based on impressions estimated organic monthly traffic to the domain calculated as the product of CTR (click-through-rate) and impressions values of the returned keyword learn more about how the metric is calculated in this help center article | [optional] 
**estimated_paid_traffic_cost** | **float** | estimated cost of converting organic search traffic into paid represents the estimated monthly cost of running ads for the returned keyword the metric is calculated as the product of organic etv and paid cpc values and indicates the cost of driving the estimated volume of monthly organic traffic through PPC advertising in Google Search learn more about how the metric is calculated in this help center article | [optional] 
**rank_changes** | [**RankChanges**](RankChanges.md) |  | [optional] 
**clickstream_etv** | **int** | estimated traffic volume based on clickstream data calculated as the product of click-through-rate and clickstream search volume values of all keywords the domain ranks for to retrieve results for this field, the parameter include_clickstream_data must be set to true learn more about how the metric is calculated in this help center article https://dataforseo.com/help-center/whats-clickstream-estimated-traffic-volume-and-how-is-it-calculated | [optional] 

## Example

```python
from dataforseo_client.models.local_pack_dataforseo_labs_serp_element_item import LocalPackDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of LocalPackDataforseoLabsSerpElementItem from a JSON string
local_pack_dataforseo_labs_serp_element_item_instance = LocalPackDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(LocalPackDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
local_pack_dataforseo_labs_serp_element_item_dict = local_pack_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of LocalPackDataforseoLabsSerpElementItem from a dict
local_pack_dataforseo_labs_serp_element_item_from_dict = LocalPackDataforseoLabsSerpElementItem.from_dict(local_pack_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


