[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ContentAnalysisSentimentAnalysisLiveResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**positive_connotation_distribution** | [**PositiveConnotationDistribution**](PositiveConnotationDistribution.md) |  | [optional]
**sentiment_connotation_distribution** | [**SentimentConnotationDistribution**](SentimentConnotationDistribution.md) |  | [optional]

## Example

```python
from dataforseo_client.models.content_analysis_sentiment_analysis_live_result_info import ContentAnalysisSentimentAnalysisLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAnalysisSentimentAnalysisLiveResultInfo from a JSON string
content_analysis_sentiment_analysis_live_result_info_instance = ContentAnalysisSentimentAnalysisLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print ContentAnalysisSentimentAnalysisLiveResultInfo.to_json()

# convert the object into a dict
content_analysis_sentiment_analysis_live_result_info_dict = content_analysis_sentiment_analysis_live_result_info_instance.to_dict()
# create an instance of ContentAnalysisSentimentAnalysisLiveResultInfo from a dict
content_analysis_sentiment_analysis_live_result_info_form_dict = content_analysis_sentiment_analysis_live_result_info.from_dict(content_analysis_sentiment_analysis_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")