# AiOptimizationPerplexityLlmResponsesLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**model_name** | **StrictStr** | <em>name of the AI model used</em> |[optional]|
**input_tokens** | **StrictInt** | <em>number of tokens in the input</em><br>total count of tokens processed |[optional]|
**output_tokens** | **StrictInt** | <em>number of tokens in the output</em><br>total count of tokens generated in the AI response |[optional]|
**reasoning_tokens** | **StrictInt** |  |[optional]|
**web_search** | **StrictBool** | <em>indicates if web search was used</em><br><strong>Note:</strong> web search is enabled by default in Perplexity Sonar models |[optional]|
**money_spent** | **StrictFloat** | <em>cost of AI tokens, USD</em><br>the price charged by the third-party AI model provider for according to its <a href='https://docs.perplexity.ai/guides/pricing' target='_blank'>Pricing</a> |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**items** | **List[Optional[MessageAiOptimizationLlmResponseElementItem]]** | <em>array of response items</em><br>contains structured AI response data |[optional]|
**fan_out_queries** | **Any** | <em>array of fan-out queries</em><br>contains related search queries derived from the main query to provide a more comprehensive response |[optional]|