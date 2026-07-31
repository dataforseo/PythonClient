# DataforseoLabsLocationsAndLanguagesResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**location_code** | **StrictInt** | <em>location code</em> |[optional]|
**location_name** | **StrictStr** | <em>full name of the location</em> |[optional]|
**location_code_parent** | **StrictInt** | <em>the code of the superordinate location</em><br>the value will be <code>null</code> as <code>Country</code> is the only supported <code>location_type</code> for this API |[optional]|
**country_iso_code** | **StrictStr** | <em>ISO country code of the location</em> |[optional]|
**location_type** | **StrictStr** | <em>location type</em><br>possible values:<br><code>Country</code> |[optional]|
**available_languages** | **List[Optional[AvailableLanguages]]** | <em>supported languages</em><br>contains the languages which are supported for a specific location |[optional]|