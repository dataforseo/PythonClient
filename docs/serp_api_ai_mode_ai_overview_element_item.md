# SerpApiAiModeAiOverviewElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of the element |[optional]|
**text** | **StrictStr** | text or description of the element in SERP |[optional]|
**markdown** | **StrictStr** | content of the element in markdown format |[optional]|
**links** | **List[Optional[InformationAndTicketsElement]]** | website links featured in the element |[optional]|
**images** | **List[Optional[AiModeImagesElement]]** | images of the element<br>if there are none, equals null |[optional]|
**references** | **List[Optional[AiAiOverviewReferenceInfo]]** | references relevant to the element<br>includes references to webpages that were used to generate the ai_overview_element |[optional]|