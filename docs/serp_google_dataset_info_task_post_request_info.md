# SerpGoogleDatasetInfoTaskPostRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**dataset_id** | **StrictStr** | ID of the datasetrequired fieldyou can find dataset ID in the dataset URL or dataset item of Google Dataset Search resultexample:L2cvMTFqbl85ZHN6MQ== |[optional]|
**language_code** | **StrictStr** | search engine language codeoptional fieldif you use this field, you don't need to specify language_namepossible value:en |[optional]|
**priority** | **StrictInt** | task priorityoptional fieldcan take the following values:1 – normal execution priority (set by default)2 – high execution priority<br>You will be additionally charged for the tasks with high execution priority.The cost can be calculated on the Pricing page. |[optional]|
**device** | **StrictStr** | device typeoptional fieldreturn results for a specific device typepossible value: desktop |[optional]|
**pingback_url** | **StrictStr** | notification URL of a completed taskoptional fieldwhen a task is completed we will notify you by GET request sent to the URL you have specifiedyou can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.example:http://your-server.com/pingscript?id=$idhttp://your-server.com/pingscript?id=$id&tag=$tagNote: special characters in pingback_url will be urlencoded;i.a., the # character will be encoded into %23<br>learn more on our Help Center |[optional]|
**postback_url** | **StrictStr** | URL for sending task resultsoptional fieldonce the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specifiedyou can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the requestexample:http://your-server.com/postbackscript?id=$idhttp://your-server.com/postbackscript?id=$id&tag=$tagNote: special characters in postback_url will be urlencoded;i.a., the # character will be encoded into %23<br>learn more on our Help Center |[optional]|
**postback_data** | **StrictStr** | postback_url datatyperequired field if you specify postback_urlcorresponds to the datatype that will be sent to your serverpossible value: advanced |[optional]|