# SerpGoogleDatasetInfoTaskPostRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**dataset_id** | **StrictStr** | ID of the dataset<br>required field<br>you can find dataset ID in the dataset URL or dataset item of Google Dataset Search result<br>example:<br>L2cvMTFqbl85ZHN6MQ== |[optional]|
**priority** | **StrictInt** | task priority<br>optional field<br>can take the following values:<br>1 – normal execution priority (set by default)<br>2 – high execution priority<br>You will be additionally charged for the tasks with high execution priority.<br>The cost can be calculated on the Pricing page. |[optional]|
**language_name** | **StrictStr** | full name of search engine language<br>optional field<br>if you use this field, you don’t need to specify language_code<br>possible value:<br>English |[optional]|
**language_code** | **StrictStr** | search engine language code<br>optional field<br>if you use this field, you don’t need to specify language_name<br>possible value:<br>en |[optional]|
**device** | **StrictStr** | device type<br>optional field<br>possible value: desktop |[optional]|
**os** | **StrictStr** | device operating system<br>optional field<br>choose from the following values: windows, macos<br>default value: windows |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|
**postback_url** | **StrictStr** | return URL for sending task results<br>optional field<br>once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified<br>you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request<br>example:<br>http://your-server.com/postbackscript?id=$id<br>http://your-server.com/postbackscript?id=$id&tag=$tag<br>Note: special characters in postback_url will be urlencoded;<br>i.a., the # character will be encoded into %23<br>learn more on our Help Center |[optional]|
**postback_data** | **StrictStr** | postback_url datatype<br>required field if you specify postback_url<br>corresponds to the datatype that will be sent to your server<br>possible value: advanced |[optional]|
**pingback_url** | **StrictStr** | notification URL of a completed task<br>optional field<br>when a task is completed we will notify you by GET request sent to the URL you have specified<br>you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.<br>example:<br>http://your-server.com/pingscript?id=$id<br>http://your-server.com/pingscript?id=$id&tag=$tag<br>Note: special characters in pingback_url will be urlencoded;<br>i.a., the # character will be encoded into %23<br>learn more on our Help Center |[optional]|