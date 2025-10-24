# SerpGoogleAiModeLiveHtmlResultInfo

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **string** | keyword received in a POST array<br>keyword is returned with decoded %## (plus character ‘+’ will be decoded to a space character) |[optional]|
**type** | **string** | type of element |[optional]|
**se_domain** | **string** | search engine domain in a POST array |[optional]|
**location_code** | **number** | location code in a POST array |[optional]|
**language_code** | **string** | language code in a POST array |[optional]|
**datetime** | **string** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**items_count** | **number** | the number of results returned in the items array |[optional]|
**items** | **HtmlItemInfo[]** | elements of search results found in SERP |[optional]|