# AvailableLanguages


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**available_sources** | **List[Optional[StrictStr]]** | <em>supported sources</em><br>contains the sources of data supported for a specific location and language combination<br>only <code>google</code> and <code>bing</code> are currently available |[optional]|
**language_name** | **StrictStr** | <em>language name</em> |[optional]|
**language_code** | **StrictStr** | <em>language code according to <a href='https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes' target='_blank' rel='noopener noreferrer'>ISO 639-1</a></em> |[optional]|
**keywords** | **StrictInt** | <em>the number of keywords available for the given location and language |[optional]|
**serps** | **StrictInt** | <em>the number of SERP pages available for the given location and language |[optional]|