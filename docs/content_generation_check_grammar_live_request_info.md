# ContentGenerationCheckGrammarLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**text** | **StrictStr** | target text<br>required field<br>can contain from 1 to 10000 tokens<br>learn more about tokens on our help center |[optional]|
**language_code** | **StrictStr** | code of the text language<br>required field if you do not specify language_name<br>see the List of Languages for Content Generation Check Grammar API |[optional]|
**language_name** | **StrictStr** | name of the text language<br>required field if you do not specify language_code<br>see the List of Languages for Content Generation Check Grammar API |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|