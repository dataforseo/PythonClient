# RankInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_rank** | **int** | page rank page_rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm; learn more about the metric and how it is calculated in this help center article | [optional] 
**main_domain_rank** | **int** | main domain rank main_domain_rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm learn more about the metric and how it is calculated in this help center article | [optional] 

## Example

```python
from dataforseo_client.models.rank_info import RankInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RankInfo from a JSON string
rank_info_instance = RankInfo.from_json(json)
# print the JSON string representation of the object
print RankInfo.to_json()

# convert the object into a dict
rank_info_dict = rank_info_instance.to_dict()
# create an instance of RankInfo from a dict
rank_info_form_dict = rank_info.from_dict(rank_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


