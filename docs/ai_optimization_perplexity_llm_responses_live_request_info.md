# AiOptimizationPerplexityLlmResponsesLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**user_prompt** | **StrictStr** | prompt for the AI modelrequired fieldthe question or task you want to send to the AI model;you can specify up to 500 characters in the user_prompt field |[optional]|
**model_name** | **StrictStr** | name of the AI modelrequired fieldmodel_nameconsists of the actual model name and version name;if the basic model name is specified, its latest version will be set by default;you can receive the list of available LLM models by making a separate request to the following endpoint: https://api.dataforseo.com/v3/ai_optimization/perplexity/llm_responses/models |[optional]|
**max_output_tokens** | **StrictInt** | maximum number of tokens in the AI responseoptional fieldminimum value: 1maximum value: 4096;default value: 2048;Note: if the reasoning model is specified in the request, the output token count may exceed the specified max_output_tokens limit |[optional]|
**temperature** | **StrictFloat** | randomness of the AI responseoptional fieldhigher values make output more diverse lower values make output more focusedminimum value: 0maximum value: 1.9default value: 0.77 |[optional]|
**top_p** | **StrictFloat** | diversity of the AI responseoptional field controls diversity of the response by limiting token selectionminimum value: 0maximum value: 1 default value: 0.9 |[optional]|
**web_search_country_iso_code** | **StrictStr** | country code for web search localizationoptional fieldspecify the country  ISO code to get localized web search resultsNote: available only for Perplexity Sonar modelsexample: US |[optional]|
**system_message** | **StrictStr** | instructions for the AI behavioroptional fielddefines the AI's role, tone, or specific behavior you can specify up to 500 characters in the system_message field |[optional]|
**message_chain** | **List[Optional[LlmMessageChainItem]]** | conversation history<br>optional field<br>array of message objects representing previous conversation turns;<br>each object must contain:<br>role string with either user or ai role;<br>message string with message content (max 500 characters);<br>you can specify maximum of 10 message objects in the array;<br>Note: for Perplexity models, messages must strictly alternate between user and AI roles (user → ai);<br>example:<br>'message_chain': [{'role':'user','message':'Hello, what’s up?'},{'role':'ai','message':'Hello! I’m doing well, thank you. How can I assist you today?'}] |[optional]|
**tag** | **StrictStr** | user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response |[optional]|