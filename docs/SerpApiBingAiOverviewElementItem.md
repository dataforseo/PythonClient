# SerpApiBingAiOverviewElementItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**position** | **string** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**title** | **string** | title of the result in SERP |[optional]|
**text** | **string** | text or description of the element in SERP |[optional]|
**markdown** | **string** | content of the element in markdown format |[optional]|
**links** | **LinkElement[]** | sitelinks<br>the links shown below some search results<br>if there are none, equals null |[optional]|
**images** | **AiModeImagesElementInfo[]** | images of the element |[optional]|
**references** | **AiModeAiOverviewReferenceInfo[]** | references relevant to the element<br>includes references to webpages that were used to generate the ai_overview_element |[optional]|