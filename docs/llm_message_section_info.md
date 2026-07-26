# LlmMessageSectionInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**text** | **StrictStr** | <em>text of the reasoning chain section</em><br>text of the reasoning chain  section summarizing the model's thought process |[optional]|
**annotations** | **List[Optional[AnnotationInfo]]** | <em>array of references used to generate the response</em><br>equals <code>null</code> if the <code>web_search</code> parameter is not set to <code>true</code><br><strong>Note:</strong> <code>annotations</code> may return empty even when <code>web_search</code> is <code>true</code>, as the AI will attempt to retrieve web information but may not find relevant results |[optional]|