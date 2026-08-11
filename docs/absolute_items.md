# AbsoluteItems


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**geo_id** | **StrictStr** | <em>location identifier</em><br>you can use this field for matching obtained results with location parameters specified in the request<br>see the full list of available locations with their <code>geo_id</code> <a href='/v3/keywords_data/dataforseo_trends/locations/' rel='noopener noreferrer' target='_blank'>here</a> or by making a separate request to <code>https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations</code><br>example:<br><code>US-NY</code> |[optional]|
**geo_name** | **StrictStr** | <em>location name</em><br>you can use this field for matching obtained results with location parameters specified in the request<br>see the full list of available locations with their <code>geo_name</code> <a href='/v3/keywords_data/dataforseo_trends/locations/' rel='noopener noreferrer' target='_blank'>here</a> or by making a separate request to <code>https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations</code><br>example:<br><code>Andorra</code> |[optional]|
**values** | **List[Optional[StrictStr]]** | <em>contains data on relative keyword popularity by country or region</em> |[optional]|