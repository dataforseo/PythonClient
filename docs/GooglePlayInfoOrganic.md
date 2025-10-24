# GooglePlayInfoOrganic

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**rank_group** | **number** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank among all the listed apps<br>absolute position among all apps on the list |[optional]|
**position** | **string** | the alignment of the element in SERP<br>can take the following values: left |[optional]|
**app_id** | **string** | ID of the app |[optional]|
**title** | **string** | title of the app |[optional]|
**url** | **string** | URL to the app page on Google Play |[optional]|
**icon** | **string** | URL to the app icon |[optional]|
**description** | **string** | description of the app |[optional]|
**reviews_count** | **number** | the total number of reviews the app has |[optional]|
**rating** | **RatingInfo** | average rating of the app |[optional]|
**price** | **PriceInfo** | price of the app |[optional]|
**is_free** | **boolean** | indicates whether the app is free |[optional]|
**main_category** | **string** | main category of the app |[optional]|
**installs** | **string** | number of installs of the app<br>approximate number of installs as displayed on the app page |[optional]|
**installs_count** | **number** | number of installs of the app<br>the exact number of installs of the app |[optional]|
**developer** | **string** | name of the app developer |[optional]|
**developer_id** | **string** | ID of the app developer |[optional]|
**developer_url** | **string** | URL to the developer page on Google Play |[optional]|
**developer_email** | **string** | email address of the developer |[optional]|
**developer_address** | **string** | physical address of the developer |[optional]|
**developer_website** | **string** | official website of the developer |[optional]|
**version** | **string** | current version of the app |[optional]|
**minimum_os_version** | **string** | minimum OS version required to install the app |[optional]|
**size** | **string** | size of the app |[optional]|
**released_date** | **string** | date and time when the app was released<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**last_update_date** | **string** | date and time when the app was last updated<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**update_notes** | **string** | update notes<br>contains the latest update notes from the developer |[optional]|
**images** | **string[]** | app images<br>contains URLs to the images published on the app page on Google Play |[optional]|
**videos** | **string[]** | app videos<br>contains URLs to the video published on the app page on Google Play |[optional]|
**similar_apps** | **AppsInfo[]** | similar apps<br>displays apps similar to the app in a POST request |[optional]|
**more_apps_by_developer** | **AppsInfo[]** | similar apps<br>information about apps built by the same developer |[optional]|
**genres** | **string[]** | app genres<br>contains relevant app categories |[optional]|
**tags** | **string[]** | app tags<br>contains relevant app tags |[optional]|