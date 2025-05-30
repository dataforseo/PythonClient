# DataforseoTrendsinterestsValuesInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**geo_id** | **StrictStr** | location identifier<br>you can use this field for matching obtained results with location parameters specified in the request<br>see the full list of available locations with their geo_id here or by making a separate request to https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations<br>example:<br>US-NY |[optional]|
**geo_name** | **StrictStr** | location name<br>you can use this field for matching obtained results with location parameters specified in the request<br>see the full list of available locations with their geo_name here or by making a separate request to https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations<br>example:<br>Andorra |[optional]|
**value** | **StrictFloat** | relative keyword popularity rate in a given location<br>represents location-specific keyword popularity rate over the specified time range;<br>using this value you can understand how popular a keyword is in one location compared to another location;<br>calculation: we determine the highest popularity value for the relevant keyword across all locations, and then express all other values as a percentage of that highest value (100);<br>a value of 100 is the highest popularity for the term<br>a value of 50 means that the term is half as popular<br>a value of 0 means there was not enough data for this term |[optional]|