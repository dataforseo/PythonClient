# KeywordsDataGoogleTrendsCategoriesResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**category_code** | **StrictInt** | <em>unique google trends category identifier</em> |[optional]|
**category_name** | **StrictStr** | <em>name of the google trends category</em> |[optional]|
**category_code_parent** | **StrictInt** | <em>the code of the superordinate category</em><br>example:<br><code>'category_code': 1100,</code><br><code>'category_name': 'Superhero Films',</code><br><code>'category_code_parent': 1097</code> <br>where <code>category_code_parent</code> corresponds to: <br><code>'category_code': 1097,</code><br><code>'category_name': 'Action &amp; Adventure Films'</code> |[optional]|