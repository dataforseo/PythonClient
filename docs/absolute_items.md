# AbsoluteItems


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**geo_id** | **StrictStr** | location identifier<br>you can use this field for matching obtained results with location parameters specified in the request<br>see the full list of available locations with their geo_id here or by making a separate request to https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations<br>example:<br>US-NY |[optional]|
**geo_name** | **StrictStr** | location name<br>you can use this field for matching obtained results with location parameters specified in the request<br>see the full list of available locations with their geo_name here or by making a separate request to https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations<br>example:<br>Andorra |[optional]|
**values** | **List[Optional[StrictStr]]** | contains data on relative keyword popularity by country or region |[optional]|