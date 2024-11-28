# KeywordProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**core_keyword** | **str** | main keyword in a group contains the main keyword in a group determined by the synonym clustering algorithm if the value is null, our database does not contain any keywords the corresponding algorithm could identify as synonymous with keyword | [optional] 
**synonym_clustering_algorithm** | **str** | the algorithm used to identify synonyms possible values: keyword_metrics – indicates the algorithm based on keyword_info parameters text_processing – indicates the text-based algorithm if the value is null, our database does not contain any keywords the corresponding algorithm could identify as synonymous with keyword | [optional] 
**keyword_difficulty** | **int** | difficulty of ranking in the first top-10 organic results for a keyword indicates the chance of getting in top-10 organic results for a keyword on a logarithmic scale from 0 to 100; calculated by analysing, among other parameters, link profiles of the first 10 pages in SERP; learn more about the metric in this help center guide | [optional] 
**detected_language** | **str** | detected language of the keyword indicates the language of the keyword as identified by our system | [optional] 
**is_another_language** | **bool** | detected language of the keyword is different from the set language if true, the language set in the request does not match the language determined by our system for a given keyword | [optional] 

## Example

```python
from dataforseo_client.models.keyword_properties import KeywordProperties

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordProperties from a JSON string
keyword_properties_instance = KeywordProperties.from_json(json)
# print the JSON string representation of the object
print(KeywordProperties.to_json())

# convert the object into a dict
keyword_properties_dict = keyword_properties_instance.to_dict()
# create an instance of KeywordProperties from a dict
keyword_properties_from_dict = KeywordProperties.from_dict(keyword_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


