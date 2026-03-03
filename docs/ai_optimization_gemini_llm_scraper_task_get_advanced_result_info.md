# AiOptimizationGeminiLlmScraperTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | keyword received in a POST array<br>the keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character) |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**model** | **StrictStr** | indicates the model version |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**markdown** | **StrictStr** | content of the element in markdown format<br>content of the result formatted in the markdown markup language |[optional]|
**sources** | **List[Optional[SourceInfo]]** | array of sources<br>the sources the model actually cited or relied on in its final answer |[optional]|
**se_results_count** | **StrictInt** | total number of results |[optional]|
**item_types** | **List[Optional[StrictStr]]** | types of search results<br>contains types of search results (items) found in SERP.<br>possible item types:<br>gemini_text, gemini_table, gemini_images |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[BaseGeminiLlmScraperElementItem]]** | items present in the element |[optional]|