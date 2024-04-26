# OrganicDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**domain** | **str** | subdomain in SERP | [optional] 
**title** | **str** | title of the result in SERP | [optional] 
**url** | **str** | relevant URL in SERP | [optional] 
**breadcrumb** | **str** | breadcrumb in SERP | [optional] 
**website_name** | **str** | relevant website name in SERP | [optional] 
**is_image** | **bool** | indicates whether the element contains an image | [optional] 
**is_video** | **bool** | indicates whether the element contains a video | [optional] 
**is_featured_snippet** | **bool** | indicates whether the element is a featured_snippet | [optional] 
**is_malicious** | **bool** | indicates whether the element is marked as malicious | [optional] 
**description** | **str** | description of the results element in SERP | [optional] 
**pre_snippet** | **str** | includes additional information appended before the result description in SERP | [optional] 
**extended_snippet** | **str** | includes additional information appended after the result description in SERP | [optional] 
**amp_version** | **bool** | Accelerated Mobile Pages indicates whether an item has the Accelerated Mobile Page (AMP) version | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**highlighted** | **List[Optional[str]]** | words highlighted in bold within the results description | [optional] 
**links** | [**List[AdLinkElement]**](AdLinkElement.md) | sitelinks the links shown below some of Google’s search results if there are none, equals null | [optional] 
**about_this_result** | **object** | contains information from the ‘About this result’ panel ‘About this result’ panel provides additional context about why Google returned this result for the given query; this feature appears after clicking on the three dots next to most results | [optional] 
**main_domain** | **str** | primary domain name in SERP | [optional] 
**relative_url** | **str** | URL in SERP that does not specify the HTTPs protocol and domain name | [optional] 
**etv** | **float** | estimated traffic volume estimated paid monthly traffic to the domain calculated as the product of CTR (click-through-rate) and search volume values of all keywords in the category that the domain ranks for learn more about how the metric is calculated in this help center article | [optional] 
**impressions_etv** | **float** | estimated traffic volume based on impressions estimated paid monthly traffic to the domain calculated as the product of CTR (click-through-rate) and impressions values of all keywords in the category that the domain ranks for learn more about how the metric is calculated in this help center article | [optional] 
**estimated_paid_traffic_cost** | **float** | estimated cost of monthly search traffic represents the estimated cost of paid monthly traffic (USD) based on etv and cpc values of all keywords in the category that the domain ranks for learn more about how the metric is calculated in this help center article | [optional] 
**rank_changes** | [**RankChanges**](RankChanges.md) |  | [optional] 
**backlinks_info** | [**BacklinksInfo**](BacklinksInfo.md) |  | [optional] 
**rank_info** | [**RankInfo**](RankInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.organic_dataforseo_labs_serp_element_item import OrganicDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrganicDataforseoLabsSerpElementItem from a JSON string
organic_dataforseo_labs_serp_element_item_instance = OrganicDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print OrganicDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
organic_dataforseo_labs_serp_element_item_dict = organic_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of OrganicDataforseoLabsSerpElementItem from a dict
organic_dataforseo_labs_serp_element_item_form_dict = organic_dataforseo_labs_serp_element_item.from_dict(organic_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


