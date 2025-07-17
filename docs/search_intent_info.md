# SearchIntentInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type<br>possible values: google |[optional]|
**main_intent** | **StrictStr** | main search intent<br>possible values: informational, navigational, commercial, transactional |[optional]|
**foreign_intent** | **List[Optional[StrictStr]]** | supplementary search intents<br>possible values: informational, navigational, commercial, transactional |[optional]|
**last_updated_time** | **StrictStr** | date and time when the dataset was updated<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|