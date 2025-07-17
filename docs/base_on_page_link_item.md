# BaseOnPageLinkItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**domain_from** | **StrictStr** | referring domain<br>the link was found on this domain |[optional]|
**domain_to** | **StrictStr** | referenced domain<br>the link is pointing to this domain |[optional]|
**page_from** | **StrictStr** | referring page<br>relative URL of the page on which the link was found |[optional]|
**page_to** | **StrictStr** | referenced page<br>relative URL of the page to which the link is pointing |[optional]|
**link_from** | **StrictStr** | referring page<br>absolute URL of the page on which the link was found |[optional]|
**link_to** | **StrictStr** | referenced page<br>absolute URL of the page to which the link is pointing |[optional]|
**dofollow** | **StrictBool** | indicates whether the link is dofollow<br>if the value is true, the link doesn’t have a rel='nofollow' attribute |[optional]|
**page_from_scheme** | **StrictStr** | url scheme of the referring page |[optional]|
**page_to_scheme** | **StrictStr** | url scheme of the referenced page |[optional]|
**direction** | **StrictStr** | direction of the link<br>possible values: internal, external |[optional]|
**is_broken** | **StrictBool** | link is broken<br>indicates whether a link is directing to a broken page or resource |[optional]|
**is_link_relation_conflict** | **StrictBool** | indicates that the link may have a conflict with another link<br>if true, at least one link pointing to link_to has a rel='nofollow' attribute and at least one is dofollow |[optional]|
**page_to_status_code** | **StrictInt** | status code of the referenced page<br>status code of the page to which the link is pointing |[optional]|