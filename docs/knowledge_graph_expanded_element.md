# KnowledgeGraphExpandedElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**featured_title** | **StrictStr** | <em>title of a given element</em> |[optional]|
**url** | **StrictStr** | <em>relevant URL </em> |[optional]|
**domain** | **StrictStr** | <em>domain where a link points</em> |[optional]|
**title** | **StrictStr** | <em>title of the result in SERP</em> |[optional]|
**snippet** | **StrictStr** | <em>text alongside the link title</em> |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | <em>images of the element</em><br>if there are none, equals <code>null</code> |[optional]|
**timestamp** | **StrictStr** | <em>date and time when the result was published</em><br>in the UTC format: 'yyyy-mm-dd hh-mm-ss +00:00'<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**table** | **Table** | <em>table present in the element</em><br>the header and content of the table present in the element |[optional]|