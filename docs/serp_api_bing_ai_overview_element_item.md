# SerpApiBingAiOverviewElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**position** | **StrictStr** | <em>the alignment of the element in SERP</em><br>            can take the following values:<br>            <code>left</code>, <code>right</code> |[optional]|
**title** | **StrictStr** | <em>title of the result in SERP</em> |[optional]|
**text** | **StrictStr** | <em>text or description of the element in SERP</em> |[optional]|
**markdown** | **StrictStr** | <em>content of the element in markdown format</em> |[optional]|
**links** | **List[Optional[LinkElement]]** | <em>sitelinks</em><br>            the links shown below some search results<br>            if there are none, equals <code>null</code> |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | <em>images of the element</em> |[optional]|
**references** | **List[Optional[AiModeAiOverviewReferenceInfo]]** | <em>references relevant to the element</em><br>            includes references to webpages that were used to generate the <code>ai_overview_element</code> |[optional]|