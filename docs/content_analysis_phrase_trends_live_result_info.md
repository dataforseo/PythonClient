# ContentAnalysisPhraseTrendsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**date** | **StrictStr** | date for which the data is provided |[optional]|
**total_count** | **StrictFloat** | total number of results in our database relevant to your request |[optional]|
**rank** | **StrictFloat** | rank of all URLs citing the keyword<br>normalized sum of ranks of all URLs citing the target keyword for the given date |[optional]|
**top_domains** | **List[Optional[TopDomainCountInfo]]** | top domains citing the target keyword<br>contains objects with top domains citing the target keyword and citation count per each domain |[optional]|
**sentiment_connotations** | **Dict[str, Optional[StrictInt]]** | sentiment connotations<br>contains sentiments (emotional reactions) related to the target keyword citation and the number of citations per each sentiment<br>possible connotations: 'anger', 'happiness', 'love', 'sadness', 'share', 'fun' |[optional]|
**connotation_types** | **Dict[str, Optional[StrictInt]]** | connotation types<br>contains types of sentiments (sentiment polarity) related to the keyword citation and citation count per each sentiment type<br>possible connotation types: 'positive', 'negative', 'neutral' |[optional]|
**text_categories** | **List[Optional[ContentAnalysisCategoriesInfo]]** | text categories<br>contains objects with text categories and citation count in each text category<br>to obtain a full list of available categories, refer to the Categories endpoint |[optional]|
**page_categories** | **List[Optional[ContentAnalysisCategoriesInfo]]** | page categories<br>contains objects with page categories and citation count in each page category<br>to obtain a full list of available categories, refer to the Categories endpoint |[optional]|
**page_types** | **Dict[str, Optional[StrictInt]]** | page types<br>contains page types and citation count per each page type |[optional]|
**countries** | **Dict[str, Optional[StrictInt]]** | countries<br>contains countries and citation count in each country<br>to obtain a full list of available countries, refer to the Locations endpoint |[optional]|
**languages** | **Dict[str, Optional[StrictInt]]** | languages<br>contains languages and citation count in each language<br>to obtain a full list of available languages, refer to the Languages endpoint |[optional]|