# ContentGenerationApi

All URIs are relative to *https://api.dataforseo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
[**generateLive**](ContentGenerationApi.md#generateLive) | **POST**  /v3/content_generation/generate/live  |
[**generateTextLive**](ContentGenerationApi.md#generateTextLive) | **POST**  /v3/content_generation/generate_text/live  |
[**generateMetaTagsLive**](ContentGenerationApi.md#generateMetaTagsLive) | **POST**  /v3/content_generation/generate_meta_tags/live  |
[**generateSubTopicsLive**](ContentGenerationApi.md#generateSubTopicsLive) | **POST**  /v3/content_generation/generate_sub_topics/live  |
[**paraphraseLive**](ContentGenerationApi.md#paraphraseLive) | **POST**  /v3/content_generation/paraphrase/live  |
[**checkGrammarLive**](ContentGenerationApi.md#checkGrammarLive) | **POST**  /v3/content_generation/check_grammar/live  |
[**contentGenerationCheckGrammarLanguages**](ContentGenerationApi.md#contentGenerationCheckGrammarLanguages) | **GET**  /v3/content_generation/check_grammar/languages  |
[**grammarRules**](ContentGenerationApi.md#grammarRules) | **GET**  /v3/content_generation/grammar_rules  |
[**textSummaryLive**](ContentGenerationApi.md#textSummaryLive) | **POST**  /v3/content_generation/text_summary/live  |
[**contentGenerationTextSummaryLanguages**](ContentGenerationApi.md#contentGenerationTextSummaryLanguages) | **GET**  /v3/content_generation/text_summary/languages  |

<a id="generateLive"></a>
# **generateLive**
> ContentGenerationGenerateLiveResponseInfo generateLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_generation_api import ContentGenerationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_content_generation_generate_live_request_info import List[Optional[ContentGenerationGenerateLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_generation_api = ContentGenerationApi(api_client)

        response = content_generation_api.generate_live([ContentGenerationGenerateLiveRequestInfo(
                text="SEO is",
                max_new_tokens=100,
                creativity_index=1,
                avoid_starting_words=[
                    "SEO",
                    "search engine optimization",
                    "SEO is",
                    ],
                stop_words=[
                    "123",
                    "\n",
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[ContentGenerationGenerateLiveRequestInfo]]&gt;**](List[Optional[ContentGenerationGenerateLiveRequestInfo]].md)|  | [optional] |



### Return type

[**ContentGenerationGenerateLiveResponseInfo**](ContentGenerationGenerateLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="generateTextLive"></a>
# **generateTextLive**
> ContentGenerationGenerateTextLiveResponseInfo generateTextLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_generation_api import ContentGenerationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_content_generation_generate_text_live_request_info import List[Optional[ContentGenerationGenerateTextLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_generation_api = ContentGenerationApi(api_client)

        response = content_generation_api.generate_text_live([ContentGenerationGenerateTextLiveRequestInfo(
                topic="Steve Jobs",
                word_count=50,
                sub_topics=[
                    "Apple",
                    "Pixar",
                    "Amazing Products",
                    ],
                description="Take a closer look at Steve Jobs' life and his incredible impact on the tech industry, with a special focus on the development of the iPhone.",
                meta_keywords=[
                    "iPhone",
                    "sell",
                    "CEO",
                    ],
                creativity_index=0.8,
                include_conclusion=True,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[ContentGenerationGenerateTextLiveRequestInfo]]&gt;**](List[Optional[ContentGenerationGenerateTextLiveRequestInfo]].md)|  | [optional] |



### Return type

[**ContentGenerationGenerateTextLiveResponseInfo**](ContentGenerationGenerateTextLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="generateMetaTagsLive"></a>
# **generateMetaTagsLive**
> ContentGenerationGenerateMetaTagsLiveResponseInfo generateMetaTagsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_generation_api import ContentGenerationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_content_generation_generate_meta_tags_live_request_info import List[Optional[ContentGenerationGenerateMetaTagsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_generation_api = ContentGenerationApi(api_client)

        response = content_generation_api.generate_meta_tags_live([ContentGenerationGenerateMetaTagsLiveRequestInfo(
                text="The idea to develop an instrument for local SEO didn’t come to the GMB Crush CEO, Matteo Barletta, out of the blue. Having a huge interest in search engine optimization, Matteo has come a long way from being an SEO freelancer to launching his own agency, SEO Heroes. At some point, he and his team noticed that it was quite challenging to work with local SEO projects, especially those related to Google My Business listings. There were simply no tools that could streamline their work and provide the functionality the agency needed.\n\n“We started to develop the idea of ​​our tool capable of doing Google Business SEO audits, tracking stats, and generating business proposals at the same time.",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[ContentGenerationGenerateMetaTagsLiveRequestInfo]]&gt;**](List[Optional[ContentGenerationGenerateMetaTagsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**ContentGenerationGenerateMetaTagsLiveResponseInfo**](ContentGenerationGenerateMetaTagsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="generateSubTopicsLive"></a>
# **generateSubTopicsLive**
> ContentGenerationGenerateSubTopicsLiveResponseInfo generateSubTopicsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_generation_api import ContentGenerationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_content_generation_generate_sub_topics_live_request_info import List[Optional[ContentGenerationGenerateSubTopicsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_generation_api = ContentGenerationApi(api_client)

        response = content_generation_api.generate_sub_topics_live([ContentGenerationGenerateSubTopicsLiveRequestInfo(
                topic="Steve Jobs",
                creativity_index=0.9,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[ContentGenerationGenerateSubTopicsLiveRequestInfo]]&gt;**](List[Optional[ContentGenerationGenerateSubTopicsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**ContentGenerationGenerateSubTopicsLiveResponseInfo**](ContentGenerationGenerateSubTopicsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="paraphraseLive"></a>
# **paraphraseLive**
> ContentGenerationParaphraseLiveResponseInfo paraphraseLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_generation_api import ContentGenerationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_content_generation_paraphrase_live_request_info import List[Optional[ContentGenerationParaphraseLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_generation_api = ContentGenerationApi(api_client)

        response = content_generation_api.paraphrase_live([ContentGenerationParaphraseLiveRequestInfo(
                text="The idea to develop an instrument for local SEO didn’t come to the GMB Crush CEO, Matteo Barletta, out of the blue. Having a huge interest in search engine optimization, Matteo has come a long way from being an SEO freelancer to launching his own agency, SEO Heroes. At some point, he and his team noticed that it was quite challenging to work with local SEO projects, especially those related to Google My Business listings.",
                creativity_index=0.8,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[ContentGenerationParaphraseLiveRequestInfo]]&gt;**](List[Optional[ContentGenerationParaphraseLiveRequestInfo]].md)|  | [optional] |



### Return type

[**ContentGenerationParaphraseLiveResponseInfo**](ContentGenerationParaphraseLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="checkGrammarLive"></a>
# **checkGrammarLive**
> ContentGenerationCheckGrammarLiveResponseInfo checkGrammarLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_generation_api import ContentGenerationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_content_generation_check_grammar_live_request_info import List[Optional[ContentGenerationCheckGrammarLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_generation_api = ContentGenerationApi(api_client)

        response = content_generation_api.check_grammar_live([ContentGenerationCheckGrammarLiveRequestInfo(
                text="Hello, my name is John! And I'm very glad to work with you toda",
                language_code="en-US",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[ContentGenerationCheckGrammarLiveRequestInfo]]&gt;**](List[Optional[ContentGenerationCheckGrammarLiveRequestInfo]].md)|  | [optional] |



### Return type

[**ContentGenerationCheckGrammarLiveResponseInfo**](ContentGenerationCheckGrammarLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="contentGenerationCheckGrammarLanguages"></a>
# **contentGenerationCheckGrammarLanguages**
> ContentGenerationCheckGrammarLanguagesResponseInfo contentGenerationCheckGrammarLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_generation_api import ContentGenerationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_generation_api = ContentGenerationApi(api_client)

        response = content_generation_api.content_generation_check_grammar_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**ContentGenerationCheckGrammarLanguagesResponseInfo**](ContentGenerationCheckGrammarLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="grammarRules"></a>
# **grammarRules**
> ContentGenerationGrammarRulesResponseInfo grammarRules()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_generation_api import ContentGenerationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_generation_api = ContentGenerationApi(api_client)

        response = content_generation_api.grammar_rules()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**ContentGenerationGrammarRulesResponseInfo**](ContentGenerationGrammarRulesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="textSummaryLive"></a>
# **textSummaryLive**
> ContentGenerationTextSummaryLiveResponseInfo textSummaryLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_generation_api import ContentGenerationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_content_generation_text_summary_live_request_info import List[Optional[ContentGenerationTextSummaryLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_generation_api = ContentGenerationApi(api_client)

        response = content_generation_api.text_summary_live([ContentGenerationTextSummaryLiveRequestInfo(
                text="Removing [RequireHttps] does nothing but break the https redirection, and doesn't enforce an https url on my route. I've got one method which i want to expose over http and a different one over https. If i accidentally enter http in my url for the https-only method, it should redirect. It currently works as is, the problem is that there is an undocument (seemingly unrelated) setting I have to add to get it all working. And that is the SslPort thing",
                language_name="English (United States)",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[ContentGenerationTextSummaryLiveRequestInfo]]&gt;**](List[Optional[ContentGenerationTextSummaryLiveRequestInfo]].md)|  | [optional] |



### Return type

[**ContentGenerationTextSummaryLiveResponseInfo**](ContentGenerationTextSummaryLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="contentGenerationTextSummaryLanguages"></a>
# **contentGenerationTextSummaryLanguages**
> ContentGenerationTextSummaryLanguagesResponseInfo contentGenerationTextSummaryLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_generation_api import ContentGenerationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_generation_api = ContentGenerationApi(api_client)

        response = content_generation_api.content_generation_text_summary_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**ContentGenerationTextSummaryLanguagesResponseInfo**](ContentGenerationTextSummaryLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |