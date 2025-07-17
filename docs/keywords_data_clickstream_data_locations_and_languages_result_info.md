# KeywordsDataClickstreamDataLocationsAndLanguagesResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**location_code** | **StrictInt** | location code |[optional]|
**location_name** | **StrictStr** | full name of the location |[optional]|
**location_code_parent** | **StrictStr** | the code of the superordinate location<br>the value will be null as Country is the only supported location_type for this API |[optional]|
**country_iso_code** | **StrictStr** | ISO country code of the location |[optional]|
**location_type** | **StrictStr** | location type<br>possible values:<br>Country |[optional]|
**available_languages** | **List[Optional[AvailableLanguages]]** | supported languages<br>contains the languages which are supported for a specific location |[optional]|