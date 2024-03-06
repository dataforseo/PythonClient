[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DataforseoLabsSerpCompetitorsLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional]
**domain** | **str** | domain name of the detected SERP competitor | [optional]
**avg_position** | **float** | the average position of the domain for the specified keywords the arithmetic mean of values in the keywords_positions array | [optional]
**median_position** | **int** | the median position of the domain for the specified keywords the median of the values in the keywords_positions array | [optional]
**rating** | **int** | the margin between the greatest possible and actual keyword positions represents the relative visibility rate of the domain in SERP for the specified keywords calculated as sum(100-keywords_positions) | [optional]
**etv** | **float** | estimated traffic volume represents the estimated monthly traffic that specified keywords are driving to the website calculated as the sum of the products of the specified keywords’ search volume values and CTR (click-through-rate) rates at certain positions in SERP learn more about how the metric is calculated in this help center article | [optional]
**keywords_count** | **int** | the number of specified keywords the domain has positions for in SERPs | [optional]
**visibility** | **float** | SERP visibility rate represents the website visibility rate based on the SERP positions of the specified keywords Keywords with positions in the range from 1 to 10 are assigned the visibility index from 1 to 0.1, respectively Keywords with positions in the range from 11 to 20 have the fixed visibility index of 0.05 keywords with positions from 20 to 100 have the visibility index equal to 0 | [optional]
**relevant_serp_items** | **int** | the number of SERP elements relevant to the domain represents the number of search results in SERP relevant to the domain for the specified keywords | [optional]
**keywords_positions** | **Dict[str, List[float]]** |  | [optional]

## Example

```python
from dataforseo_client.models.dataforseo_labs_serp_competitors_live_item import DataforseoLabsSerpCompetitorsLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsSerpCompetitorsLiveItem from a JSON string
dataforseo_labs_serp_competitors_live_item_instance = DataforseoLabsSerpCompetitorsLiveItem.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsSerpCompetitorsLiveItem.to_json()

# convert the object into a dict
dataforseo_labs_serp_competitors_live_item_dict = dataforseo_labs_serp_competitors_live_item_instance.to_dict()
# create an instance of DataforseoLabsSerpCompetitorsLiveItem from a dict
dataforseo_labs_serp_competitors_live_item_form_dict = dataforseo_labs_serp_competitors_live_item.from_dict(dataforseo_labs_serp_competitors_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")