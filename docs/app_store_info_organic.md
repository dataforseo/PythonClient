# AppStoreInfoOrganic


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank among all the listed apps<br>absolute position among all apps on the list |[optional]|
**position** | **StrictStr** | the alignment of the element in SERP<br>can take the following values: left |[optional]|
**app_id** | **StrictStr** | ID of the app |[optional]|
**title** | **StrictStr** | title of the app |[optional]|
**url** | **StrictStr** | URL to the app page on App Store |[optional]|
**icon** | **StrictStr** | URL to the app icon |[optional]|
**description** | **StrictStr** | description of the app |[optional]|
**reviews_count** | **StrictInt** | the total number of reviews of the app |[optional]|
**rating** | **RatingInfo** | average rating of the app |[optional]|
**price** | **PriceInfo** | price of the app |[optional]|
**is_free** | **StrictBool** | indicates whether the app is free |[optional]|
**main_category** | **StrictStr** | main category/genre of the app |[optional]|
**categories** | **List[Optional[StrictStr]]** | all relevant categories/genres of the app |[optional]|
**languages** | **List[Optional[StrictStr]]** | languages supported in the app |[optional]|
**advisories** | **List[Optional[StrictStr]]** | age rating and age-based content advisories |[optional]|
**developer** | **StrictStr** | name of the app developer |[optional]|
**developer_id** | **StrictStr** | ID of the app developer |[optional]|
**developer_url** | **StrictStr** | URL to the developer page on App Store |[optional]|
**version** | **StrictStr** | current version of the app |[optional]|
**minimum_os_version** | **StrictStr** | minimum OS version required to install the app |[optional]|
**size** | **StrictStr** | size of the app |[optional]|
**released_date** | **StrictStr** | date and time when the app was released<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**last_update_date** | **StrictStr** | date and time when the app was last updated<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**update_notes** | **StrictStr** | update notes<br>contains the latest update notes from the developer |[optional]|
**images** | **List[Optional[StrictStr]]** | app images<br>contains URLs to the images used on the app page on App Store |[optional]|
**similar_apps** | **List[Optional[AppsInfo]]** | similar apps<br>displays apps similar to the app in a POST request |[optional]|
**more_apps_by_developer** | **List[Optional[AppsInfo]]** | similar apps<br>information about apps built by the same developer |[optional]|