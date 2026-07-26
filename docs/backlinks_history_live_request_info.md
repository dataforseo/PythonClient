# BacklinksHistoryLiveRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**target** | **StrictStr** | <em>domain</em><br><strong>required field</strong><br>a domain should be specified without <code>https://</code> and <code>www.</code> |[optional]|
**date_from** | **StrictStr** | <em>starting date of the time range</em><br>optional field<br>minimum value <code>2019-01-01</code><br>if you don't specify this field, the minimum value will be used by default<br>date format: <code>'yyyy-mm-dd'</code><br>example:<br><code>'2019-01-15'</code> |[optional]|
**date_to** | **StrictStr** | <em>ending date of the time range</em><br>optional field<br>if you don't specify this field, the today's date will be used by default<br>date format: <code>'yyyy-mm-dd'</code><br>example:<br><code>'2019-01-15'</code> |[optional]|
**rank_scale** | **StrictStr** | <em>defines the scale used for calculating and displaying the <code>rank</code>, <code>domain_from_rank</code>, and <code>page_from_rank</code> values</em><br>optional field<p>you can use this parameter to choose whether rank values are presented on a 0–100 or 0–1000 scale<p>possible values:<br><code>one_hundred</code> — rank values are displayed on a 0–100 scale<br><code>one_thousand</code> — rank values are displayed on a 0–1000 scale<p>default value: <code>one_thousand</code><p>learn more about how this parameter works and how ranking metrics are calculated in <a href='https://dataforseo.com/help-center/what_is_rank_in_backlinks_api#rank_scale'>this Help Center article</a> |[optional]|
**tag** | **StrictStr** | <em>user-defined task identifier</em><br>optional field<br><em>the character limit is 255</em><br>you can use this parameter to identify the task and match it with the result<br>you will find the specified <code>tag</code> value in the <code>data</code> object of the response |[optional]|