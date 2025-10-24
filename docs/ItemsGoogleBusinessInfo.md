# ItemsGoogleBusinessInfo

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**rank_group** | **number** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank among all the elements |[optional]|
**position** | **string** | the alignment in SERP |[optional]|
**title** | **string** | title of the element in SERP<br>the name of the business entity for which the results are collected |[optional]|
**original_title** | **string** | original title of the element<br>original title not translated by Google |[optional]|
**description** | **string** | description of the element in SERP<br>the description of the business entity for which the results are collected |[optional]|
**category** | **string** | business category<br>Google My Business general category that best describes the services provided by the business entity |[optional]|
**category_ids** | **string[]** | global category IDs<br>universal category IDs that do not change based on the selected country |[optional]|
**additional_categories** | **string[]** | additional business categories<br>additional Google My Business categories that describe the services provided by the business entity in more detail |[optional]|
**cid** | **string** | google-defined client id<br>unique id of a local establishment;<br>can be used with Google Reviews API to get a full list of reviews<br>learn more about the identifier in this help center article |[optional]|
**feature_id** | **string** | the unique identifier of the element in SERP<br>learn more about the identifier in this help center article |[optional]|
**address** | **string** | address of the business entity |[optional]|
**address_info** | **AddressInfo** | object containing address components of the business entity |[optional]|
**place_id** | **string** | unique place identifier<br>place id of the local establishment featured in the element<br>learn more about the identifier in this help center article |[optional]|
**phone** | **string** | phone number of the business entity |[optional]|
**url** | **string** | absolute url of the business entity |[optional]|
**contact_url** | **string** | URL of the preferred contact page |[optional]|
**contributor_url** | **string** | URL of the user’s or entity’s Local Guides profile, if available |[optional]|
**book_online_url** | **string** | URL in the ‘book online’ button of the element<br>URL directing users to the online booking or order page of the business entity |[optional]|
**domain** | **string** | domain of the business entity |[optional]|
**logo** | **string** | URL of the logo featured in Google My Business profile |[optional]|
**main_image** | **string** | URL of the main image featured in Google My Business profile |[optional]|
**total_photos** | **number** | total count of images featured in Google My Business profile |[optional]|
**snippet** | **string** | additional information on the business entity |[optional]|
**latitude** | **number** | latitude coordinate of the local establishments in google maps<br>example:<br>'latitude': 51.584091 |[optional]|
**longitude** | **number** | longitude coordinate of the local establishment in google maps<br>example:<br>'longitude': -0.31365919999999997 |[optional]|
**is_claimed** | **boolean** | shows whether the entity is verified by its owner on Google Maps |[optional]|
**attributes** | **BusinessDataAttributesInfo** | service details in a form of user-reviewed checks;<br>service details of a business entity displayed in a form of checks and based on user feedback and business category |[optional]|
**place_topics** | **{ [key: string]: number; }** | keywords mentioned in customer reviews<br>contains most popular keywords related to products/services mentioned in customer reviews of a business entity and the number of reviews mentioning each keyword<br>example: <br>'place_topics': {<br>'egg roll': 48,<br>'birthday': 33<br>} |[optional]|
**rating** | **RatingInfo** | the element’s rating <br>the popularity rate based on reviews and displayed in SERP |[optional]|
**hotel_rating** | **string** | hotel class rating<br>class ratings range between 1-5 stars, learn more<br>if there is no hotel class rating information, the value will be null |[optional]|
**price_level** | **string** | property price level<br>can take values: inexpensive, moderate, expensive, very_expensive<br>if there is no price level information, the value will be null |[optional]|
**rating_distribution** | **{ [key: string]: number; }** | the distribution of ratings of the business entity<br>the object displays the number of 1-star to 5-star ratings, as reviewed by users |[optional]|
**people_also_search** | **PeopleAlsoSearch[]** | related business entities |[optional]|
**work_time** | **BusinessWorkHoursInfo** | work time details<br>information related to operational hours of the business entity |[optional]|
**popular_times** | **any** | popular times<br>information related to busy hours of the business entity |[optional]|
**local_business_links** | **any** | available interactions with the business<br>list of options to interact with the business directly from search results |[optional]|
**is_directory_item** | **boolean** | business establishment is a part of the directory<br>indicates whether the business establishment is a part of the directory;<br>if true, the item is a part of the larger directory of businesses with the same address (e.g., a mall or a business centre);<br>note: if the business establishment is a parent item in the directory, the value will be null |[optional]|
**directory** | **any** | items of the directory<br>includes information about businesses that are located within the target business establishment and have the same address |[optional]|