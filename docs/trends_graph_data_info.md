# TrendsGraphDataInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**date_from** | **StrictStr** | start date of the corresponding time range<br>in the UTC format: “yyyy-mm-dd” |[optional]|
**date_to** | **StrictStr** | end date of the corresponding time range<br>in the UTC format: “yyyy-mm-dd” |[optional]|
**timestamp** | **StrictFloat** | a point in time in the Unix time format |[optional]|
**missing_data** | **StrictBool** | indicates whether the data is unavailable<br>if true the data on the graph in the Google Trends interface is missing and thus labelled with a dotted line |[optional]|
**values** | **List[Optional[StrictFloat]]** | relative keyword popularity rate at a specific timestamp<br>represents the keyword popularity rate over the given time range<br>if you specify more than one keyword, the values will be averaged to the highest value across all specified keywords<br>a value of 100 is the peak popularity for the term. A value of 50 means that the term is half as popular. A score of 0 means there was not enough data for this term |[optional]|