# AppStoreInfoOrganic


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>position within a group of elements with identical <code>type</code> values</em><br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank among all the listed apps</em><br>absolute position among all apps on the list |[optional]|
**position** | **StrictStr** | <em>the alignment of the element in SERP</em><br>can take the following values: <code>left</code> |[optional]|
**app_id** | **StrictStr** | <em>ID of the app</em> |[optional]|
**title** | **StrictStr** | <em>title of the app</em> |[optional]|
**subtitle** | **StrictStr** | <em>subtitle of the app</em> |[optional]|
**url** | **StrictStr** | <em>URL to the app page on App Store</em> |[optional]|
**icon** | **StrictStr** | <em>URL to the app icon</em> |[optional]|
**description** | **StrictStr** | <em>description of the app</em> |[optional]|
**reviews_count** | **StrictInt** | <em>the total number of reviews of the app</em> |[optional]|
**rating** | **RatingInfo** | <em>average rating of the app</em> |[optional]|
**price** | **PriceInfo** | <em>price of the app</em> |[optional]|
**is_free** | **StrictBool** | <em>indicates whether the app is free</em> |[optional]|
**main_category** | **StrictStr** | <em>main category/genre of the app</em> |[optional]|
**categories** | **List[Optional[StrictStr]]** | <em>all relevant categories/genres of the app</em><br><strong>Note:</strong> this field returns only one relevant category in the array |[optional]|
**languages** | **List[Optional[StrictStr]]** | <em>languages supported in the app</em><br><strong>Note:</strong> this field returns only one supported language in the array |[optional]|
**advisories** | **List[Optional[StrictStr]]** | <em>age rating and age-based content advisories</em> |[optional]|
**developer** | **StrictStr** | <em>name of the app developer</em> |[optional]|
**developer_id** | **StrictStr** | <em>ID of the app developer</em> |[optional]|
**developer_url** | **StrictStr** | <em>URL to the developer page on App Store</em> |[optional]|
**version** | **StrictStr** | <em>current version of the app</em> |[optional]|
**minimum_os_version** | **StrictStr** | <em>minimum OS version required to install the app</em> |[optional]|
**size** | **StrictStr** | <em>size of the app</em> |[optional]|
**released_date** | **StrictStr** | <em>date and time when the app was released</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br><code>2019-11-15 12:57:46 +00:00</code><br><strong>Note:</strong> this field is deprecated and always returns <code>null</code> |[optional]|
**last_update_date** | **StrictStr** | <em>date and time when the app was last updated</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br><code>2019-11-15 12:57:46 +00:00</code> |[optional]|
**update_notes** | **StrictStr** | <em>update notes</em><br>contains the latest update notes from the developer |[optional]|
**images** | **List[Optional[StrictStr]]** | <em>app images</em><br>contains URLs to the images used on the app page on App Store |[optional]|
**similar_apps** | **List[Optional[AppsInfo]]** | <em>similar apps</em><br>displays apps similar to the app in a POST request |[optional]|
**more_apps_by_developer** | **List[Optional[AppsInfo]]** | <em>similar apps</em><br>information about apps built by the same developer |[optional]|