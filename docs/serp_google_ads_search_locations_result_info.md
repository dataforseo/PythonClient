# SerpGoogleAdsSearchLocationsResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**location_code** | **StrictInt** | <em>location code</em> |[optional]|
**location_name** | **StrictStr** | <em>full name of the location</em> |[optional]|
**location_code_parent** | **StrictInt** | <em>the code of the superordinate location</em><br>example:<br>`'location_code': 9041134`,<br>`'location_name': 'Vienna International Airport,Lower Austria,Austria'`,<br>`'location_code_parent': 20044`<p>where `location_code_parent` corresponds to:<p>`'location_code': 20044`,<br>`'location_name': 'Lower Austria,Austria'` |[optional]|
**country_iso_code** | **StrictStr** | <em>ISO country code of the location</em> |[optional]|
**location_type** | **StrictStr** | <em>location type</em> |[optional]|