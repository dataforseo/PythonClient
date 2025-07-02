# AiModeAiOverviewExpandedComponent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | reference page title |[optional]|
**text** | **StrictStr** | text or description of the element in SERP |[optional]|
**markdown** | **StrictStr** | content of the element in markdown format<br>the text of the ai_overview formatted in the markdown markup language |[optional]|
**images** | **List[Optional[ImagesElement]]** | images of the element<br>if there are none, equals null |[optional]|
**links** | **List[Optional[AiModeLinkElement]]** | website links featured in the element |[optional]|
**references** | **List[Optional[AiModeReferences]]** | additional references relevant to the item<br>includes references to webpages that may have been used to generate the ai_overview |[optional]|