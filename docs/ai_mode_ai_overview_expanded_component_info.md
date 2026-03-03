# AiModeAiOverviewExpandedComponentInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | reference page title |[optional]|
**text** | **StrictStr** | additional text of the element in SERP |[optional]|
**markdown** | **StrictStr** | content of the element in markdown format |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | images of the componentif there are none, equals null |[optional]|
**links** | **List[Optional[AiModeLinkElementInfo]]** | sitelinksthe links shown below some of Google's search resultsif there are none, equals null |[optional]|
**references** | **List[Optional[AiModeAiOverviewReferenceInfo]]** | references relevant to the elementincludes references to webpages that were used to generate the ai_overview_element |[optional]|