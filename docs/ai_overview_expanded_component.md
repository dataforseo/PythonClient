# AiOverviewExpandedComponent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | <em>reference page title</em> |[optional]|
**text** | **StrictStr** | <em>reference text</em><br>text snippet from the page that was used to generate the <code>ai_overview_element</code> |[optional]|
**markdown** | **StrictStr** | <em>content of the element in markdown format</em> |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | <em>images of the element</em><br>if there is none, equals <code>null</code> |[optional]|
**links** | **List[Optional[LinkElement]]** | <em>sitelinks</em><br>the links shown below some of Google's search results<br>if there are none, equals <code>null</code> |[optional]|
**references** | **List[Optional[AiModeAiOverviewReferenceInfo]]** | <em>references relevant to the element</em><br>includes references to webpages that were used to generate the <code>ai_overview_element</code> |[optional]|