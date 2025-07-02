# AppDataGoogleAppListingsSearchLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**app_id** | **StrictStr** | ID of the returned app |[optional]|
**se_domain** | **StrictStr** | search engine domain in a POST array |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to search engine results<br>you can use it to make sure that we provided accurate results |[optional]|
**time_update** | **StrictStr** | date and time when SERP data was last updated<br>in the ISO 8601 format: “YYYY-MM-DDThh:mm:ss.sssssssZ”<br>example:<br>2023-05-23 10:16:19 +00:00 |[optional]|
**item** | **AppDataGooglePlayInfoOrganicSerpElementItem** | detailed information about the app |[optional]|