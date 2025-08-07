# AppDataAppleLocationsResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**location_code** | **StrictInt** | location code |[optional]|
**location_name** | **StrictStr** | full name of the location |[optional]|
**location_name_parent** | **StrictStr** | the name of the superordinate location<br>example:<br>'location_code': 1006473,<br>'location_name': 'Altrincham,England,United Kingdom',<br>'location_name_parent': 'England,United Kingdom', where location_name_parent corresponds to:<br>'location_code': 20339,<br>'location_name': 'England,United Kingdom'<br>note: Apple App Data API currently supports countries only, that is why this value will always be null |[optional]|
**country_iso_code** | **StrictStr** | ISO country code of the location |[optional]|
**location_type** | **StrictStr** | location type |[optional]|