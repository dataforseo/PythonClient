# RankChanges


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**previous_rank_absolute** | **StrictInt** | <em>previous absolute rank in SERP</em><br>            indicates previous rank of the element in Google SERP;<br>            if this element is new, the value will be <code>null</code> |[optional]|
**is_new** | **StrictBool** | <em>number of new ranked elements</em><br>            indicates how many new ranked elements were found for this domain or webpage |[optional]|
**is_up** | **StrictBool** | <em>rank went up</em><br>            indicates how many ranked elements of this target went up in Google Search |[optional]|
**is_down** | **StrictBool** | <em>rank went down</em><br>            indicates how many ranked elements of this target went down in Google Search |[optional]|