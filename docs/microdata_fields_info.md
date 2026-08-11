# MicrodataFieldsInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**name** | **StrictStr** | <em>field name</em><br>name of the data field |[optional]|
**types** | **List[Optional[StrictStr]]** | list of microdata types |[optional]|
**value** | **StrictStr** | microdata value<br>microdata value specified on a target web page |[optional]|
**test_results** | **MessageInfo** | <em>microdata validation test results</em><br>sub-type microdata test results that contain detected errors and related messages |[optional]|
**fields** | **List[Optional[MicrodataFieldsInfo]]** | <em>microdata fields</em><br>an array of objects containing data fields related to the certain microdata type |[optional]|