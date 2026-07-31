# ContentAnalysisCategoriesResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**category_code** | **StrictInt** | <em>category code</em> |[optional]|
**category_name** | **StrictStr** | <em>full name of the category</em> |[optional]|
**category_code_parent** | **StrictInt** | <em>the code of the superordinate category</em><br>example:<br><code>'category_code': 10178,<br>'category_name': 'Apparel Accessories',<br>'category_code_parent': 10021</code> <br>where <code>category_code_parent</code> <br>corresponds to: <br><code>'category_code': 10178,<br>'category_name': 'Apparel Accessories'</code> |[optional]|