# AiModeAiOverviewElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**position** | **StrictStr** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**title** | **StrictStr** | title of the element |[optional]|
**text** | **StrictStr** | text or description of the element in SERP |[optional]|
**markdown** | **StrictStr** | content of the element in markdown format |[optional]|
**links** | **List[Optional[AiModeLinkElement]]** | website links featured in the element |[optional]|
**images** | **List[Optional[ImagesElement]]** | images of the element<br>if there are none, equals null |[optional]|
**references** | **List[Optional[AiModeAiOverviewReference]]** | references relevant to the element<br>includes references to webpages that were used to generate the ai_overview_element |[optional]|