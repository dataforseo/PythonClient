# AiOptimizationChatGptLlmScraperTaskGetAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | keyword received in a POST array<br>the keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character) |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**model** | **StrictStr** | indicates the model version |[optional]|
**check_url** | **StrictStr** | direct URL to search engine results<br>you can use it to make sure that we provided exact results |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**markdown** | **StrictStr** | content of the element in markdown format<br>content of the result formatted in the markdown markup language |[optional]|
**search_results** | **List[Optional[ChatgptSearchResult]]** | array of search results<br>all web search outputs the model retrieved when looking up information, including duplicates and unused entries |[optional]|
**sources** | **List[Optional[ChatGptSource]]** | array of sources<br>the sources the model actually cited or relied on in its final answer |[optional]|
**fan_out_queries** | **List[Optional[StrictStr]]** | array of fan-out queries<br>contains related search queries derived from the main query to provide a more comprehensive response |[optional]|
**brand_entities** | **List[Optional[ChatGptBrandEntity]]** | array of brand entities<br>contains information on brands mentioned in the response |[optional]|
**se_results_count** | **StrictInt** | total number of results |[optional]|
**item_types** | **List[Optional[StrictStr]]** | types of search results<br>contains types of search results (items) found.<br>possible item types:<br>chat_gpt_text, chat_gpt_table, chat_gpt_navigation_list, chat_gpt_images, chat_gpt_local_businesses, chat_gpt_products |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[BaseChatGptLlmScraperElementItem]]** | items present in the element |[optional]|