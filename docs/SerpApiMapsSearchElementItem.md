# SerpApiMapsSearchElementItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**original_title** | **string** | original title of the element<br>original title not translated by Google |[optional]|
**contact_url** | **string** | URL of the preferred contact page |[optional]|
**contributor_url** | **string** | URL of the user’s or entity’s Local Guides profile, if available |[optional]|
**book_online_url** | **string** | URL in the ‘book online’ button of the element<br>URL directing users to the online booking or order page of the business entity |[optional]|
**hotel_rating** | **number** | hotel class rating<br>class ratings range between 1-5 stars, learn more<br>if there is no hotel class rating information, the value will be null |[optional]|
**price_level** | **string** | property price level<br>can take values: inexpensive, moderate, expensive, very_expensive<br>if there is no price level information, the value will be null |[optional]|
**snippet** | **string** | element snippet<br>contains the address and other information about the local establishment featured in the element |[optional]|
**address** | **string** | address line<br>address of the local establishment featured in the element |[optional]|
**address_info** | **AddressInfo** | object containing address components of the local establishment |[optional]|
**place_id** | **string** | unique place identifier<br>place id of the local establishment featured in the element |[optional]|
**phone** | **string** | phone number<br>phone number of the local establishment featured in the element |[optional]|
**main_image** | **string** | URL of the main image featured in Google My Business profile |[optional]|
**total_photos** | **number** | total count of images featured in Google My Business profile |[optional]|
**category** | **string** | business category<br>Google My Business general category that best describes the services provided by the business entity |[optional]|
**additional_categories** | **string[]** | additional business categories<br>additional Google My Business categories that describe the services provided by the business entity in more detail |[optional]|
**category_ids** | **string[]** | global category IDs<br>universal category IDs that do not change based on the selected country |[optional]|
**work_hours** | **WorkHours** | open hours<br>information about work hours of the local establishment |[optional]|
**feature_id** | **string** | the unique identifier of the element in SERP |[optional]|
**cid** | **string** | google-defined client id<br>unique id of a local establishment;<br>can be used with Google Reviews API to get a full list of reviews |[optional]|
**latitude** | **number** | latitude coordinate of the local establishments in google maps<br>example:<br>'latitude': 51.584091 |[optional]|
**longitude** | **number** | longitude coordinate of the local establishment in google maps<br>example:<br>'longitude': -0.31365919999999997 |[optional]|
**is_claimed** | **boolean** | indicates whether ownership of this local establishment is claimed |[optional]|
**local_justifications** | **LocalJustificationInfo[]** | Google local justifications<br>snippets of text that “justify” why the business is showing up for search query |[optional]|
**is_directory_item** | **boolean** | indicates whether this local establishment is a directory |[optional]|