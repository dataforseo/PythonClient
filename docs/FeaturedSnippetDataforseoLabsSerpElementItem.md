# FeaturedSnippetDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**domain** | **str** | subdomain in SERP | [optional] 
**title** | **str** | title of the result in SERP | [optional] 
**featured_title** | **str** | the title of the featured snippets source page | [optional] 
**description** | **str** | description of the results element in SERP | [optional] 
**url** | **str** | relevant URL in SERP | [optional] 
**table** | [**Table**](Table.md) |  | [optional] 
**main_domain** | **str** | primary domain name in SERP | [optional] 
**relative_url** | **str** | relative URL in SERP | [optional] 
**etv** | **float** | estimated traffic volume estimated organic monthly traffic to the domain; calculated as the product of CTR (click-through-rate) and search volume values of the returned keyword learn more about how the metric is calculated in this help center article | [optional] 
**estimated_paid_traffic_cost** | **float** | estimated cost of converting organic search traffic into paid represents the estimated monthly cost of running ads (USD) for the returned keyword; the metric is calculated as the product of organic etv and paid cpc values and indicates the cost of driving the estimated volume of monthly organic traffic through PPC advertising in Bing Search learn more about how the metric is calculated in this help center article | [optional] 
**rank_changes** | [**RankChanges**](RankChanges.md) |  | [optional] 
**backlinks_info** | [**BacklinksInfo**](BacklinksInfo.md) |  | [optional] 
**rank_info** | [**RankInfo**](RankInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.featured_snippet_dataforseo_labs_serp_element_item import FeaturedSnippetDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of FeaturedSnippetDataforseoLabsSerpElementItem from a JSON string
featured_snippet_dataforseo_labs_serp_element_item_instance = FeaturedSnippetDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(FeaturedSnippetDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
featured_snippet_dataforseo_labs_serp_element_item_dict = featured_snippet_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of FeaturedSnippetDataforseoLabsSerpElementItem from a dict
featured_snippet_dataforseo_labs_serp_element_item_from_dict = FeaturedSnippetDataforseoLabsSerpElementItem.from_dict(featured_snippet_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


