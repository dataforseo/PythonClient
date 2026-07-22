# AiOverviewExpandedComponent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | reference page title |[optional]|
**text** | **StrictStr** | reference text<br>text snippet from the page that was used to generate the ai_overview_element |[optional]|
**markdown** | **StrictStr** | content of the element in markdown format |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | images of the element<br>if there is none, equals null |[optional]|
**links** | **List[Optional[LinkElement]]** | sitelinks<br>the links shown below some of Google’s search results<br>if there are none, equals null |[optional]|
**references** | **List[Optional[AiModeAiOverviewReferenceInfo]]** | references relevant to the element<br>includes references to webpages that were used to generate the ai_overview_element |[optional]|