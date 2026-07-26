# BusinessDataGoogleHotelInfoLiveHtmlResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | <em>unique hotel identifier specified as <code>'hotel_id:$'</code></em> |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** |  |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <strong><code>items</code></strong> array</em> |[optional]|
**items** | **List[Optional[HtmlItemInfo]]** | <em>HTML pages</em> |[optional]|