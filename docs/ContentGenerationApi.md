# dataforseo_client.ContentGenerationApi

All URIs are relative to *https://api.dataforseo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_grammar_live**](ContentGenerationApi.md#check_grammar_live) | **POST** /v3/content_generation/check_grammar/live | 
[**content_generation_check_grammar_languages**](ContentGenerationApi.md#content_generation_check_grammar_languages) | **GET** /v3/content_generation/check_grammar/languages | 
[**content_generation_text_summary_languages**](ContentGenerationApi.md#content_generation_text_summary_languages) | **GET** /v3/content_generation/text_summary/languages | 
[**generate_live**](ContentGenerationApi.md#generate_live) | **POST** /v3/content_generation/generate/live | 
[**generate_meta_tags_live**](ContentGenerationApi.md#generate_meta_tags_live) | **POST** /v3/content_generation/generate_meta_tags/live | 
[**generate_sub_topics_live**](ContentGenerationApi.md#generate_sub_topics_live) | **POST** /v3/content_generation/generate_sub_topics/live | 
[**generate_text_live**](ContentGenerationApi.md#generate_text_live) | **POST** /v3/content_generation/generate_text/live | 
[**grammar_rules**](ContentGenerationApi.md#grammar_rules) | **GET** /v3/content_generation/grammar_rules | 
[**paraphrase_live**](ContentGenerationApi.md#paraphrase_live) | **POST** /v3/content_generation/paraphrase/live | 
[**text_summary_live**](ContentGenerationApi.md#text_summary_live) | **POST** /v3/content_generation/text_summary/live | 


# **check_grammar_live**
> ContentGenerationCheckGrammarLiveResponseInfo check_grammar_live(content_generation_check_grammar_live_request_info=content_generation_check_grammar_live_request_info)



‌ This endpoint will provide you with grammar and spelling corrections for the text you specify. for more info please visit 'https://docs.dataforseo.com/v3/content_generation/check_grammar/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_generation_check_grammar_live_request_info import ContentGenerationCheckGrammarLiveRequestInfo
from dataforseo_client.models.content_generation_check_grammar_live_response_info import ContentGenerationCheckGrammarLiveResponseInfo
from dataforseo_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dataforseo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dataforseo_client.Configuration(
    host = "https://api.dataforseo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = dataforseo_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with dataforseo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataforseo_client.ContentGenerationApi(api_client)
    content_generation_check_grammar_live_request_info = [dataforseo_client.ContentGenerationCheckGrammarLiveRequestInfo()] # List[ContentGenerationCheckGrammarLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.check_grammar_live(content_generation_check_grammar_live_request_info=content_generation_check_grammar_live_request_info)
        print("The response of ContentGenerationApi->check_grammar_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationApi->check_grammar_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_check_grammar_live_request_info** | [**List[ContentGenerationCheckGrammarLiveRequestInfo]**](ContentGenerationCheckGrammarLiveRequestInfo.md)|  | [optional] 

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
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_generation_check_grammar_languages**
> ContentGenerationCheckGrammarLanguagesResponseInfo content_generation_check_grammar_languages()



You will receive the list of languages by calling this API.   As a response of the API server, you will receive JSON-encoded data containing a tasks array with the information specific to the set tasks. for more info please visit 'https://docs.dataforseo.com/v3/content_generation/check_grammar/languages/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_generation_check_grammar_languages_response_info import ContentGenerationCheckGrammarLanguagesResponseInfo
from dataforseo_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dataforseo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dataforseo_client.Configuration(
    host = "https://api.dataforseo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = dataforseo_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with dataforseo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataforseo_client.ContentGenerationApi(api_client)

    try:
        api_response = api_instance.content_generation_check_grammar_languages()
        print("The response of ContentGenerationApi->content_generation_check_grammar_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationApi->content_generation_check_grammar_languages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ContentGenerationCheckGrammarLanguagesResponseInfo**](ContentGenerationCheckGrammarLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_generation_text_summary_languages**
> ContentGenerationTextSummaryLanguagesResponseInfo content_generation_text_summary_languages()



You will receive the list of languages by calling this API.   As a response of the API server, you will receive JSON-encoded data containing a tasks array with the information specific to the set tasks. for more info please visit 'https://docs.dataforseo.com/v3/content_generation/text_summary/languages/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_generation_text_summary_languages_response_info import ContentGenerationTextSummaryLanguagesResponseInfo
from dataforseo_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dataforseo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dataforseo_client.Configuration(
    host = "https://api.dataforseo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = dataforseo_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with dataforseo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataforseo_client.ContentGenerationApi(api_client)

    try:
        api_response = api_instance.content_generation_text_summary_languages()
        print("The response of ContentGenerationApi->content_generation_text_summary_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationApi->content_generation_text_summary_languages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ContentGenerationTextSummaryLanguagesResponseInfo**](ContentGenerationTextSummaryLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_live**
> ContentGenerationGenerateLiveResponseInfo generate_live(content_generation_generate_live_request_info=content_generation_generate_live_request_info)



‌ This endpoint will provide you with a text generated based on the part of the text you define and other available parameters. for more info please visit 'https://docs.dataforseo.com/v3/content_generation/generate/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_generation_generate_live_request_info import ContentGenerationGenerateLiveRequestInfo
from dataforseo_client.models.content_generation_generate_live_response_info import ContentGenerationGenerateLiveResponseInfo
from dataforseo_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dataforseo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dataforseo_client.Configuration(
    host = "https://api.dataforseo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = dataforseo_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with dataforseo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataforseo_client.ContentGenerationApi(api_client)
    content_generation_generate_live_request_info = [dataforseo_client.ContentGenerationGenerateLiveRequestInfo()] # List[ContentGenerationGenerateLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.generate_live(content_generation_generate_live_request_info=content_generation_generate_live_request_info)
        print("The response of ContentGenerationApi->generate_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationApi->generate_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_generate_live_request_info** | [**List[ContentGenerationGenerateLiveRequestInfo]**](ContentGenerationGenerateLiveRequestInfo.md)|  | [optional] 

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
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_meta_tags_live**
> ContentGenerationGenerateMetaTagsLiveResponseInfo generate_meta_tags_live(content_generation_generate_meta_tags_live_request_info=content_generation_generate_meta_tags_live_request_info)



‌ This endpoint is designed to generate title and description meta tags for a text specified in the request. for more info please visit 'https://docs.dataforseo.com/v3/content_generation/generate_meta_tags/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_generation_generate_meta_tags_live_request_info import ContentGenerationGenerateMetaTagsLiveRequestInfo
from dataforseo_client.models.content_generation_generate_meta_tags_live_response_info import ContentGenerationGenerateMetaTagsLiveResponseInfo
from dataforseo_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dataforseo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dataforseo_client.Configuration(
    host = "https://api.dataforseo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = dataforseo_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with dataforseo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataforseo_client.ContentGenerationApi(api_client)
    content_generation_generate_meta_tags_live_request_info = [dataforseo_client.ContentGenerationGenerateMetaTagsLiveRequestInfo()] # List[ContentGenerationGenerateMetaTagsLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.generate_meta_tags_live(content_generation_generate_meta_tags_live_request_info=content_generation_generate_meta_tags_live_request_info)
        print("The response of ContentGenerationApi->generate_meta_tags_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationApi->generate_meta_tags_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_generate_meta_tags_live_request_info** | [**List[ContentGenerationGenerateMetaTagsLiveRequestInfo]**](ContentGenerationGenerateMetaTagsLiveRequestInfo.md)|  | [optional] 

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
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_sub_topics_live**
> ContentGenerationGenerateSubTopicsLiveResponseInfo generate_sub_topics_live(content_generation_generate_sub_topics_live_request_info=content_generation_generate_sub_topics_live_request_info)



‌ This endpoint will provide you with 10 subtopics generated based on the topic and other parameters you specify. for more info please visit 'https://docs.dataforseo.com/v3/content_generation/generate_sub_topics/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_generation_generate_sub_topics_live_request_info import ContentGenerationGenerateSubTopicsLiveRequestInfo
from dataforseo_client.models.content_generation_generate_sub_topics_live_response_info import ContentGenerationGenerateSubTopicsLiveResponseInfo
from dataforseo_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dataforseo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dataforseo_client.Configuration(
    host = "https://api.dataforseo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = dataforseo_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with dataforseo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataforseo_client.ContentGenerationApi(api_client)
    content_generation_generate_sub_topics_live_request_info = [dataforseo_client.ContentGenerationGenerateSubTopicsLiveRequestInfo()] # List[ContentGenerationGenerateSubTopicsLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.generate_sub_topics_live(content_generation_generate_sub_topics_live_request_info=content_generation_generate_sub_topics_live_request_info)
        print("The response of ContentGenerationApi->generate_sub_topics_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationApi->generate_sub_topics_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_generate_sub_topics_live_request_info** | [**List[ContentGenerationGenerateSubTopicsLiveRequestInfo]**](ContentGenerationGenerateSubTopicsLiveRequestInfo.md)|  | [optional] 

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
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_text_live**
> ContentGenerationGenerateTextLiveResponseInfo generate_text_live(content_generation_generate_text_live_request_info=content_generation_generate_text_live_request_info)



‌ This endpoint will provide you with a text generated based on the topic and other parameters you specify. for more info please visit 'https://docs.dataforseo.com/v3/content_generation/generate_text/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_generation_generate_text_live_request_info import ContentGenerationGenerateTextLiveRequestInfo
from dataforseo_client.models.content_generation_generate_text_live_response_info import ContentGenerationGenerateTextLiveResponseInfo
from dataforseo_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dataforseo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dataforseo_client.Configuration(
    host = "https://api.dataforseo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = dataforseo_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with dataforseo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataforseo_client.ContentGenerationApi(api_client)
    content_generation_generate_text_live_request_info = [dataforseo_client.ContentGenerationGenerateTextLiveRequestInfo()] # List[ContentGenerationGenerateTextLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.generate_text_live(content_generation_generate_text_live_request_info=content_generation_generate_text_live_request_info)
        print("The response of ContentGenerationApi->generate_text_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationApi->generate_text_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_generate_text_live_request_info** | [**List[ContentGenerationGenerateTextLiveRequestInfo]**](ContentGenerationGenerateTextLiveRequestInfo.md)|  | [optional] 

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
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grammar_rules**
> ContentGenerationGrammarRulesResponseInfo grammar_rules()



You will receive the list of grammar rules by calling this API.   As a response of the API server, you will receive JSON-encoded data containing a tasks array with the information specific to the set tasks. for more info please visit 'https://docs.dataforseo.com/v3/content_generation/grammar_rules/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_generation_grammar_rules_response_info import ContentGenerationGrammarRulesResponseInfo
from dataforseo_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dataforseo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dataforseo_client.Configuration(
    host = "https://api.dataforseo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = dataforseo_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with dataforseo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataforseo_client.ContentGenerationApi(api_client)

    try:
        api_response = api_instance.grammar_rules()
        print("The response of ContentGenerationApi->grammar_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationApi->grammar_rules: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ContentGenerationGrammarRulesResponseInfo**](ContentGenerationGrammarRulesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **paraphrase_live**
> ContentGenerationParaphraseLiveResponseInfo paraphrase_live(content_generation_paraphrase_live_request_info=content_generation_paraphrase_live_request_info)



‌ This endpoint will provide you with a paraphrased version of the text you specify. for more info please visit 'https://docs.dataforseo.com/v3/content_generation/paraphrase/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_generation_paraphrase_live_request_info import ContentGenerationParaphraseLiveRequestInfo
from dataforseo_client.models.content_generation_paraphrase_live_response_info import ContentGenerationParaphraseLiveResponseInfo
from dataforseo_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dataforseo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dataforseo_client.Configuration(
    host = "https://api.dataforseo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = dataforseo_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with dataforseo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataforseo_client.ContentGenerationApi(api_client)
    content_generation_paraphrase_live_request_info = [dataforseo_client.ContentGenerationParaphraseLiveRequestInfo()] # List[ContentGenerationParaphraseLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.paraphrase_live(content_generation_paraphrase_live_request_info=content_generation_paraphrase_live_request_info)
        print("The response of ContentGenerationApi->paraphrase_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationApi->paraphrase_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_paraphrase_live_request_info** | [**List[ContentGenerationParaphraseLiveRequestInfo]**](ContentGenerationParaphraseLiveRequestInfo.md)|  | [optional] 

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
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **text_summary_live**
> ContentGenerationTextSummaryLiveResponseInfo text_summary_live(content_generation_text_summary_live_request_info=content_generation_text_summary_live_request_info)



‌ This endpoint will provide you with statistical data based on the given text, such as the number of words and sentences, vocabulary density, and text readability. for more info please visit 'https://docs.dataforseo.com/v3/content_generation/text_summary/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_generation_text_summary_live_request_info import ContentGenerationTextSummaryLiveRequestInfo
from dataforseo_client.models.content_generation_text_summary_live_response_info import ContentGenerationTextSummaryLiveResponseInfo
from dataforseo_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dataforseo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dataforseo_client.Configuration(
    host = "https://api.dataforseo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = dataforseo_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with dataforseo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataforseo_client.ContentGenerationApi(api_client)
    content_generation_text_summary_live_request_info = [dataforseo_client.ContentGenerationTextSummaryLiveRequestInfo()] # List[ContentGenerationTextSummaryLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.text_summary_live(content_generation_text_summary_live_request_info=content_generation_text_summary_live_request_info)
        print("The response of ContentGenerationApi->text_summary_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentGenerationApi->text_summary_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_generation_text_summary_live_request_info** | [**List[ContentGenerationTextSummaryLiveRequestInfo]**](ContentGenerationTextSummaryLiveRequestInfo.md)|  | [optional] 

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
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

