# TrendsGraphDataInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**date_from** | **StrictStr** | <em>start date of the corresponding time range</em><br>in the UTC format: 'yyyy-mm-dd' |[optional]|
**date_to** | **StrictStr** | <em>end date of the corresponding time range</em><br>in the UTC format: 'yyyy-mm-dd' |[optional]|
**timestamp** | **StrictInt** | <em>a point in time in the <a href='https://en.wikipedia.org/wiki/Unix_time'>Unix time format</a></em> |[optional]|
**missing_data** | **StrictBool** | <em>indicates whether the data is unavailable<em><br>if <code>true<code> the data on the graph in the Google Trends interface is missing and thus labelled with a dotted line |[optional]|
**values** | **List[Optional[StrictFloat]]** | <em>relative keyword popularity rate at a specific timestamp</em><br>represents the keyword popularity rate over the given time range<br><strong>if you specify more than one keyword, the values will be averaged to the highest value across all specified keywords</strong><br>a value of 100 is the peak popularity for the term. A value of 50 means that the term is half as popular. A score of 0 means there was not enough data for this term |[optional]|