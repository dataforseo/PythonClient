# DemographyItemValueInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**value** | **StrictInt** | <em>keyword popularity rate within the specified age range</em><br>using this <code>value</code> you can understand how popular a keyword is within each age range; <br>calculation: we determine the highest popularity value for the relevant keyword across all age groups, and then express all other values as a percentage of that highest value (100);<br>a value of <code>100</code> is the highest popularity for the term<br>a value of <code>0</code> means there was not enough data for this term |[optional]|