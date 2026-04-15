# LlmMessageSectionInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**text** | **StrictStr** | AI-generated text content |[optional]|
**annotations** | **List[Optional[AnnotationInfo]]** | array of references used to generate the responseequals null if the web_search parameter is not set to trueNote: annotations may return empty even when web_search is true, as the AI will attempt to retrieve web information but may not find relevant results |[optional]|