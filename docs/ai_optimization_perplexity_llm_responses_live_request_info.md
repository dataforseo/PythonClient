# AiOptimizationPerplexityLlmResponsesLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**user_prompt** | **StrictStr** | prompt for the AI model<br>required field<br>the question or task you want to send to the AI model;<br>you can specify up to 500 characters in the user_prompt field |[optional]|
**model_name** | **StrictStr** | name of the AI model<br>required field<br>model_nameconsists of the actual model name and version name;<br>if the basic model name is specified, its latest version will be set by default;<br>you can receive the list of available LLM models by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/gemini/llm_responses/models |[optional]|
**max_output_tokens** | **StrictInt** | maximum number of tokens in the AI response<br>optional field<br>minimum value: 1<br>maximum value: 2048<br>default value: 2048 |[optional]|
**temperature** | **StrictFloat** | randomness of the AI response<br>optional field<br>higher values make output more diverse<br>lower values make output more focused<br>minimum value: 0<br>maximum value: 1.9<br>default value: 0.77 |[optional]|
**top_p** | **StrictFloat** | diversity of the AI response<br>optional field<br>controls diversity of the response by limiting token selection<br>minimum value: 0<br>maximum value: 1<br>default value: 0.9 |[optional]|
**web_search_country_iso_code** | **StrictStr** | country code for web search localization<br>optional field<br>specify the country  ISO code to get localized web search results<br>Note: available only for Perplexity Sonar models<br>example: US |[optional]|
**system_message** | **StrictStr** | instructions for the AI behavior<br>optional field<br>defines the AI’s role, tone, or specific behavior<br>you can specify up to 500 characters in the system_message field |[optional]|
**message_chain** | **List[Optional[LlmMessageChainItem]]** | conversation history<br>optional field<br>array of message objects representing previous conversation turns;<br>each object must contain:<br>role string with either user or ai role;<br>message string with message content (max 500 characters);<br>you can specify maximum of 10 message objects in the array;<br>Note: for Perplexity models, messages must strictly alternate between user and AI roles (user → ai);<br>example:<br>'message_chain': [{'role':'user','message':'Hello, what’s up?'},{'role':'ai','message':'Hello! I’m doing well, thank you. How can I assist you today?'}] |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|