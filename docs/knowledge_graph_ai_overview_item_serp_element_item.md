# KnowledgeGraphAiOverviewItemSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**asynchronous_ai_overview** | **StrictBool** | indicates whether the element is loaded asynchronously<br>if true, the people_also_ask_ai_overview_expanded_element element is loaded asynchronously;<br>if false, the people_also_ask_ai_overview_expanded_element element is loaded from cache; |[optional]|
**items** | **List[Optional[BaseSerpApiAiOverviewElementItem]]** | contains arrays of elements available in the list |[optional]|
**references** | **List[Optional[AiModeAiOverviewReferenceInfo]]** | references relevant to the element<br>includes references to webpages that were used to generate the ai_overview_element |[optional]|