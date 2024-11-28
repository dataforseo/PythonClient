# SentimentConnotationDistribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anger** | [**ContentAnalysisSummaryInfo**](ContentAnalysisSummaryInfo.md) |  | [optional] 
**happiness** | [**ContentAnalysisSummaryInfo**](ContentAnalysisSummaryInfo.md) |  | [optional] 
**love** | [**ContentAnalysisSummaryInfo**](ContentAnalysisSummaryInfo.md) |  | [optional] 
**sadness** | [**ContentAnalysisSummaryInfo**](ContentAnalysisSummaryInfo.md) |  | [optional] 
**share** | [**ContentAnalysisSummaryInfo**](ContentAnalysisSummaryInfo.md) |  | [optional] 
**fun** | [**ContentAnalysisSummaryInfo**](ContentAnalysisSummaryInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.sentiment_connotation_distribution import SentimentConnotationDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of SentimentConnotationDistribution from a JSON string
sentiment_connotation_distribution_instance = SentimentConnotationDistribution.from_json(json)
# print the JSON string representation of the object
print(SentimentConnotationDistribution.to_json())

# convert the object into a dict
sentiment_connotation_distribution_dict = sentiment_connotation_distribution_instance.to_dict()
# create an instance of SentimentConnotationDistribution from a dict
sentiment_connotation_distribution_from_dict = SentimentConnotationDistribution.from_dict(sentiment_connotation_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


