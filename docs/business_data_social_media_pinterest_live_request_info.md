# BusinessDataSocialMediaPinterestLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**targets** | **List[Optional[StrictStr]]** | target URLs<br>required field<br>target page should be specified with its absolute URL (including http:// or https://)<br>example:<br>https://dataforseo.com/<br>Note: you can specify 10 targets maximum. You will be charged per earch URL you specify in this array |[optional]|
**tag** | **StrictStr** | user-defined task identifier<br>optional field<br>the character limit is 255<br>you can use this parameter to identify the task and match it with the result<br>you will find the specified tag value in the data object of the response |[optional]|