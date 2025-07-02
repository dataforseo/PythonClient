# AbsoluteItems


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**geo_id** | **StrictStr** | location identifier<br>you can use this field for matching obtained results with location parameters specified in the request<br>see the full list of available locations with their geo_id here or by making a separate request to https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations<br>example:<br>US-NY |[optional]|
**geo_name** | **StrictStr** | location name<br>you can use this field for matching obtained results with location parameters specified in the request<br>see the full list of available locations with their geo_name here or by making a separate request to https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations<br>example:<br>Andorra |[optional]|
**values** | **List[Optional[StrictInt]]** | keyword popularity rates within a given location<br>represents location-specific keyword popularity rate over the specified time range;<br>using these values, you can understand which of the specified keywords is more popular in the related location;<br>the first value in the array is provided for the first term from the keywords array, the second value is provided for the second keyword, and so on;<br>calculation: we determine the highest popularity value across all specified keywords within a given location, and then express the popularity values of each keyword as a percentage of the highest value (100);<br>a value of 100 is the peak popularity for the term<br>a value of 50 means that the term is half as popular<br>a value of 0 means there was not enough data for this term |[optional]|