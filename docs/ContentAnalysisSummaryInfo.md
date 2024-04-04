# ContentAnalysisSummaryInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**total_count** | **int** | total amount of results in our database relevant to your request | [optional] 
**rank** | **int** | rank of all URLs citing the keyword normalized sum of ranks of all URLs citing the target keyword | [optional] 
**top_domains** | [**List[TopDomainInfo]**](TopDomainInfo.md) | top domains citing the target keyword contains objects with top domains citing the target keword and citation count per each domain | [optional] 
**sentiment_connotations** | **Dict[str, Optional[int]]** | sentiment connotations contains sentiments (emotional reactions) related to the target keyword citation and the number of citations per each sentiment possible sentiment connotations: anger, happiness, love, sadness, share, fun | [optional] 
**connotation_types** | **Dict[str, Optional[int]]** | connotation types contains types of sentiments (sentiment polarity) related to the keyword citation and citation count per each sentiment type possible sentiment connotation types: positive, negative, neutral | [optional] 
**text_categories** | [**List[ContentAnalysisCategoriesInfo]**](ContentAnalysisCategoriesInfo.md) | text categories contains objects with text categories and citation count in each text category to obtain a full list of available categories, refer to the Categories endpoint | [optional] 
**page_categories** | [**List[ContentAnalysisCategoriesInfo]**](ContentAnalysisCategoriesInfo.md) | page categories contains objects with page categories and citation count in each page category to obtain a full list of available categories, refer to the Categories endpoint | [optional] 
**page_types** | **Dict[str, Optional[int]]** | page types contains page types and citation count per each page type | [optional] 
**countries** | **Dict[str, Optional[int]]** | countries contains countries and citation count in each country to obtain a full list of available countries, refer to the Locations endpoint | [optional] 
**languages** | **Dict[str, Optional[int]]** | languages contains languages and citation count in each language to obtain a full list of available languages, refer to the Languages endpoint | [optional] 

## Example

```python
from dataforseo_client.models.content_analysis_summary_info import ContentAnalysisSummaryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAnalysisSummaryInfo from a JSON string
content_analysis_summary_info_instance = ContentAnalysisSummaryInfo.from_json(json)
# print the JSON string representation of the object
print ContentAnalysisSummaryInfo.to_json()

# convert the object into a dict
content_analysis_summary_info_dict = content_analysis_summary_info_instance.to_dict()
# create an instance of ContentAnalysisSummaryInfo from a dict
content_analysis_summary_info_form_dict = content_analysis_summary_info.from_dict(content_analysis_summary_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


