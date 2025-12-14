# AiOptimizationLLmMentionsDomainElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **StrictStr** | target domain<br>required field if you don’t specify keyword<br>a domain should be specified without https:// and www. |[optional]|
**include_subdomains** | **StrictBool** | indicates if the subdomains of the target domain will be included in the search<br>optional field<br>if set to true, the subdomains will be included in the search<br>default value: false |[optional]|
**search_scope** | **List[Optional[StrictStr]]** | target domain search scope<br>optional field<br>possible values:<br>any, sources, search_results<br>default value: any |[optional]|
**search_filter** | **StrictStr** | target domain search filter<br>optional field<br>possible values:<br>include, exclude<br>default value: include |[optional]|