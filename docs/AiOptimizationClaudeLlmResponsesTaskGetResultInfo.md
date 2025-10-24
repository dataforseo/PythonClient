# AiOptimizationClaudeLlmResponsesTaskGetResultInfo

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**model_name** | **string** | name of the AI model used |[optional]|
**input_tokens** | **number** | number of tokens in the input<br>total count of tokens processed |[optional]|
**output_tokens** | **number** | number of tokens in the output<br>total count of tokens generated in the AI response |[optional]|
**web_search** | **boolean** | indicates if web search was used |[optional]|
**money_spent** | **number** | cost of AI tokens, USD<br>the price charged by the third-party AI model provider for according to its Pricing |[optional]|
**datetime** | **string** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**items** | **AiOptimizationItem[]** | array of response items<br>contains structured AI response data |[optional]|