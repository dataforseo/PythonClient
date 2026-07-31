# AppDataAppleAppListingsSearchLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**app_id** | **StrictStr** | <em>ID of the returned app</em> |[optional]|
**se_domain** | **StrictStr** | <em>search engine domain in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**check_url** | **StrictStr** | <em>direct URL to search engine results</em><br>you can use it to make sure that we provided accurate results |[optional]|
**time_update** | **StrictStr** | <em>date and time when SERP data was last updated</em><br>in the <a href='https://en.wikipedia.org/wiki/ISO_8601'>ISO 8601</a> format: “YYYY-MM-DDThh:mm:ss.sssssssZ”<br>example:<br><code class='long-string'>2023-05-23 10:16:19 +00:00</code> |[optional]|
**item** | **AppStoreInfoOrganic** | <em>detailed information about the app</em> |[optional]|