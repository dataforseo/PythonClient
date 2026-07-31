# BusinessDataSocialMediaPinterestLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**targets** | **List[Optional[StrictStr]]** | <em>target URLs</em><br><strong>required field</strong><br>target page should be specified with its absolute URL (including http:// or https://)<br>example:<br><code>https://dataforseo.com/</code><p><strong>Note:</strong> you can specify 10 targets maximum. You will be charged per earch URL you specify in this array |[optional]|
**tag** | **StrictStr** | <em>user-defined task identifier</em><br>optional field<br><em>the character limit is 255</em><br>you can use this parameter to identify the task and match it with the result<br>you will find the specified <code>tag</code> value in the <code>data</code> object of the response |[optional]|