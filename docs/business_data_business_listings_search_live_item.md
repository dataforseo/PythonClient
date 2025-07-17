# BusinessDataBusinessListingsSearchLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | title of the element in SERP<br>the name of the business entity for which the results are collected |[optional]|
**original_title** | **StrictStr** | original title of the element<br>original title not translated by Google |[optional]|
**description** | **StrictStr** | description of the element in SERP<br>the description of the business entity for which the results are collected |[optional]|
**category** | **StrictStr** | business category<br>Google My Business general category that best describes the services provided by the business entity |[optional]|
**category_ids** | **List[Optional[StrictStr]]** | global category IDs<br>universal category IDs that do not change based on the selected country |[optional]|
**additional_categories** | **List[Optional[StrictStr]]** | additional business categories<br>additional Google My Business categories that describe the services provided by the business entity in more detail |[optional]|
**cid** | **StrictStr** | google-defined client id<br>unique id of a local establishment<br>learn more about the identifier in this help center article |[optional]|
**feature_id** | **StrictStr** | the unique identifier of the element in SERP<br>learn more about the identifier in this help center article |[optional]|
**address** | **StrictStr** | address of the business entity |[optional]|
**address_info** | **AddressInfo** | object containing address components of the business entity |[optional]|
**place_id** | **StrictStr** | unique place identifier<br>place id of the local establishment featured in the element<br>learn more about the identifier in this help center article |[optional]|
**phone** | **StrictStr** | phone number of the business entity |[optional]|
**url** | **StrictStr** | absolute url of the business entity |[optional]|
**domain** | **StrictStr** | domain of the business entity |[optional]|
**logo** | **StrictStr** | URL of the logo featured in Google My Business profile |[optional]|
**main_image** | **StrictStr** | URL of the main image featured in Google My Business profile |[optional]|
**total_photos** | **StrictInt** | total count of images featured in Google My Business profile |[optional]|
**snippet** | **StrictStr** | additional information on the business entity |[optional]|
**latitude** | **StrictFloat** | latitude coordinate of the local establishments in google maps<br>example:<br>'latitude': 51.584091 |[optional]|
**longitude** | **StrictFloat** | longitude coordinate of the local establishment in google maps<br>example:<br>'longitude': -0.31365919999999997 |[optional]|
**is_claimed** | **StrictBool** | shows whether the entity is verified by its owner on Google Maps |[optional]|
**attributes** | **BusinessDataAttributesInfo** | service details in a form of user-reviewed checks;<br>service details of a business entity displayed in a form of checks and based on user feedback and business category |[optional]|
**place_topics** | **Dict[str, Optional[StrictInt]]** | keywords mentioned in customer reviews<br>contains most popular keywords related to products/services mentioned in customer reviews of a business entity and the number of reviews mentioning each keyword<br>example: <br>'place_topics': {<br>'egg roll': 48,<br>'birthday': 33<br>} |[optional]|
**rating** | **RatingInfo** | the element’s rating <br>the popularity rate based on reviews and displayed in SERP |[optional]|
**hotel_rating** | **StrictInt** | hotel class rating<br>class ratings range between 1-5 stars, learn more<br>if there is no hotel class rating information, the value will be null |[optional]|
**price_level** | **StrictStr** | property price level<br>can take values: inexpensive, moderate, expensive, very_expensive<br>if there is no price level information, the value will be null |[optional]|
**rating_distribution** | **Dict[str, Optional[StrictInt]]** | the distribution of ratings of the business entity<br>the object displays the number of 1-star to 5-star ratings, as reviewed by users |[optional]|
**people_also_search** | **List[Optional[PeopleAlsoSearch]]** | related business entities |[optional]|
**work_time** | **BusinessWorkHoursInfo** | work time details<br>information related to operational hours of the business entity |[optional]|
**popular_times** | **PopularTimes** | popular times<br>information related to busy hours of the business entity |[optional]|
**local_business_links** | **List[Optional[BaseLocalBusinessLink]]** | available interactions with the business<br>list of options to interact with the business directly from search results |[optional]|
**contact_info** | **List[Optional[BusinessDataContactInfo]]** | available contacts of the business<br>list of contacts to interact with the business |[optional]|
**check_url** | **StrictStr** | direct URL to search engine results<br>you can use it to make sure that we provided accurate results |[optional]|
**last_updated_time** | **StrictStr** | date and time when the data was last updated<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2023-01-26 09:03:15 +00:00 |[optional]|
**first_seen** | **StrictStr** | date and time when our crawler found the business listing element for the first time<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2023-03-11 10:04:11 +00:00 |[optional]|