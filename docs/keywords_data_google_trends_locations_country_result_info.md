# KeywordsDataGoogleTrendsLocationsCountryResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**location_code** | **StrictInt** | location code |[optional]|
**location_name** | **StrictStr** | full name of the location |[optional]|
**location_code_parent** | **StrictInt** | the code of the superordinate location<br>example:<br>'location_code': 9041134,<br>'location_name': 'Vienna International Airport,Lower Austria,Austria',<br>'location_code_parent': 20044<br>where location_code_parent corresponds to:<br>'location_code': 20044,<br>'location_name': 'Lower Austria,Austria' |[optional]|
**country_iso_code** | **StrictStr** | ISO country code of the location |[optional]|
**location_type** | **StrictStr** | location type<br>possible values according to Google’s target types |[optional]|
**geo_id** | **StrictStr** | google trends location identifier<br>you can use this field for matching obtained results with the location_code parameter specified in the request |[optional]|