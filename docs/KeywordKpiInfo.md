# KeywordKpiInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_position** | **str** | represents the position of the relevant ad in SERP can take the following values: FirstPage1: The first ad to appear on the right side of the first search results page FirstPage2: The second ad to appear on the right side of the first search results page FirstPage3: The third ad to appear on the right side of the first search results page FirstPage4: The fourth ad to appear on the right side of the first search results page FirstPage5: The fifth ad to appear on the right side of the first search results page FirstPage6: The sixth ad to appear on the right side of the first search results page FirstPage7: The seventh ad to appear on the right side of the first search results page FirstPage8: The eighth ad to appear on the right side of the first search results page FirstPage9: The ninth ad to appear on the right side of the first search results page FirstPage10: The tenth ad to appear on the right side of the first search results page MainLine1: The first ad to appear at the top of the search results page MainLine2: The second ad to appear at the top of the search results page MainLine3: The third ad to appear at the top of the search results page MainLine4: The fourth ad to appear at the top of the search results page | [optional] 
**clicks** | **int** | ad clicks the number of clicks that the keyword and match type generated during the last month | [optional] 
**impressions** | **int** | ad impressions the number of impressions that the keyword and match type generated during the last month | [optional] 
**average_cpc** | **float** | average cost per click, USD calculated by dividing the cost of all clicks by the number of clicks | [optional] 
**ctr** | **float** | click-through rate as a percentage calculated by dividing the number of clicks by the number of impressions and multiplying the result by 100 | [optional] 
**total_cost** | **int** | total cost of an ad, USD the cost of using the specified keyword and match type during the last month | [optional] 
**average_bid** | **float** | average bid of the keyword | [optional] 

## Example

```python
from dataforseo_client.models.keyword_kpi_info import KeywordKpiInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordKpiInfo from a JSON string
keyword_kpi_info_instance = KeywordKpiInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordKpiInfo.to_json())

# convert the object into a dict
keyword_kpi_info_dict = keyword_kpi_info_instance.to_dict()
# create an instance of KeywordKpiInfo from a dict
keyword_kpi_info_from_dict = KeywordKpiInfo.from_dict(keyword_kpi_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


