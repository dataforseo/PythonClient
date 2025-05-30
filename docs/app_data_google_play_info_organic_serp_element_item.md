# AppDataGooglePlayInfoOrganicSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**app_id** | **StrictStr** | ID of the app |[optional]|
**url** | **StrictStr** | URL to the app page on Google Play |[optional]|
**icon** | **StrictStr** | URL to the app icon |[optional]|
**description** | **StrictStr** | description of the app |[optional]|
**reviews_count** | **StrictFloat** | the total number of reviews the app has |[optional]|
**price** | **PriceInfo** | price of the app |[optional]|
**is_free** | **StrictBool** | indicates whether the app is free |[optional]|
**main_category** | **StrictStr** | main category of the app |[optional]|
**installs** | **StrictStr** | number of installs of the app<br>approximate number of installs as displayed on the app page |[optional]|
**installs_count** | **StrictFloat** | number of installs of the app<br>the exact number of installs of the app |[optional]|
**developer** | **StrictStr** | name of the app developer |[optional]|
**developer_id** | **StrictStr** | ID of the app developer |[optional]|
**developer_url** | **StrictStr** | URL to the developer page on Google Play |[optional]|
**developer_email** | **StrictStr** | email address of the developer |[optional]|
**developer_address** | **StrictStr** | physical address of the developer |[optional]|
**developer_website** | **StrictStr** | official website of the developer |[optional]|
**version** | **StrictStr** | current version of the app |[optional]|
**minimum_os_version** | **StrictStr** | minimum OS version required to install the app |[optional]|
**size** | **StrictStr** | size of the app |[optional]|
**released_date** | **StrictStr** | date and time when the app was released<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**last_update_date** | **StrictStr** | date and time when the app was last updated<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**update_notes** | **StrictStr** | update notes<br>contains the latest update notes from the developer |[optional]|
**images** | **List[Optional[StrictStr]]** | app images<br>contains URLs to the images published on the app page on Google Play |[optional]|
**videos** | **List[Optional[StrictStr]]** | app videos<br>contains URLs to the video published on the app page on Google Play |[optional]|
**similar_apps** | **List[Optional[AppsInfo]]** | similar apps<br>displays apps similar to the app in a POST request |[optional]|
**more_apps_by_developer** | **List[Optional[AppsInfo]]** | similar apps<br>information about apps built by the same developer |[optional]|
**genres** | **List[Optional[StrictStr]]** | app genres<br>contains relevant app categories |[optional]|
**tags** | **List[Optional[StrictStr]]** | app tags<br>contains relevant app tags |[optional]|