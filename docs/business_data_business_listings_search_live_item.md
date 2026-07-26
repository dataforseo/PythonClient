# BusinessDataBusinessListingsSearchLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | <em>title of the element in SERP</em><br>the name of the business entity for which the results are collected |[optional]|
**original_title** | **StrictStr** | <em>original title of the element</em><br>original title not translated by Google |[optional]|
**description** | **StrictStr** | <em>description of the element in SERP</em><br>the description of the business entity for which the results are collected |[optional]|
**category** | **StrictStr** | <em>business category</em><br>Google My Business general category that best describes the services provided by the business entity |[optional]|
**category_ids** | **List[Optional[StrictStr]]** | <em>global category IDs</em><br>universal category IDs that do not change based on the selected country |[optional]|
**additional_categories** | **List[Optional[StrictStr]]** | <em>additional business categories</em><br>additional Google My Business categories that describe the services provided by the business entity in more detail |[optional]|
**cid** | **StrictStr** | <em>google-defined client id</em><br>unique id of a local establishment<br>learn more about the identifier in <a href='https://dataforseo.com/help-center/what-is-cid-place-id-feature-id' target='_blank' rel='noopener noreferrer'>this help center article</a> |[optional]|
**feature_id** | **StrictStr** | <em>the unique identifier of the element in SERP</em><br>learn more about the identifier in <a href='https://dataforseo.com/help-center/what-is-cid-place-id-feature-id' target='_blank' rel='noopener noreferrer'>this help center article</a> |[optional]|
**address** | **StrictStr** | <em>address of the business entity</em> |[optional]|
**address_info** | **AddressInfo** | <em>object containing address components of the business entity</em> |[optional]|
**place_id** | **StrictStr** | <em>unique place identifier</em><br><a href='https://developers.google.com/places/place-id'>place id</a> of the local establishment featured in the element<br>learn more about the identifier in <a href='https://dataforseo.com/help-center/what-is-cid-place-id-feature-id' target='_blank' rel='noopener noreferrer'>this help center article</a> |[optional]|
**phone** | **StrictStr** | <em>phone number of the business entity</em> |[optional]|
**url** | **StrictStr** | <em>absolute url of the business entity</em> |[optional]|
**domain** | **StrictStr** | <em>domain of the business entity</em> |[optional]|
**logo** | **StrictStr** | <em>URL of the logo featured in Google My Business profile</em> |[optional]|
**main_image** | **StrictStr** | <em>URL of the main image featured in Google My Business profile</em> |[optional]|
**total_photos** | **StrictInt** | <em>total count of images featured in Google My Business profile</em> |[optional]|
**snippet** | **StrictStr** | <em>additional information on the business entity</em> |[optional]|
**latitude** | **StrictFloat** | <i>latitude coordinate of the local establishments in google maps</i><br>example:<br><code>'latitude': 51.584091</code> |[optional]|
**longitude** | **StrictFloat** | <i>longitude coordinate of the local establishment in google maps</i><br>example:<br><code>'longitude': -0.31365919999999997</code> |[optional]|
**is_claimed** | **StrictBool** | <i>shows whether the entity is verified by its owner on Google Maps</i> |[optional]|
**attributes** | **BusinessDataAttributesInfo** | <em>service details in a form of user-reviewed checks;</em><br>service details of a business entity displayed in a form of checks and based on user feedback and business <code>category</code> |[optional]|
**place_topics** | **Dict[str, Optional[StrictInt]]** | <em>keywords mentioned in customer reviews</em><br>contains most popular keywords related to products/services mentioned in customer reviews of a business entity and the number of reviews mentioning each keyword<br>example: <code><br>'place_topics': {<br>'egg roll': 48,<br>'birthday': 33<br>}</code> |[optional]|
**rating** | **RatingInfo** | <em>the element's rating </em><br>the popularity rate based on reviews and displayed in SERP |[optional]|
**hotel_rating** | **StrictInt** | <em>hotel class rating</em><br>class ratings range between 1-5 stars, <a href='https://support.google.com/business/answer/7660515?hl=en' rel='noopener noreferrer' target='_blank'>learn more</a><br>if there is no hotel class rating information, the value will be <code>null</code> |[optional]|
**price_level** | **StrictStr** | <em>property price level</em><br>can take values: <code>inexpensive</code>, <code>moderate</code>, <code>expensive</code>, <code>very_expensive</code><br>if there is no price level information, the value will be <code>null</code> |[optional]|
**rating_distribution** | **Dict[str, Optional[StrictInt]]** | <em>the distribution of ratings of the business entity</em><br>the object displays the number of 1-star to 5-star ratings, as reviewed by users |[optional]|
**people_also_search** | **List[Optional[PeopleAlsoSearch]]** | <em>related business entities</em> |[optional]|
**work_time** | **BusinessWorkHoursInfo** | <em>work time details</em><br>information related to operational hours of the business entity |[optional]|
**popular_times** | **PopularTimes** | <em>popular times</em><br>information related to busy hours of the business entity |[optional]|
**local_business_links** | **List[Optional[BaseLocalBusinessLink]]** | <em>available interactions with the business</em><br>list of options to interact with the business directly from search results |[optional]|
**contact_info** | **List[Optional[BusinessDataContactInfo]]** | <em>available contacts of the business</em><br>list of contacts to interact with the business |[optional]|
**check_url** | **StrictStr** | <em>direct URL to search engine results</em><br>you can use it to make sure that we provided accurate results |[optional]|
**last_updated_time** | **StrictStr** | <em>date and time when the data was last updated</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code>2023-01-26 09:03:15 +00:00</code> |[optional]|
**first_seen** | **StrictStr** | <em>date and time when our crawler found the business listing element for the first time</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code>2023-03-11 10:04:11 +00:00</code> |[optional]|
**services** | **List[Optional[BusinessDataServiceInfo]]** |  |[optional]|