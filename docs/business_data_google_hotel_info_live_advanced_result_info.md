# BusinessDataGoogleHotelInfoLiveAdvancedResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**hotel_identifier** | **StrictStr** | identifier received in a POST array<br>this field will contain the hotel_identifier parameter specified when setting a task;<br>example:<br>CgoI-KWyzenM_MV3EAE |[optional]|
**location_code** | **StrictInt** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**check_url** | **StrictStr** | direct URL to search engine results<br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | date and time when the result was received<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**title** | **StrictStr** | hotel title<br>the title of the hotel entity for which the results are collected |[optional]|
**stars** | **StrictInt** | hotel class rating<br>class rating that ranges between 1-5 stars and displayed after review ratings in hotel summary |[optional]|
**stars_description** | **StrictStr** | hotel class rating<br>class rating that ranges between 1-5 stars and displayed after review ratings in the hotel summary |[optional]|
**address** | **StrictStr** | hotel address<br>physical address of the hotel |[optional]|
**phone** | **StrictStr** | hotel phone number<br>contact phone number of the hotel |[optional]|
**about** | **HotelAboutInfo** | information about the hotel |[optional]|
**location** | **HotelLocationInfo** | information about the hotel location<br>information about the location where the hotel is located |[optional]|
**reviews** | **HotelReviewInfo** | hotel reviews by criteria<br>information about reviews of the hotel entity |[optional]|
**overview_images** | **List[Optional[StrictStr]]** | images displayed in the hotel overview<br>array containing URLs to images displayed in the hotel overview |[optional]|
**prices** | **HotelPriceInfo** | pricing details of the hotel entity<br>contains information about the hotel’s prices |[optional]|