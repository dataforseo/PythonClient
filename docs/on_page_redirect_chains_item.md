# OnPageRedirectChainsItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**is_redirect_loop** | **StrictBool** | indicates if redirects in chain start and end at the same URL<br>if true, the last URL from the chain redirects back to the original URL |[optional]|
**chain** | **List[Optional[OnPageRedirectLinkItem]]** | contains links that form a chain |[optional]|