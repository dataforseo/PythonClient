# KeywordsDataGoogleTrendsCategoriesResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**category_code** | **StrictFloat** | unique google trends category identifier |[optional]|
**category_name** | **StrictStr** | name of the google trends category |[optional]|
**category_code_parent** | **StrictFloat** | the code of the superordinate category<br>example:<br>'category_code': 1100,<br>'category_name': 'Superhero Films',<br>'category_code_parent': 1097<br>where category_code_parent corresponds to:<br>'category_code': 1097,<br>'category_name': 'Action & Adventure Films' |[optional]|