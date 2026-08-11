# KeywordsDataClickstreamDataGlobalSearchVolumeLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keywords** | **List[Optional[StrictStr]]** | <em>target keywords</em><br><strong>required field</strong><br>UTF-8 encoding<br>maximum number of keywords you can specify in this array: 1000;<br>each keyword should be at least 3 characters long;<br>the keywords will be converted to lowercase format;<br><strong>Note:</strong> certain symbols and characters (e.g., UTF symbols, emojis) are not allowed<br>to learn more about which symbols and characters can be used, please refer to <a href='https://dataforseo.com/help-center/using-symbols-in-keywords-when-setting-a-google-ads-task' target='_blank' rel='noopener noreferrer'>this article</a><p>learn more about rules and limitations of <code>keyword</code> and <code>keywords</code> fields in DataForSEO APIs in this <a href='https://dataforseo.com/help-center/rules-and-limitations-of-keyword-and-keywords-fields-in-dataforseo-apis' rel='noopener noreferrer' target='_blank'>Help Center article</a> |[optional]|
**tag** | **StrictStr** | <em>user-defined task identifier</em><br>optional field<br><em>the character limit is 255</em><br>you can use this parameter to identify the task and match it with the result<br>you will find the specified <code>tag</code> value in the <code>data</code> object of the response |[optional]|