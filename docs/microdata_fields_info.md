# MicrodataFieldsInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**name** | **StrictStr** | field name<br>name of the data field |[optional]|
**types** | **List[Optional[StrictStr]]** | parent microdata types<br>for a full list of available types, please visit schema.org |[optional]|
**value** | **StrictStr** | microdata value<br>microdata value specified on a target web page |[optional]|
**test_results** | **MessageInfo** | microdata validation test results<br>sub-type microdata test results that contain detected errors and related messages |[optional]|
**fields** | **List[Optional[MicrodataFieldsInfo]]** | microdata fields<br>an array of objects containing data fields related to the certain microdata type |[optional]|