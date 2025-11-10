# SerpApiKnowledgeGraphAiOverviewItemElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**asynchronous_ai_overview** | **StrictBool** | indicates whether the element is loaded asynchronously<br>if true, the ai_overview element is loaded asynchronously;<br>if false, the ai_overview element is loaded from cache; |[optional]|
**items** | **List[Optional[BaseSerpApiAiOverviewElementItem]]** | contains results featured in the ‘hotels_pack’ element of SERP |[optional]|
**references** | **List[Optional[AiModeAiOverviewReferenceInfo]]** | additional references relevant to the item<br>includes references to webpages that may have been used to generate the ai_overview |[optional]|