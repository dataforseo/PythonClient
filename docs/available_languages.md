# AvailableLanguages


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**available_sources** | **List[Optional[StrictStr]]** | supported sources<br>contains the sources of data supported for a specific location and language combination<br>only google and bing are currently available |[optional]|
**language_name** | **StrictStr** | language name |[optional]|
**language_code** | **StrictStr** | language code according to ISO 639-1 |[optional]|
**keywords** | **StrictFloat** | the number of keywords available for the given location and language |[optional]|
**serps** | **StrictFloat** | the number of SERP pages available for the given location and language |[optional]|