# ContentGenerationCheckGrammarLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**message** | **StrictStr** | message of the grammar or spelling error |[optional]|
**description** | **StrictStr** | description of the grammar or spelling error |[optional]|
**suggestions** | **List[Optional[StrictStr]]** | suggested corrections |[optional]|
**offset** | **StrictInt** | offset token for subsequent requests |[optional]|
**length** | **StrictInt** | offset token for subsequent requests |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**rule_id** | **StrictStr** | id of the grammar or spelling rule<br>see the List of Grammar Rules for Content Generation API |[optional]|
**rule_description** | **StrictStr** | description of the grammar or spelling rule |[optional]|
**rule_issue_type** | **StrictStr** | type of the issue found by the relevant rule |[optional]|
**rule_category_id** | **StrictStr** | id of the rule category |[optional]|
**rule_category_name** | **StrictStr** | name of the rule category |[optional]|