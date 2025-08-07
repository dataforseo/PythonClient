# DuplicatePageInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**similarity** | **StrictInt** | content similarity score<br>by default, the content is considered duplicate if the value is greater than or equals 6<br>can take values from 0 to 10 |[optional]|
**page** | **List[Optional[OnPageHtmlResourceItem]]** | information about the page with duplicate content |[optional]|