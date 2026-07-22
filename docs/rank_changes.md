# RankChanges


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**previous_rank_absolute** | **StrictInt** | previous absolute rank in SERP<br>indicates previous rank of the element in Google SERP;<br>if this element is new, the value will be null |[optional]|
**is_new** | **StrictBool** | number of new ranked elements<br>indicates how many new ranked elements were found for this domain or webpage |[optional]|
**is_up** | **StrictBool** | rank went up<br>indicates how many ranked elements of this target went up in Google Search |[optional]|
**is_down** | **StrictBool** | rank went down<br>indicates how many ranked elements of this target went down in Google Search |[optional]|