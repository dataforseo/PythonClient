# DataforseoLabsAmazonRelatedKeywordsLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword required field UTF-8 encoding a keyword should be at least 3 characters long; the keywords should be specified in the lowercase format | [optional] 
**location_name** | **str** | full name of the location required field if you don’t specify location_code Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_name by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the US, Egypt, Saudi Arabia, and the United Arab Emirates locations only; example: United States | [optional] 
**location_code** | **int** | location code required field if you don’t specify location_name Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_code by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the US, Egypt, Saudi Arabia, and the United Arab Emirates locations only; example: 2840 | [optional] 
**language_name** | **str** | full name of the language required field if you don’t specify language_code Note: it is required to specify either language_name or language_code you can receive the list of available locations with their language_name by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: English | [optional] 
**language_code** | **str** | language code required field if you don’t specify language_name Note: it is required to specify either language_name or language_code you can receive the list of available locations with their language_code by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: en | [optional] 
**depth** | **int** | keyword search depth optional field default value: 1; number of the returned results depends on the value you set in this field; you can specify a level from 0 to 4; estimated number of keywords for each level (maximum): 0 – the keyword set in the keyword field 1 – 6 keywords 2 – 42 keywords 3 – 258 keywords 4 – 1554 keywords | [optional] 
**include_seed_keyword** | **bool** | include data for the seed keyword optional field if set to true, data for the seed keyword specified in the keyword field will be provided in the seed_keyword_data array of the response default value: false | [optional] 
**ignore_synonyms** | **bool** | ignore highly similar keywords optional field if set to true only core keywords will be returned, all highly similar keywords will be excluded; default value: false | [optional] 
**limit** | **int** | the maximum number of returned keywords optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned keywords optional field default value: 0 if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_amazon_related_keywords_live_request_info import DataforseoLabsAmazonRelatedKeywordsLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsAmazonRelatedKeywordsLiveRequestInfo from a JSON string
dataforseo_labs_amazon_related_keywords_live_request_info_instance = DataforseoLabsAmazonRelatedKeywordsLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsAmazonRelatedKeywordsLiveRequestInfo.to_json())

# convert the object into a dict
dataforseo_labs_amazon_related_keywords_live_request_info_dict = dataforseo_labs_amazon_related_keywords_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsAmazonRelatedKeywordsLiveRequestInfo from a dict
dataforseo_labs_amazon_related_keywords_live_request_info_form_dict = dataforseo_labs_amazon_related_keywords_live_request_info.from_dict(dataforseo_labs_amazon_related_keywords_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


