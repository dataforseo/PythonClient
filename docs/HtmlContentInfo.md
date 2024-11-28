# HtmlContentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plain_text_size** | **int** | total size of the text on the page measured in bytes | [optional] 
**plain_text_rate** | **float** | plaintext rate value plain_text_size to size ratio | [optional] 
**plain_text_word_count** | **float** | number of words on the page | [optional] 
**automated_readability_index** | **float** | Automated Readability Index | [optional] 
**coleman_liau_readability_index** | **float** | Coleman–Liau Index | [optional] 
**dale_chall_readability_index** | **float** | Dale–Chall Readability Index | [optional] 
**flesch_kincaid_readability_index** | **float** | Flesch–Kincaid Readability Index | [optional] 
**smog_readability_index** | **float** | SMOG Readability Index | [optional] 
**description_to_content_consistency** | **float** | consistency of the meta description tag with the page content measured from 0 to 1 | [optional] 
**title_to_content_consistency** | **float** | consistency of the meta title tag with the page content measured from 0 to 1 | [optional] 
**meta_keywords_to_content_consistency** | **float** | consistency of meta keywordstag with the page content measured from 0 to 1 | [optional] 

## Example

```python
from dataforseo_client.models.html_content_info import HtmlContentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HtmlContentInfo from a JSON string
html_content_info_instance = HtmlContentInfo.from_json(json)
# print the JSON string representation of the object
print(HtmlContentInfo.to_json())

# convert the object into a dict
html_content_info_dict = html_content_info_instance.to_dict()
# create an instance of HtmlContentInfo from a dict
html_content_info_from_dict = HtmlContentInfo.from_dict(html_content_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


