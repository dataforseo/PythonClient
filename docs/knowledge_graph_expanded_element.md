# KnowledgeGraphExpandedElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**featured_title** | **StrictStr** | title of a given element |[optional]|
**url** | **StrictStr** | relevant URL |[optional]|
**domain** | **StrictStr** | domain in SERP |[optional]|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**snippet** | **StrictStr** | text alongside the link title |[optional]|
**images** | **List[Optional[AiModeImagesElement]]** | images of the element |[optional]|
**timestamp** | **StrictStr** | date and time when the result was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**table** | **Table** | table present in the element<br>the header and content of the table present in the element |[optional]|