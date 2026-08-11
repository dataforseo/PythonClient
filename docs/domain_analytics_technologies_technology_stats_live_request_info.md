# DomainAnalyticsTechnologiesTechnologyStatsLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**technology** | **StrictStr** | <em>target technology</em><br><strong>required field</strong><br>you can find the full list of technologies you can specify here <a href='/v3/domain_analytics/technologies/technologies' target='_blank' rel='noopener noreferrer'>on this page</a><br>example:<br><code>'Salesforce'</code> |[optional]|
**date_from** | **StrictStr** | <em>starting date of the time range</em><br>optional field<br>minimum value: <code>2022-10-31</code><br>if you don't specify this field, the minimum value will be used by default<br>date format: <code>'yyyy-mm-dd'</code><br>example:<br><code>'2023-06-01'</code> |[optional]|
**date_to** | **StrictStr** | <em>ending date of the time range</em><br>optional field<br>if you don't specify this field, the today's date will be used by default<br>date format: <code>'yyyy-mm-dd'</code><br>example:<br><code>'2023-01-15'</code> |[optional]|
**tag** | **StrictStr** | <em>user-defined task identifier</em><br>optional field<br><em>the character limit is 255</em><br>you can use this parameter to identify the task and match it with the result<br>you will find the specified <code>tag</code> value in the <code>data</code> object of the response |[optional]|