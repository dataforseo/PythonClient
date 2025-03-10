# AvgBacklinksInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**backlinks** | **float** | average number of backlinks | [optional] 
**dofollow** | **float** | average number of dofollow links | [optional] 
**referring_pages** | **float** | average number of referring pages | [optional] 
**referring_domains** | **float** | average number of referring domains | [optional] 
**referring_main_domains** | **float** | average number of referring main domains | [optional] 
**rank** | **float** | average rank learn more about the metric and its calculation formula in this help center article | [optional] 
**main_domain_rank** | **float** | average main domain rank learn more about the metric and its calculation formula in this help center article | [optional] 
**last_updated_time** | **str** | date and time when SERP data was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 

## Example

```python
from dataforseo_client.models.avg_backlinks_info import AvgBacklinksInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AvgBacklinksInfo from a JSON string
avg_backlinks_info_instance = AvgBacklinksInfo.from_json(json)
# print the JSON string representation of the object
print(AvgBacklinksInfo.to_json())

# convert the object into a dict
avg_backlinks_info_dict = avg_backlinks_info_instance.to_dict()
# create an instance of AvgBacklinksInfo from a dict
avg_backlinks_info_from_dict = AvgBacklinksInfo.from_dict(avg_backlinks_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


