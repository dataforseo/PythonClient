# SerpApiAiModeAiOverviewElementItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **string** | title of the element |[optional]|
**text** | **string** | text or description of the element in SERP |[optional]|
**markdown** | **string** | content of the element in markdown format |[optional]|
**links** | **AiModeLinkElementInfo[]** | website links featured in the element |[optional]|
**images** | **AiModeImagesElementInfo[]** | images of the element<br>if there are none, equals null |[optional]|
**references** | **AiModeAiOverviewReferenceInfo[]** | references relevant to the element<br>includes references to webpages that were used to generate the ai_overview_element |[optional]|