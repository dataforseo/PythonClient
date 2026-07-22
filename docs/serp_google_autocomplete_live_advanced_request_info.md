# SerpGoogleAutocompleteLiveAdvancedRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | keywordrequired fieldyou can specify up to 700 characters in the keyword fieldall %## will be decoded (plus character ‘+’ will be decoded to a space character)if you need to use the “%” character for your keyword, please specify it as “%25”;if you need to use the “+” character for your keyword, please specify it as “%2B”;<br>learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article |[optional]|
**location_code** | **StrictInt** | search engine location coderequired field if you don't specify location_name;you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/serp/google/locationsexample:2840 |[optional]|
**language_code** | **StrictStr** | search engine language coderequired field if you don't specify language_nameif you use this field, you don't need to specify language_name;you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languagesexample:en |[optional]|
**cursor_pointer** | **StrictInt** | search bar cursor pointeroptional fieldthe horizontal numerical position of the cursor pointer within the keyword in the search bar;by modifying the position of the cursor pointer, you will obtain different autocomplete suggestions for the same seed keyword;minimal value: 0default value: the number of the last character of the specified keywordexample:|which query are s - 'cursor_pointer': 0which query is s| - 'cursor_pointer': 16which que|ry is s - 'cursor_pointer': 9 |[optional]|