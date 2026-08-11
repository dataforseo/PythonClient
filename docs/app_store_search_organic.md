# AppStoreSearchOrganic


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>position within a group of elements with identical <code>type</code> values</em><br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in SERP</em><br>absolute position among all the elements in SERP |[optional]|
**position** | **StrictStr** | <em>the alignment of the element in SERP</em><br>can take the following values:<br><code>left</code>, <code>right</code> |[optional]|
**app_id** | **StrictStr** | <em>id of the app in a POST array</em> |[optional]|
**title** | **StrictStr** | <em>title of the app</em> |[optional]|
**url** | **StrictStr** | <em>URL to the app page on App Store</em> |[optional]|
**icon** | **StrictStr** | <em>URL to the app icon</em> |[optional]|
**reviews_count** | **StrictInt** | <em>the total number of reviews of the app</em> |[optional]|
**rating** | **RatingInfo** | <em>average rating of the app</em> |[optional]|
**is_free** | **StrictBool** | <em>indicates whether the app is free</em> |[optional]|
**price** | **PriceInfo** | <em>pricing information for the app</em> |[optional]|