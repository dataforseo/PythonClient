# AiOverviewExpandedComponent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | title of the element |[optional]|
**text** | **StrictStr** | reference text<br>text snippet from the page that was used to generate the ai_overview_element |[optional]|
**markdown** | **StrictStr** | content of the element in markdown format |[optional]|
**images** | **List[Optional[AiModeImagesElement]]** | images of the element |[optional]|
**links** | **List[Optional[LinkElement]]** | website links featured in the element |[optional]|
**references** | **List[Optional[AiAiOverviewReferenceInfo]]** | references relevant to the element<br>includes references to webpages that were used to generate the ai_overview_element |[optional]|