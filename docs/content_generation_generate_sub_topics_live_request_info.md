# ContentGenerationGenerateSubTopicsLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**topic** | **StrictStr** | main topic of the content to generate<br>required field<br>main topic for content generation;<br>can contain from 1 to 50 tokens |[optional]|
**creativity_index** | **StrictFloat** | creativity of content generation<br>optional field<br>the randomness of the selection of equally probable subsequent tokens;<br>can take values from 0 to 1<br>default value: 0.8<br>learn more about this parameter on our help center |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|