# MapsSearch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>position within a group of elements with identical <code>type</code> values</em><br>positions of elements with different <code>type</code> values are omitted from the <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank among all the elements</em> |[optional]|
**domain** | **StrictStr** | <em>domain of the business entity</em> |[optional]|
**title** | **StrictStr** | <em>directory title</em><br>can take the following values: <code>At this place</code>, <code>Directory</code> |[optional]|
**url** | **StrictStr** | <em>URL to view the menu</em> |[optional]|
**rating** | **RatingInfo** | <em>the element's rating </em><br>the popularity rate based on reviews and displayed in SERP |[optional]|
**rating_distribution** | **Dict[str, Optional[StrictInt]]** | the distribution of ratings of the business entity<br>the object displays the number of 1-star to 5-star ratings, as reviewed by users |[optional]|
**snippet** | **StrictStr** | <em>additional information about the business entity</em> |[optional]|
**address** | **StrictStr** | <em>address of the business entity</em> |[optional]|
**address_info** | **AddressInfo** | <em>object containing address components of the business entity</em> |[optional]|
**place_id** | **StrictStr** | <em>unique place identifier</em><br><a href='https://developers.google.com/places/place-id'>place id</a> of the local establishment featured in the element<br>learn more about the identifier in <a href='https://dataforseo.com/help-center/what-is-cid-place-id-feature-id' target='_blank' rel='noopener noreferrer'>this help center article</a> |[optional]|
**phone** | **StrictStr** | <em>phone number of the business entity</em> |[optional]|
**main_image** | **StrictStr** | <em>URL of the main image featured in Google My Business profile</em> |[optional]|
**total_photos** | **StrictStr** | <em>total count of images featured in Google My Business profile</em> |[optional]|
**category** | **StrictStr** | <em>business category</em><br>Google My Business general category that best describes the services provided by the business entity |[optional]|
**additional_categories** | **List[Optional[StrictStr]]** | <em>additional business categories</em><br>additional Google My Business categories that describe the services provided by the business entity in more detail |[optional]|
**price_level** | **StrictStr** | <em>property price level</em><br>can take values: <code>inexpensive</code>, <code>moderate</code>, <code>expensive</code>, <code>very_expensive</code><br>if there is no price level information, the value will be <code>null</code> |[optional]|
**hotel_rating** | **StrictStr** | <em>hotel class rating</em><br>class ratings range between 1-5 stars, <a href='https://support.google.com/business/answer/7660515?hl=en' rel='noopener noreferrer' target='_blank'>learn more</a><br>if there is no hotel class rating information, the value will be <code>null</code> |[optional]|
**category_ids** | **List[Optional[StrictStr]]** | <em>global category IDs</em><br>universal category IDs that do not change based on the selected country |[optional]|
**work_hours** | **BusinessWorkHoursInfo** | <em>open hours</em><br>information about work hours of the local establishment |[optional]|
**feature_id** | **StrictStr** | <em>the unique identifier of the element in SERP</em><br>learn more about the identifier in <a href='https://dataforseo.com/help-center/what-is-cid-place-id-feature-id' target='_blank' rel='noopener noreferrer'>this help center article</a> |[optional]|
**cid** | **StrictStr** | <em>google-defined client id</em><br>unique id of a local establishment;<br>can be used with <a href='/v3/reviews/google/overview/?php' target='_blank' rel='noopener noreferrer'>Google Reviews API</a> to get a full list of reviews<br>learn more about the identifier in <a href='https://dataforseo.com/help-center/what-is-cid-place-id-feature-id' target='_blank' rel='noopener noreferrer'>this help center article</a> |[optional]|
**latitude** | **StrictFloat** | <i>latitude coordinate of the local establishments in google maps</i><br>example:<br><code>'latitude': 51.584091</code> |[optional]|
**longitude** | **StrictFloat** | <i>longitude coordinate of the local establishment in google maps</i><br>example:<br><code>'longitude': -0.31365919999999997</code> |[optional]|
**is_claimed** | **StrictBool** | <i>shows whether the entity is verified by its owner on Google Maps</i> |[optional]|
**local_justifications** | **List[Optional[StrictStr]]** | <em>Google local justifications</em><br>snippets of text that “justify” why the business is showing up for search query |[optional]|
**is_directory_item** | **StrictBool** | <em>business establishment is a part of the directory</em><br>indicates whether the business establishment is a part of the directory;<br>if <code>true</code>, the item is a part of the larger directory of businesses with the same address (e.g., a mall or a business centre);<br><strong>note:</strong> if the business establishment is a parent item in the directory, the value will be <code>null</code> |[optional]|