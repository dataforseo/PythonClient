# SerpApiKnowledgeGraphAiOverviewItemElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**asynchronous_ai_overview** | **StrictBool** | <em>indicates whether the element is loaded asynchronously</em><br>if <code>true</code>, the <code>ai_overview</code> element is loaded asynchronously;<br>if <code>false</code>, the <code>ai_overview</code> element is loaded from cache;<br>to obtain the content of <code>ai_overview</code> elements, use the <code>load_async_ai_overview</code> parameter in the POST request |[optional]|
**items** | **List[Optional[BaseSerpApiAiOverviewElementItem]]** | <em>contains results featured in the 'hotels_pack' element of SERP</em> |[optional]|
**references** | **List[Optional[AiModeAiOverviewReferenceInfo]]** | <em>additional references relevant to the item</em><br>includes references to webpages that may have been used to generate the <code>ai_overview</code> |[optional]|