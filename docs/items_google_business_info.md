# ItemsGoogleBusinessInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>position within a group of elements with identical <code>type</code> values</em><br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank among all the elements</em> |[optional]|
**position** | **StrictStr** | <em>the alignment in SERP</em> |[optional]|
**title** | **StrictStr** | <em>title of the element in SERP</em><br>the name of the business entity for which the results are collected |[optional]|
**original_title** | **StrictStr** | <em>original title of the element</em><br>original title not translated by Google |[optional]|
**description** | **StrictStr** | <em>description of the element in SERP</em><br>the description of the business entity for which the results are collected |[optional]|
**category** | **StrictStr** | <em>business category</em><br>Google My Business general category that best describes the services provided by the business entity |[optional]|
**category_ids** | **List[Optional[StrictStr]]** | <em>global category IDs</em><br>universal category IDs that do not change based on the selected country |[optional]|
**additional_categories** | **List[Optional[StrictStr]]** | <em>additional business categories</em><br>additional Google My Business categories that describe the services provided by the business entity in more detail |[optional]|
**cid** | **StrictStr** | <em>google-defined client id</em><br>unique id of a local establishment;<br>can be used with <a href='/v3/reviews/google/overview/?php' target='_blank' rel='noopener noreferrer'>Google Reviews API</a> to get a full list of reviews<br>learn more about the identifier in <a href='https://dataforseo.com/help-center/what-is-cid-place-id-feature-id' target='_blank' rel='noopener noreferrer'>this help center article</a> |[optional]|
**feature_id** | **StrictStr** | <em>the unique identifier of the element in SERP</em><br>learn more about the identifier in <a href='https://dataforseo.com/help-center/what-is-cid-place-id-feature-id' target='_blank' rel='noopener noreferrer'>this help center article</a> |[optional]|
**address** | **StrictStr** | <em>address of the business entity</em> |[optional]|
**address_info** | **AddressInfo** | <em>object containing address components of the business entity</em> |[optional]|
**place_id** | **StrictStr** | <em>unique place identifier</em><br><a href='https://developers.google.com/places/place-id'>place id</a> of the local establishment featured in the element<br>learn more about the identifier in <a href='https://dataforseo.com/help-center/what-is-cid-place-id-feature-id' target='_blank' rel='noopener noreferrer'>this help center article</a> |[optional]|
**phone** | **StrictStr** | <em>phone number of the business entity</em> |[optional]|
**url** | **StrictStr** | <em>absolute url of the business entity</em> |[optional]|
**contact_url** | **StrictStr** | <em>URL of the preferred contact page</em> |[optional]|
**contributor_url** | **StrictStr** | <em>URL of the user's or entity's Local Guides profile, if available</em> |[optional]|
**book_online_url** | **StrictStr** | <em>URL in the 'book online' button of the element</em><br>URL directing users to the online booking or order page of the business entity |[optional]|
**domain** | **StrictStr** | <em>domain of the business entity</em> |[optional]|
**logo** | **StrictStr** | <em>URL of the logo featured in Google My Business profile</em> |[optional]|
**main_image** | **StrictStr** | <em>URL of the main image featured in Google My Business profile</em> |[optional]|
**total_photos** | **StrictInt** | <em>total count of images featured in Google My Business profile</em> |[optional]|
**snippet** | **StrictStr** | <em>additional information on the business entity</em> |[optional]|
**latitude** | **StrictFloat** | <i>latitude coordinate of the local establishments in google maps</i><br>example:<br><code>'latitude': 51.584091</code> |[optional]|
**longitude** | **StrictFloat** | <i>longitude coordinate of the local establishment in google maps</i><br>example:<br><code>'longitude': -0.31365919999999997</code> |[optional]|
**is_claimed** | **StrictBool** | <i>shows whether the entity is verified by its owner on Google Maps</i> |[optional]|
**attributes** | **BusinessDataAttributesInfo** | <em>service details in a form of user-reviewed checks;</em><br>service details of a business entity displayed in a form of checks and based on user feedback and business <code>category</code> |[optional]|
**place_topics** | **Dict[str, Optional[StrictInt]]** | <em>keywords mentioned in customer reviews</em><br>contains most popular keywords related to products/services mentioned in customer reviews of a business entity and the number of reviews mentioning each keyword<br>example:<br> <code><br>'place_topics': {<br>'egg roll': 48,<br>'birthday': 33<br>}</code> |[optional]|
**rating** | **RatingInfo** | <em>the element's rating </em><br>the popularity rate based on reviews and displayed in SERP |[optional]|
**hotel_rating** | **StrictStr** | <em>hotel class rating</em><br>class ratings range between 1-5 stars, <a href='https://support.google.com/business/answer/7660515?hl=en' rel='noopener noreferrer' target='_blank'>learn more</a><br>if there is no hotel class rating information, the value will be <code>null</code> |[optional]|
**price_level** | **StrictStr** | <em>property price level</em><br>can take values: <code>inexpensive</code>, <code>moderate</code>, <code>expensive</code>, <code>very_expensive</code><br>if there is no price level information, the value will be <code>null</code> |[optional]|
**rating_distribution** | **Dict[str, Optional[StrictInt]]** | <em>the distribution of ratings of the business entity</em><br>the object displays the number of 1-star to 5-star ratings, as reviewed by users |[optional]|
**people_also_search** | **List[Optional[PeopleAlsoSearch]]** | <em>related business entities</em> |[optional]|
**work_time** | **BusinessWorkHoursInfo** | <em>work time details</em><br>information related to operational hours of the business entity |[optional]|
**popular_times** | **Any** | <em>popular times</em><br>information related to busy hours of the business entity |[optional]|
**local_business_links** | **Any** | <em>available interactions with the business</em><br>list of options to interact with the business directly from search results |[optional]|
**is_directory_item** | **StrictBool** | <em>business establishment is a part of the directory</em><br>indicates whether the business establishment is a part of the directory;<br>if <code>true</code>, the item is a part of the larger directory of businesses with the same address (e.g., a mall or a business centre);<br><strong>note:</strong> if the business establishment is a parent item in the directory, the value will be <code>null</code> |[optional]|
**directory** | **Any** | <em>items of the directory</em><br>includes information about businesses that are located within the target business establishment and have the same address |[optional]|
**services** | **List[Optional[BusinessDataServiceInfo]]** | <em>list of services offered by the business</em> |[optional]|