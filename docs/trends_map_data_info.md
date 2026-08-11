# TrendsMapDataInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**geo_id** | **StrictStr** | <em>Google Trends location identifier</em><br>you can use this field for matching obtained results with location parameters specified in the request<br>example:<br><code>US-NY</code> |[optional]|
**geo_name** | **StrictStr** | <em>Google Trends location name</em><br>you can use this field for matching obtained results with location parameters specified in the request |[optional]|
**values** | **List[Optional[StrictFloat]]** | <em>relative keyword popularity rate in a given location</em><br>represents the location-specific keyword popularity rate over the given time range<br><strong>if you specify more than one keyword, the values will be averaged to the highest value across all specified keywords</strong><br>a value of <code>100</code> is the peak popularity for the term<br>a value of <code>50</code> means that the term is half as popular<br>a value of <code>0</code> means there was not enough data for this term |[optional]|
**max_value_index** | **StrictInt** | <em>max value among comparable terms</em><br>represents the maximum value if you specified more than two keywords in a POST array<br>if you specified only one keyword, the value will be <code>null</code> |[optional]|