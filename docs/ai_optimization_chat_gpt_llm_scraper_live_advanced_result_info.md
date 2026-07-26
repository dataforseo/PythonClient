# AiOptimizationChatGptLlmScraperLiveAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | <em>keyword received in a POST array<br></em><strong>the keyword is returned with decoded %## (plus symbol '+' will be decoded to a space character)</strong> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**model** | **StrictStr** | <em>indicates the model version</em> |[optional]|
**check_url** | **StrictStr** | <em>direct URL to search engine results<br></em>you can use it to make sure that we provided exact results |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**markdown** | **StrictStr** | <em>content of the element in markdown format</em><br>content of the result formatted in the <a href='https://en.wikipedia.org/wiki/Markdown' target='_blank'>markdown markup language</a> |[optional]|
**search_results** | **List[Optional[ChatgptSearchResult]]** | <em>array of search results</em><br>all web search outputs the model retrieved when looking up information, including duplicates and unused entries |[optional]|
**sources** | **List[Optional[SourceInfo]]** | <em>array of sources</em><br>the sources the model actually cited or relied on in its final answer |[optional]|
**fan_out_queries** | **List[Optional[StrictStr]]** | <em>array of fan-out queries</em><br>contains related search queries derived from the main query to provide a more comprehensive response |[optional]|
**brand_entities** | **List[Optional[ChatGptBrandEntity]]** | <em>array of brand entities</em><br>contains information on brands mentioned in the response |[optional]|
**se_results_count** | **StrictInt** | <em> total number of results</em> |[optional]|
**item_types** | **List[Optional[StrictStr]]** | <em>types of search results</em><br>contains types of search results (<code>items</code>) found in SERP.<br>possible item types:<br><code>chat_gpt_text</code>, <code>chat_gpt_table</code>, <code>chat_gpt_navigation_list</code>, <code>chat_gpt_images</code>, <code>chat_gpt_local_businesses</code>, <code>chat_gpt_products</code> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <strong><code>items</code></strong> array</em> |[optional]|
**items** | **List[Optional[BaseChatGptLlmScraperElementItem]]** | <em>elements of ChatGPT results</em> |[optional]|