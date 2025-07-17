# GooglePlaySearchOrganic


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**position** | **StrictStr** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**app_id** | **StrictStr** | id of the app |[optional]|
**title** | **StrictStr** | title of the app |[optional]|
**url** | **StrictStr** | URL to the app page on Google Play |[optional]|
**icon** | **StrictStr** | URL to the app icon |[optional]|
**reviews_count** | **StrictInt** | the total number of reviews of the app |[optional]|
**rating** | **RatingElement** | average rating of the app |[optional]|
**is_free** | **StrictBool** | indicates whether the app is free |[optional]|
**price** | **PriceInfo** | price of the app |[optional]|
**developer** | **StrictStr** | name of the app developer |[optional]|
**developer_url** | **StrictStr** | URL to the developer page on Google Play |[optional]|