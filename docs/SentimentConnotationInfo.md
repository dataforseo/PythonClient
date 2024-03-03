# SentimentConnotationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anger** | **float** | anger | [optional] 
**happiness** | **float** | happiness | [optional] 
**love** | **float** | love | [optional] 
**sadness** | **float** | sadness | [optional] 
**share** | **float** | share | [optional] 
**fun** | **float** | fun | [optional] 

## Example

```python
from dataforseo_client.models.sentiment_connotation_info import SentimentConnotationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SentimentConnotationInfo from a JSON string
sentiment_connotation_info_instance = SentimentConnotationInfo.from_json(json)
# print the JSON string representation of the object
print SentimentConnotationInfo.to_json()

# convert the object into a dict
sentiment_connotation_info_dict = sentiment_connotation_info_instance.to_dict()
# create an instance of SentimentConnotationInfo from a dict
sentiment_connotation_info_form_dict = sentiment_connotation_info.from_dict(sentiment_connotation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


