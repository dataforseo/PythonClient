# ChatGptTableElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**text** | **StrictStr** | <em>text of the element</em> |[optional]|
**markdown** | **StrictStr** | <em>content of the element in markdown format</em><br>content of the result formatted in the <a href='https://en.wikipedia.org/wiki/Markdown' target='_blank'>markdown markup language</a> |[optional]|
**table** | **Table** | <em>table present in the element</em><br>the header and content of the table present in the element |[optional]|
**brand_entities** | **List[Optional[ChatGptBrandEntity]]** | <em>array of brand entities</em><br>contains information on brands mentioned in the text |[optional]|