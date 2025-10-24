# AiModeAiOverviewExpandedComponentInfo

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**title** | **string** | reference page title |[optional]|
**text** | **string** | additional text of the element in SERP |[optional]|
**markdown** | **string** | content of the element in markdown format |[optional]|
**images** | **AiModeImagesElementInfo[]** | images of the component<br>if there are none, equals null |[optional]|
**links** | **AiModeLinkElementInfo[]** | sitelinks<br>the links shown below some of Google’s search results<br>if there are none, equals null |[optional]|
**references** | **AiModeAiOverviewReferenceInfo[]** | references relevant to the element<br>includes references to webpages that were used to generate the ai_overview_element |[optional]|