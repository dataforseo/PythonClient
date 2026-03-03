# SerpApiAiModeAiOverviewElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of the element |[optional]|
**text** | **StrictStr** | text or description of the element in SERP |[optional]|
**markdown** | **StrictStr** | content of the element in markdown format |[optional]|
**links** | **List[Optional[AiModeLinkElementInfo]]** | website links featured in the elementif there are none, equals null |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | images of the elementif there are none, equals null |[optional]|
**references** | **List[Optional[AiModeAiOverviewReferenceInfo]]** | references relevant to the elementincludes references to webpages that were used to generate the ai_overview_element |[optional]|