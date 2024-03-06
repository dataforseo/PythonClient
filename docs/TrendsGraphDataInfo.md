[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# TrendsGraphDataInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **str** | start date of the corresponding time range in the UTC format: “yyyy-mm-dd” | [optional]
**date_to** | **str** | end date of the corresponding time range in the UTC format: “yyyy-mm-dd” | [optional]
**timestamp** | **int** | a point in time in the Unix time format | [optional]
**missing_data** | **bool** | indicates whether the data is unavailable if true the data on the graph in the Google Trends interface is missing and thus labelled with a dotted line | [optional]
**values** | **List[Optional[int]]** | relative keyword popularity rate at a specific timestamp represents the keyword popularity rate over the given time range if you specify more than one keyword, the values will be averaged to the highest value across all specified keywords a value of 100 is the peak popularity for the term. A value of 50 means that the term is half as popular. A score of 0 means there was not enough data for this term | [optional]

## Example

```python
from dataforseo_client.models.trends_graph_data_info import TrendsGraphDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TrendsGraphDataInfo from a JSON string
trends_graph_data_info_instance = TrendsGraphDataInfo.from_json(json)
# print the JSON string representation of the object
print TrendsGraphDataInfo.to_json()

# convert the object into a dict
trends_graph_data_info_dict = trends_graph_data_info_instance.to_dict()
# create an instance of TrendsGraphDataInfo from a dict
trends_graph_data_info_form_dict = trends_graph_data_info.from_dict(trends_graph_data_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")