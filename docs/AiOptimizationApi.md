# AiOptimizationApi

All URIs are relative to *https://api.dataforseo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
[**chatGptLlmResponsesModels**](AiOptimizationApi.md#chatGptLlmResponsesModels) | **GET**  /v3/ai_optimization/chat_gpt/llm_responses/models  |
[**chatGptLlmResponsesLive**](AiOptimizationApi.md#chatGptLlmResponsesLive) | **POST**  /v3/ai_optimization/chat_gpt/llm_responses/live  |
[**chatGptLlmResponsesTaskPost**](AiOptimizationApi.md#chatGptLlmResponsesTaskPost) | **POST**  /v3/ai_optimization/chat_gpt/llm_responses/task_post  |
[**chatGptLlmResponsesTasksReady**](AiOptimizationApi.md#chatGptLlmResponsesTasksReady) | **GET**  /v3/ai_optimization/chat_gpt/llm_responses/tasks_ready  |
[**chatGptLlmResponsesTaskGet**](AiOptimizationApi.md#chatGptLlmResponsesTaskGet) | **GET**  /v3/ai_optimization/chat_gpt/llm_responses/task_get/{id}  |
[**aiOptimizationChatGptLlmScraperLocations**](AiOptimizationApi.md#aiOptimizationChatGptLlmScraperLocations) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/locations  |
[**aiOptimizationChatGptLlmScraperLocationsCountry**](AiOptimizationApi.md#aiOptimizationChatGptLlmScraperLocationsCountry) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/locations/{country}  |
[**aiOptimizationChatGptLlmScraperLanguages**](AiOptimizationApi.md#aiOptimizationChatGptLlmScraperLanguages) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/languages  |
[**chatGptLlmScraperTaskPost**](AiOptimizationApi.md#chatGptLlmScraperTaskPost) | **POST**  /v3/ai_optimization/chat_gpt/llm_scraper/task_post  |
[**chatGptLlmScraperTasksReady**](AiOptimizationApi.md#chatGptLlmScraperTasksReady) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/tasks_ready  |
[**chatGptLlmScraperTaskGetAdvanced**](AiOptimizationApi.md#chatGptLlmScraperTaskGetAdvanced) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/task_get/advanced/{id}  |
[**chatGptLlmScraperTaskGetHtml**](AiOptimizationApi.md#chatGptLlmScraperTaskGetHtml) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/task_get/html/{id}  |
[**claudeLlmResponsesModels**](AiOptimizationApi.md#claudeLlmResponsesModels) | **GET**  /v3/ai_optimization/claude/llm_responses/models  |
[**claudeLlmResponsesLive**](AiOptimizationApi.md#claudeLlmResponsesLive) | **POST**  /v3/ai_optimization/claude/llm_responses/live  |
[**claudeLlmResponsesTaskPost**](AiOptimizationApi.md#claudeLlmResponsesTaskPost) | **POST**  /v3/ai_optimization/claude/llm_responses/task_post  |
[**claudeLlmResponsesTasksReady**](AiOptimizationApi.md#claudeLlmResponsesTasksReady) | **GET**  /v3/ai_optimization/claude/llm_responses/tasks_ready  |
[**claudeLlmResponsesTaskGet**](AiOptimizationApi.md#claudeLlmResponsesTaskGet) | **GET**  /v3/ai_optimization/claude/llm_responses/task_get/{id}  |
[**geminiLlmResponsesModels**](AiOptimizationApi.md#geminiLlmResponsesModels) | **GET**  /v3/ai_optimization/gemini/llm_responses/models  |
[**geminiLlmResponsesLive**](AiOptimizationApi.md#geminiLlmResponsesLive) | **POST**  /v3/ai_optimization/gemini/llm_responses/live  |
[**perplexityLlmResponsesModels**](AiOptimizationApi.md#perplexityLlmResponsesModels) | **GET**  /v3/ai_optimization/perplexity/llm_responses/models  |
[**perplexityLlmResponsesLive**](AiOptimizationApi.md#perplexityLlmResponsesLive) | **POST**  /v3/ai_optimization/perplexity/llm_responses/live  |
[**aiKeywordDataAvailableFilters**](AiOptimizationApi.md#aiKeywordDataAvailableFilters) | **GET**  /v3/ai_optimization/ai_keyword_data/available_filters  |
[**aiOptimizationAiKeywordDataLocationsAndLanguages**](AiOptimizationApi.md#aiOptimizationAiKeywordDataLocationsAndLanguages) | **GET**  /v3/ai_optimization/ai_keyword_data/locations_and_languages  |
[**aiKeywordDataKeywordsSearchVolumeLive**](AiOptimizationApi.md#aiKeywordDataKeywordsSearchVolumeLive) | **POST**  /v3/ai_optimization/ai_keyword_data/keywords_search_volume/live  |

<a id="chatGptLlmResponsesModels"></a>
# **chatGptLlmResponsesModels**
> AiOptimizationChatGptLlmResponsesModelsResponseInfo chatGptLlmResponsesModels()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let response = await api.chatGptLlmResponsesModels();
```

### Parameters


    
This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmResponsesModelsResponseInfo**](AiOptimizationChatGptLlmResponsesModelsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmResponsesLive"></a>
# **chatGptLlmResponsesLive**
> AiOptimizationChatGptLlmResponsesLiveResponseInfo chatGptLlmResponsesLive()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let task = new AiOptimizationChatGptLlmResponsesLiveRequestInfo();
   task.user_prompt = "provide information on how relevant the amusement park business is in France now";
   task.model_name = "gpt-4.1-mini";
   task.max_output_tokens = 200;
   task.temperature = 0.3;
   task.top_p = 0.5;
   task.web_search = true;
   task.web_search_country_iso_code = "FR";
   task.web_search_city = "Paris";
   task.system_message = "communicate as if we are in a business meeting";
   task.message_chain = [
         new LlmMessageChainItem({
           role: "user",
           message: "Hello, what’s up?",
         }),
         new LlmMessageChainItem({
           role: "ai",
           message: "Hello! I’m doing well, thank you. How can I assist you today? Are there any specific topics or projects you’d like to discuss in our meeting?",
         }),
   ];
 let response = await api.chatGptLlmResponsesLive([task]);
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **** | [**List&lt;AiOptimizationChatGptLlmResponsesLiveRequestInfo[]&gt;**](AiOptimizationChatGptLlmResponsesLiveRequestInfo[].md)|  | [optional] |



### Return type

[**AiOptimizationChatGptLlmResponsesLiveResponseInfo**](AiOptimizationChatGptLlmResponsesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmResponsesTaskPost"></a>
# **chatGptLlmResponsesTaskPost**
> AiOptimizationChatGptLlmResponsesTaskPostResponseInfo chatGptLlmResponsesTaskPost()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let task = new AiOptimizationChatGptLlmResponsesTaskPostRequestInfo();
   task.user_prompt = "provide information on how relevant the amusement park business is in France now";
   task.model_name = "gpt-4.1-mini";
   task.system_message = "communicate as if we are in a business meeting";
   task.message_chain = [
         new LlmMessageChainItem({
           role: "user",
           message: "Hello, what’s up?",
         }),
         new LlmMessageChainItem({
           role: "ai",
           message: "Hello! I’m doing well, thank you. How can I assist you today? Are there any specific topics or projects you’d like to discuss in our meeting?",
         }),
   ];
 let response = await api.chatGptLlmResponsesTaskPost([task]);
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **** | [**List&lt;AiOptimizationChatGptLlmResponsesTaskPostRequestInfo[]&gt;**](AiOptimizationChatGptLlmResponsesTaskPostRequestInfo[].md)|  | [optional] |



### Return type

[**AiOptimizationChatGptLlmResponsesTaskPostResponseInfo**](AiOptimizationChatGptLlmResponsesTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmResponsesTasksReady"></a>
# **chatGptLlmResponsesTasksReady**
> AiOptimizationChatGptLlmResponsesTasksReadyResponseInfo chatGptLlmResponsesTasksReady()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let response = await api.chatGptLlmResponsesTasksReady();
```

### Parameters


    
This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmResponsesTasksReadyResponseInfo**](AiOptimizationChatGptLlmResponsesTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmResponsesTaskGet"></a>
# **chatGptLlmResponsesTaskGet**
> AiOptimizationChatGptLlmResponsesTaskGetResponseInfo chatGptLlmResponsesTaskGet()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let id = "00000000-0000-0000-0000-000000000000";
 let response = await api.chatGptLlmResponsesTaskGet(id);
```

### Parameters


    
This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmResponsesTaskGetResponseInfo**](AiOptimizationChatGptLlmResponsesTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="aiOptimizationChatGptLlmScraperLocations"></a>
# **aiOptimizationChatGptLlmScraperLocations**
> AiOptimizationChatGptLlmScraperLocationsResponseInfo aiOptimizationChatGptLlmScraperLocations()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let response = await api.aiOptimizationChatGptLlmScraperLocations();
```

### Parameters


    
This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmScraperLocationsResponseInfo**](AiOptimizationChatGptLlmScraperLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="aiOptimizationChatGptLlmScraperLocationsCountry"></a>
# **aiOptimizationChatGptLlmScraperLocationsCountry**
> AiOptimizationChatGptLlmScraperLocationsCountryResponseInfo aiOptimizationChatGptLlmScraperLocationsCountry()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let country = "us";
 let response = await api.aiOptimizationChatGptLlmScraperLocationsCountry(country);
```

### Parameters


    
This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmScraperLocationsCountryResponseInfo**](AiOptimizationChatGptLlmScraperLocationsCountryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="aiOptimizationChatGptLlmScraperLanguages"></a>
# **aiOptimizationChatGptLlmScraperLanguages**
> AiOptimizationChatGptLlmScraperLanguagesResponseInfo aiOptimizationChatGptLlmScraperLanguages()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let response = await api.aiOptimizationChatGptLlmScraperLanguages();
```

### Parameters


    
This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmScraperLanguagesResponseInfo**](AiOptimizationChatGptLlmScraperLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmScraperTaskPost"></a>
# **chatGptLlmScraperTaskPost**
> AiOptimizationChatGptLlmScraperTaskPostResponseInfo chatGptLlmScraperTaskPost()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let task = new AiOptimizationChatGptLlmScraperTaskPostRequestInfo();
   task.keyword = "what is chatgpt";
   task.location_code = 2840;
   task.language_code = "en";
 let response = await api.chatGptLlmScraperTaskPost([task]);
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **** | [**List&lt;AiOptimizationChatGptLlmScraperTaskPostRequestInfo[]&gt;**](AiOptimizationChatGptLlmScraperTaskPostRequestInfo[].md)|  | [optional] |



### Return type

[**AiOptimizationChatGptLlmScraperTaskPostResponseInfo**](AiOptimizationChatGptLlmScraperTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmScraperTasksReady"></a>
# **chatGptLlmScraperTasksReady**
> AiOptimizationChatGptLlmScraperTasksReadyResponseInfo chatGptLlmScraperTasksReady()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let response = await api.chatGptLlmScraperTasksReady();
```

### Parameters


    
This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmScraperTasksReadyResponseInfo**](AiOptimizationChatGptLlmScraperTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmScraperTaskGetAdvanced"></a>
# **chatGptLlmScraperTaskGetAdvanced**
> AiOptimizationChatGptLlmScraperTaskGetAdvancedResponseInfo chatGptLlmScraperTaskGetAdvanced()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let id = "00000000-0000-0000-0000-000000000000";
 let response = await api.chatGptLlmScraperTaskGetAdvanced(id);
```

### Parameters


    
This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmScraperTaskGetAdvancedResponseInfo**](AiOptimizationChatGptLlmScraperTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmScraperTaskGetHtml"></a>
# **chatGptLlmScraperTaskGetHtml**
> AiOptimizationChatGptLlmScraperTaskGetHtmlResponseInfo chatGptLlmScraperTaskGetHtml()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let id = "00000000-0000-0000-0000-000000000000";
 let response = await api.chatGptLlmScraperTaskGetHtml(id);
```

### Parameters


    
This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmScraperTaskGetHtmlResponseInfo**](AiOptimizationChatGptLlmScraperTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="claudeLlmResponsesModels"></a>
# **claudeLlmResponsesModels**
> AiOptimizationClaudeLlmResponsesModelsResponseInfo claudeLlmResponsesModels()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let response = await api.claudeLlmResponsesModels();
```

### Parameters


    
This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationClaudeLlmResponsesModelsResponseInfo**](AiOptimizationClaudeLlmResponsesModelsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="claudeLlmResponsesLive"></a>
# **claudeLlmResponsesLive**
> AiOptimizationClaudeLlmResponsesLiveResponseInfo claudeLlmResponsesLive()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let task = new AiOptimizationClaudeLlmResponsesLiveRequestInfo();
   task.user_prompt = "provide information on how relevant the amusement park business is in France now";
   task.model_name = "claude-opus-4-0";
   task.max_output_tokens = 200;
   task.temperature = 0.3;
   task.top_p = 0.5;
   task.web_search = true;
   task.web_search_country_iso_code = "FR";
   task.system_message = "communicate as if we are in a business meeting";
   task.message_chain = [
         new LlmMessageChainItem({
           role: "user",
           message: "Hello, what’s up?",
         }),
         new LlmMessageChainItem({
           role: "ai",
           message: "Hello! I’m doing well, thank you. How can I assist you today? Are there any specific topics or projects you’d like to discuss in our meeting?",
         }),
   ];
 let response = await api.claudeLlmResponsesLive([task]);
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **** | [**List&lt;AiOptimizationClaudeLlmResponsesLiveRequestInfo[]&gt;**](AiOptimizationClaudeLlmResponsesLiveRequestInfo[].md)|  | [optional] |



### Return type

[**AiOptimizationClaudeLlmResponsesLiveResponseInfo**](AiOptimizationClaudeLlmResponsesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="claudeLlmResponsesTaskPost"></a>
# **claudeLlmResponsesTaskPost**
> AiOptimizationClaudeLlmResponsesTaskPostResponseInfo claudeLlmResponsesTaskPost()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let task = new AiOptimizationClaudeLlmResponsesTaskPostRequestInfo();
   task.user_prompt = "provide information on how relevant the amusement park business is in France now";
   task.model_name = "claude-sonnet-4-0";
   task.max_output_tokens = 1024;
   task.temperature = 0.3;
   task.top_p = 0.5;
   task.web_search = true;
   task.web_search_country_iso_code = "FR";
   task.system_message = "communicate as if we are in a business meeting";
   task.message_chain = [
         new LlmMessageChainItem({
           role: "user",
           message: "Hello, what’s up?",
         }),
         new LlmMessageChainItem({
           role: "ai",
           message: "Hello! I’m doing well, thank you. How can I assist you today? Are there any specific topics or projects you’d like to discuss in our meeting?",
         }),
   ];
 let response = await api.claudeLlmResponsesTaskPost([task]);
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **** | [**List&lt;AiOptimizationClaudeLlmResponsesTaskPostRequestInfo[]&gt;**](AiOptimizationClaudeLlmResponsesTaskPostRequestInfo[].md)|  | [optional] |



### Return type

[**AiOptimizationClaudeLlmResponsesTaskPostResponseInfo**](AiOptimizationClaudeLlmResponsesTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="claudeLlmResponsesTasksReady"></a>
# **claudeLlmResponsesTasksReady**
> AiOptimizationClaudeLlmResponsesTasksReadyResponseInfo claudeLlmResponsesTasksReady()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let response = await api.claudeLlmResponsesTasksReady();
```

### Parameters


    
This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationClaudeLlmResponsesTasksReadyResponseInfo**](AiOptimizationClaudeLlmResponsesTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="claudeLlmResponsesTaskGet"></a>
# **claudeLlmResponsesTaskGet**
> AiOptimizationClaudeLlmResponsesTaskGetResponseInfo claudeLlmResponsesTaskGet()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let id = "00000000-0000-0000-0000-000000000000";
 let response = await api.claudeLlmResponsesTaskGet(id);
```

### Parameters


    
This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationClaudeLlmResponsesTaskGetResponseInfo**](AiOptimizationClaudeLlmResponsesTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="geminiLlmResponsesModels"></a>
# **geminiLlmResponsesModels**
> AiOptimizationGeminiLlmResponsesModelsResponseInfo geminiLlmResponsesModels()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let response = await api.geminiLlmResponsesModels();
```

### Parameters


    
This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationGeminiLlmResponsesModelsResponseInfo**](AiOptimizationGeminiLlmResponsesModelsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="geminiLlmResponsesLive"></a>
# **geminiLlmResponsesLive**
> AiOptimizationGeminiLlmResponsesLiveResponseInfo geminiLlmResponsesLive()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let task = new AiOptimizationGeminiLlmResponsesLiveRequestInfo();
   task.user_prompt = "provide information on how relevant the amusement park business is in France now";
   task.model_name = "gemini-2.5-flash";
   task.max_output_tokens = 200;
   task.temperature = 0.3;
   task.top_p = 0.5;
   task.web_search = true;
   task.system_message = "communicate as if we are in a business meeting";
   task.message_chain = [
         new LlmMessageChainItem({
           role: "user",
           message: "Hello, what’s up?",
         }),
         new LlmMessageChainItem({
           role: "ai",
           message: "Hello! I’m doing well, thank you. How can I assist you today? Are there any specific topics or projects you’d like to discuss in our meeting?",
         }),
   ];
 let response = await api.geminiLlmResponsesLive([task]);
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **** | [**List&lt;AiOptimizationGeminiLlmResponsesLiveRequestInfo[]&gt;**](AiOptimizationGeminiLlmResponsesLiveRequestInfo[].md)|  | [optional] |



### Return type

[**AiOptimizationGeminiLlmResponsesLiveResponseInfo**](AiOptimizationGeminiLlmResponsesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="perplexityLlmResponsesModels"></a>
# **perplexityLlmResponsesModels**
> AiOptimizationPerplexityLlmResponsesModelsResponseInfo perplexityLlmResponsesModels()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let response = await api.perplexityLlmResponsesModels();
```

### Parameters


    
This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationPerplexityLlmResponsesModelsResponseInfo**](AiOptimizationPerplexityLlmResponsesModelsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="perplexityLlmResponsesLive"></a>
# **perplexityLlmResponsesLive**
> AiOptimizationPerplexityLlmResponsesLiveResponseInfo perplexityLlmResponsesLive()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let task = new AiOptimizationPerplexityLlmResponsesLiveRequestInfo();
   task.user_prompt = "provide information on how relevant the amusement park business is in France now";
   task.model_name = "sonar-reasoning";
   task.max_output_tokens = 200;
   task.temperature = 0.3;
   task.top_p = 0.5;
   task.web_search_country_iso_code = "FR";
   task.system_message = "communicate as if we are in a business meeting";
   task.message_chain = [
         new LlmMessageChainItem({
           role: "user",
           message: "Hello, what’s up?",
         }),
         new LlmMessageChainItem({
           role: "ai",
           message: "Hello! I’m doing well, thank you. How can I assist you today? Are there any specific topics or projects you’d like to discuss in our meeting?",
         }),
   ];
 let response = await api.perplexityLlmResponsesLive([task]);
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **** | [**List&lt;AiOptimizationPerplexityLlmResponsesLiveRequestInfo[]&gt;**](AiOptimizationPerplexityLlmResponsesLiveRequestInfo[].md)|  | [optional] |



### Return type

[**AiOptimizationPerplexityLlmResponsesLiveResponseInfo**](AiOptimizationPerplexityLlmResponsesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="aiKeywordDataAvailableFilters"></a>
# **aiKeywordDataAvailableFilters**
> AiOptimizationAiKeywordDataAvailableFiltersResponseInfo aiKeywordDataAvailableFilters()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let response = await api.aiKeywordDataAvailableFilters();
```

### Parameters


    
This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationAiKeywordDataAvailableFiltersResponseInfo**](AiOptimizationAiKeywordDataAvailableFiltersResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="aiOptimizationAiKeywordDataLocationsAndLanguages"></a>
# **aiOptimizationAiKeywordDataLocationsAndLanguages**
> AiOptimizationAiKeywordDataLocationsAndLanguagesResponseInfo aiOptimizationAiKeywordDataLocationsAndLanguages()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let response = await api.aiOptimizationAiKeywordDataLocationsAndLanguages();
```

### Parameters


    
This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationAiKeywordDataLocationsAndLanguagesResponseInfo**](AiOptimizationAiKeywordDataLocationsAndLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="aiKeywordDataKeywordsSearchVolumeLive"></a>
# **aiKeywordDataKeywordsSearchVolumeLive**
> AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveResponseInfo aiKeywordDataKeywordsSearchVolumeLive()


### Example
```typescript
 const username = 'USERNAME';
 const password = 'PASSWORD';

 let api = new AiOptimizationApi("https://api.dataforseo.com", {
   fetch: (url: RequestInfo, init?: RequestInit): Promise<Response> => {
     const token = btoa(`${username}:${password}`);
     const authHeader = { 'Authorization': `Basic ${token}` };

     const newInit: RequestInit = {
       ...init,
       headers: {
       ...init?.headers,
       ...authHeader,
     }
   };

   return fetch(url, newInit);
   }
 });

 let task = new AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveRequestInfo();
   task.keywords = [
       "iphone",
       "seo",
   ];
   task.location_code = 2840;
   task.language_name = "English";
 let response = await api.aiKeywordDataKeywordsSearchVolumeLive([task]);
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **** | [**List&lt;AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveRequestInfo[]&gt;**](AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveRequestInfo[].md)|  | [optional] |



### Return type

[**AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveResponseInfo**](AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |