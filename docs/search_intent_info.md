# SearchIntentInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**main_intent** | **StrictStr** | main search intentpossible values: informational, navigational, commercial, transactional |[optional]|
**foreign_intent** | **List[Optional[StrictStr]]** | supplementary search intentspossible values: informational, navigational, commercial, transactional |[optional]|
**last_updated_time** | **StrictStr** | date and time when keyword data was updatedin the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”example:2019-11-15 12:57:46 +00:00 |[optional]|