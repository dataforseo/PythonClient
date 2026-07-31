# ContentAnalysisPhraseTrendsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**date** | **StrictStr** | <em>date for which the data is provided</em> |[optional]|
**total_count** | **StrictInt** | <em>total number of results in our database relevant to your request</em> |[optional]|
**rank** | **StrictInt** | <em>rank of all URLs citing the <code>keyword</code></em><br>normalized sum of ranks of all URLs citing the target <code>keyword</code> for the given date |[optional]|
**top_domains** | **List[Optional[TopDomainInfo]]** | <em>top domains citing the target keyword</em><br>contains objects with top domains citing the target keyword and citation count per each domain |[optional]|
**sentiment_connotations** | **Dict[str, Optional[StrictInt]]** | <em>sentiment connotations</em><br>contains sentiments (emotional reactions) related to the target keyword citation and the number of citations per each sentiment<br>possible connotations: <code>'anger'</code>, <code>'happiness'</code>, <code>'love'</code>, <code>'sadness'</code>, <code>'share'</code>, <code>'fun'</code> |[optional]|
**connotation_types** | **Dict[str, Optional[StrictInt]]** | <em>connotation types</em><br>contains types of sentiments (sentiment polarity) related to the keyword citation and citation count per each sentiment type<br>possible connotation types: <code>'positive'</code>, <code>'negative'</code>, <code>'neutral'</code> |[optional]|
**text_categories** | **List[Optional[ContentAnalysisCategoriesInfo]]** | <em>text categories</em><br>contains objects with text categories and citation count in each text category<br>to obtain a full list of available categories, refer to the <a href='/v3/content_analysis/categories/' rel='noopener noreferrer' target='_blank'>Categories</a> endpoint |[optional]|
**page_categories** | **List[Optional[ContentAnalysisCategoriesInfo]]** | <em>page categories</em><br>contains objects with page categories and citation count in each page category<br>to obtain a full list of available categories, refer to the <a href='/v3/content_analysis/categories/' rel='noopener noreferrer' target='_blank'>Categories</a> endpoint |[optional]|
**page_types** | **Dict[str, Optional[StrictInt]]** | <em>page types</em><br>contains page types and citation count per each page type |[optional]|
**countries** | **Dict[str, Optional[StrictInt]]** | <em>countries</em><br>contains countries and citation count in each country<br>to obtain a full list of available countries, refer to the <a href='/v3/content_analysis/locations/' rel='noopener noreferrer' target='_blank'>Locations</a> endpoint |[optional]|
**languages** | **Dict[str, Optional[StrictInt]]** | <em>languages</em><br>contains languages and citation count in each language<br>to obtain a full list of available languages, refer to the <a href='/v3/content_analysis/languages/' rel='noopener noreferrer' target='_blank'>Languages</a> endpoint |[optional]|