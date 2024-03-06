[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ContentAnalysisCategoryTrendsLiveResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**var_date** | **str** | date for which the data is provided | [optional]
**total_count** | **int** | total number of results in our database relevant to your request | [optional]
**rank** | **int** | rank of all URLs citing the keyword normalized sum of ranks of all URLs citing the target keyword for the given date | [optional]
**top_domains** | [**List[TopDomainInfo]**](TopDomainInfo.md) | top domains citing the target keyword contains objects with top domains citing the target category and citation count per each domain | [optional]
**sentiment_connotations** | **Dict[str, Optional[int]]** | sentiment connotations contains sentiments (emotional reactions) related to the target category citation and the number of citations per each sentiment possible connotations: \&quot;anger\&quot;, \&quot;fear\&quot;, \&quot;happiness\&quot;, \&quot;love\&quot;, \&quot;sadness\&quot;, \&quot;share\&quot;, \&quot;neutral\&quot;, \&quot;fun\&quot; | [optional]
**connotation_types** | **Dict[str, Optional[int]]** | connotation types contains types of sentiments (sentiment polarity) related to the category citation and citation count per each sentiment type possible connotation types: \&quot;positive\&quot;, \&quot;negative\&quot;, \&quot;neutral\&quot; | [optional]
**text_categories** | [**List[ContentAnalysisCategoriesInfo]**](ContentAnalysisCategoriesInfo.md) | text categories contains objects with text categories and citation count in each text category to obtain a full list of available categories, refer to the Categories endpoint | [optional]
**page_categories** | [**List[ContentAnalysisCategoriesInfo]**](ContentAnalysisCategoriesInfo.md) | page categories contains objects with page categories and citation count in each page category to obtain a full list of available categories, refer to the Categories endpoint | [optional]
**page_types** | **Dict[str, Optional[int]]** | page types contains page types and citation count per each page type | [optional]
**countries** | **Dict[str, Optional[int]]** | countries contains countries and citation count in each country to obtain a full list of available countries, refer to the Locations endpoint | [optional]
**languages** | **Dict[str, Optional[int]]** | languages contains languages and citation count in each language to obtain a full list of available languages, refer to the Languages endpoint | [optional]

## Example

```python
from dataforseo_client.models.content_analysis_category_trends_live_result_info import ContentAnalysisCategoryTrendsLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAnalysisCategoryTrendsLiveResultInfo from a JSON string
content_analysis_category_trends_live_result_info_instance = ContentAnalysisCategoryTrendsLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print ContentAnalysisCategoryTrendsLiveResultInfo.to_json()

# convert the object into a dict
content_analysis_category_trends_live_result_info_dict = content_analysis_category_trends_live_result_info_instance.to_dict()
# create an instance of ContentAnalysisCategoryTrendsLiveResultInfo from a dict
content_analysis_category_trends_live_result_info_form_dict = content_analysis_category_trends_live_result_info.from_dict(content_analysis_category_trends_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")