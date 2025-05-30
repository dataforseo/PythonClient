# ContentGenerationGenerateMetaTagsLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**text** | **StrictStr** | initial target text<br>required field<br>text input for generating content;<br>can contain from 1 to 500 tokens<br>learn more about tokens on our help center |[optional]|
**creativity_index** | **StrictFloat** | creativity of content generation<br>optional field<br>the randomness of the selection of equally probable subsequent tokens;<br>can take values from 0 to 1;<br>default value: 0.8<br>learn more about this parameter on our help center |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|