# PaidDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the result in SERP | [optional] 
**domain** | **str** | subdomain in SERP | [optional] 
**description** | **str** | description of the results element in SERP | [optional] 
**breadcrumb** | **str** | breadcrumb in SERP | [optional] 
**url** | **str** | relevant URL in SERP | [optional] 
**highlighted** | **List[Optional[str]]** | words highlighted in bold within the results description | [optional] 
**extra** | **Dict[str, Optional[str]]** | additional information about the result | [optional] 
**description_rows** | **List[Optional[str]]** | extended description if there is none, equals null | [optional] 
**links** | [**List[AdLinkElement]**](AdLinkElement.md) | sitelinks the links shown below some of Google’s search results if there are none, equals null | [optional] 
**main_domain** | **str** | primary domain name in SERP | [optional] 
**relative_url** | **str** | URL in SERP that does not specify the HTTPs protocol and domain name | [optional] 
**etv** | **float** | estimated traffic volume estimated paid monthly traffic to the domain calculated as the product of CTR (click-through-rate) and search volume values of all keywords in the category that the domain ranks for learn more about how the metric is calculated in this help center article | [optional] 
**impressions_etv** | **float** | estimated traffic volume based on impressions estimated paid monthly traffic to the domain calculated as the product of CTR (click-through-rate) and impressions values of all keywords in the category that the domain ranks for learn more about how the metric is calculated in this help center article | [optional] 
**estimated_paid_traffic_cost** | **float** | estimated cost of monthly search traffic represents the estimated cost of paid monthly traffic (USD) based on etv and cpc values of all keywords in the category that the domain ranks for learn more about how the metric is calculated in this help center article | [optional] 
**clickstream_etv** | **int** | estimated traffic volume based on clickstream data calculated as the product of click-through-rate and clickstream search volume values of all keywords the domain ranks for to retrieve results for this field, the parameter include_clickstream_data must be set to true learn more about how the metric is calculated in this help center article | [optional] 
**rank_changes** | [**RankChanges**](RankChanges.md) |  | [optional] 
**backlinks_info** | [**BacklinksInfo**](BacklinksInfo.md) |  | [optional] 
**rank_info** | [**RankInfo**](RankInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.paid_dataforseo_labs_serp_element_item import PaidDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of PaidDataforseoLabsSerpElementItem from a JSON string
paid_dataforseo_labs_serp_element_item_instance = PaidDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print PaidDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
paid_dataforseo_labs_serp_element_item_dict = paid_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of PaidDataforseoLabsSerpElementItem from a dict
paid_dataforseo_labs_serp_element_item_form_dict = paid_dataforseo_labs_serp_element_item.from_dict(paid_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


