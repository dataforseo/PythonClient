# KeywordsDataClickstreamDataDataforseoSearchVolumeLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**location_code** | **StrictInt** | <em>location code in a POST array</em><br>if there is no data, then the value is <code>null</code> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array<br></em><br><strong>Note:</strong>if the keyword in the POST array appears to be misspelled, data will be returned for the correctly spelled keyword;<br>we use the functionality of Google Ads API to check and validate the spelling of keywords, <a href='https://support.google.com/google-ads/answer/7476658' target='_blank' rel='noopener noreferrer'>learn more by this link</a> |[optional]|
**use_clickstream** | **StrictBool** | <em>indicates if the <code>use_clickstream</code> parameter is active</em><br>possible values: <code>true</code>, <code>false</code> |[optional]|
**items_count** | **StrictInt** | <em>ithe number of results returned in the <code>items</code> array</em> |[optional]|
**items** | **List[Optional[KeywordsDataClickstreamDataSearchVolumeLiveItem]]** | <em>array of keywords</em><br>contains keywords and their search volume rates |[optional]|