# BusinessDataGoogleHotelInfoLiveAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**hotel_identifier** | **StrictStr** | <em>identifier received in a POST array</em><br>this field will contain the <code>hotel_identifier</code> parameter specified when setting a task;<br>example:<br><code>CgoI-KWyzenM_MV3EAE</code> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**check_url** | **StrictStr** | <em>direct URL to search engine results</em><br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**title** | **StrictStr** | <em>hotel title</em><br>the title of the hotel entity for which the results are collected |[optional]|
**stars** | **StrictInt** | <em>hotel class rating</em><br>class rating that ranges between 1-5 stars and displayed after review ratings in hotel summary |[optional]|
**stars_description** | **StrictStr** | <em>hotel class rating</em><br>class rating that ranges between 1-5 stars and displayed after review ratings in the hotel summary |[optional]|
**address** | **StrictStr** | <em>hotel address</em><br>physical address of the hotel |[optional]|
**phone** | **StrictStr** | <em>hotel phone number</em><br>contact phone number of the hotel |[optional]|
**about** | **HotelAboutInfo** | <em>information about the hotel</em> |[optional]|
**location** | **HotelLocationInfo** | <em>information about the hotel location</em><br>information about the location where the hotel is located |[optional]|
**reviews** | **HotelReviewInfo** | <em>hotel reviews by criteria</em><br>information about reviews of the hotel entity |[optional]|
**overview_images** | **List[Optional[StrictStr]]** | <em>images displayed in the hotel overview</em><br>array containing URLs to images displayed in the hotel overview |[optional]|
**prices** | **HotelPriceInfo** | <em>pricing details of the hotel entity</em><br>contains information about the hotel's prices |[optional]|