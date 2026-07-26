# SerpGoogleDatasetInfoLiveAdvancedRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**dataset_id** | **StrictStr** | <p><em>ID of the dataset</em><p><strong>required field</strong><p>you can find dataset ID in the dataset URL or <code>dataset</code> item of <a href='https://docs.dataforseo.com/v3/serp/google/dataset_search/live/advanced'>Google Dataset Search</a> result<p>example:<p><code>L2cvMTFqbl85ZHN6MQ==</code></p> |[optional]|
**language_code** | **StrictStr** | <p><em>search engine language code</em><p>optional field<p>if you use this field, you don't need to specify <code>language_name</code><p>possible value:<p><code class='long-string'>en</code></p> |[optional]|
**device** | **StrictStr** | <p><em>device type</em><p>optional field<p>return results for a specific device type<p>possible value: <code>desktop</code></p> |[optional]|
**language_name** | **StrictStr** | <p><em>full name of search engine language</em><p>optional field<p>if you use this field, you don't need to specify <code>language_code</code><p>possible value:<p><code class='long-string'>English</code></p> |[optional]|
**os** | **StrictStr** | <p><em>device operating system</em><p>optional field<p>possible values: <code>windows</code>, <code>macos</code><p>default value: <code>windows</code></p> |[optional]|
**tag** | **StrictStr** | <p><em>user-defined task identifier</em><p>optional field<p><em>the character limit is 255</em><p>you can use this parameter to identify the task and match it with the result<p>you will find the specified <code>tag</code> value in the <code>data</code> object of the response</p> |[optional]|