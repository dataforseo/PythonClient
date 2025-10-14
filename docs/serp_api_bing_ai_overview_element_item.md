# SerpApiBingAiOverviewElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**position** | **StrictStr** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**text** | **StrictStr** | text or description of the element in SERP |[optional]|
**markdown** | **StrictStr** | content of the element in markdown format |[optional]|
**links** | **List[Optional[LinkElement]]** | sitelinks<br>the links shown below some search results<br>if there are none, equals null |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | images of the element |[optional]|
**references** | **List[Optional[AiModeAiOverviewReferenceInfo]]** | references relevant to the element<br>includes references to webpages that were used to generate the ai_overview_element |[optional]|