# AiOptimizationGeminiLlmScraperTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | <em>keyword received in a POST array<br></em><strong>the keyword is returned with decoded %## (plus symbol '+' will be decoded to a space character)</strong> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**model** | **StrictStr** | <em>indicates the model version</em> |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**markdown** | **StrictStr** | <em>content of the element in markdown format</em><br>content of the result formatted in the <a href='https://en.wikipedia.org/wiki/Markdown' target='_blank'>markdown markup language</a> |[optional]|
**sources** | **List[Optional[SourceInfo]]** | <em>array of sources</em><br>the sources the model actually cited or relied on in its final answer |[optional]|
**se_results_count** | **StrictInt** | <em> total number of results</em> |[optional]|
**item_types** | **List[Optional[StrictStr]]** | <em>types of search results</em><br>contains types of search results (<code>items</code>) found in SERP.<br>possible item types:<br><code>gemini_text</code>, <code>gemini_table</code>, <code>gemini_images</code> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <strong><code>items</code></strong> array</em> |[optional]|
**items** | **List[Optional[BaseGeminiLlmScraperElementItem]]** | <em>items present in the element</em> |[optional]|