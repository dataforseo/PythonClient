# SerpApiAiModeAiOverviewElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | <em>title of the element</em> |[optional]|
**text** | **StrictStr** | <em>text or description of the element in SERP</em> |[optional]|
**markdown** | **StrictStr** | <em>content of the element in markdown format</em> |[optional]|
**links** | **List[Optional[AiModeLinkElementInfo]]** | <em>website links featured in the element</em><br>if there are none, equals <code>null</code> |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | <em>images of the element</em><br>if there are none, equals <code>null</code> |[optional]|
**references** | **List[Optional[AiModeAiOverviewReferenceInfo]]** | <em>references relevant to the element</em><br>includes references to webpages that were used to generate the <code>ai_overview_element</code> |[optional]|