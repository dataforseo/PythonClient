# KeywordIntentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | search intent name possible values: informational, navigational, commercial, transactional | [optional] 
**probability** | **float** | search intent probability 1 indicates the highest probability | [optional] 

## Example

```python
from dataforseo_client.models.keyword_intent_info import KeywordIntentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordIntentInfo from a JSON string
keyword_intent_info_instance = KeywordIntentInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordIntentInfo.to_json())

# convert the object into a dict
keyword_intent_info_dict = keyword_intent_info_instance.to_dict()
# create an instance of KeywordIntentInfo from a dict
keyword_intent_info_form_dict = keyword_intent_info.from_dict(keyword_intent_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


