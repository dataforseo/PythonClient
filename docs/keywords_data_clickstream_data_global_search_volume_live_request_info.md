# KeywordsDataClickstreamDataGlobalSearchVolumeLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keywords** | **List[Optional[StrictStr]]** | target keywords<br>required field<br>UTF-8 encoding<br>maximum number of keywords you can specify in this array: 1000;<br>each keyword should be at least 3 characters long;<br>the keywords will be converted to lowercase format;<br>Note: certain symbols and characters (e.g., UTF symbols, emojis) are not allowed<br>to learn more about which symbols and characters can be used, please refer to this article<br>learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|