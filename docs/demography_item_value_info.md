# DemographyItemValueInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**value** | **StrictFloat** | keyword popularity rate within the specified age range<br>using this value you can understand how popular a keyword is within each age range;<br>calculation: we determine the highest popularity value for the relevant keyword across all age groups, and then express all other values as a percentage of that highest value (100);<br>a value of 100 is the highest popularity for the term<br>a value of 0 means there was not enough data for this term |[optional]|