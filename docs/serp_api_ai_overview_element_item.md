# SerpApiAiOverviewElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of a given link element |[optional]|
**text** | **StrictStr** | reference text<br>text snippet from the page that was used to generate the ai_overview_element |[optional]|
**markdown** | **StrictStr** | text of the component in the markdwon format |[optional]|
**links** | **List[Optional[LinkElement]]** | sitelinks<br>the links shown below some of Google’s search results<br>if there are none, equals null |[optional]|
**images** | **List[Optional[AiModeImagesElement]]** | images of the element<br>if there are none, equals null |[optional]|
**references** | **List[Optional[AiAiOverviewReferenceInfo]]** | additional references relevant to the item<br>includes references to webpages that may have been used to generate the product_considerations_ai_overview_expanded_element |[optional]|