# AppStoreSearchOrganic

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**rank_group** | **number** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**position** | **string** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**app_id** | **string** | id of the app |[optional]|
**title** | **string** | title of the app |[optional]|
**url** | **string** | URL to the app page on App Store |[optional]|
**icon** | **string** | URL to the app icon |[optional]|
**reviews_count** | **number** | the total number of reviews of the app |[optional]|
**rating** | **RatingInfo** | average rating of the app |[optional]|
**is_free** | **boolean** | indicates whether the app is free |[optional]|
**price** | **PriceInfo** | price of the app |[optional]|