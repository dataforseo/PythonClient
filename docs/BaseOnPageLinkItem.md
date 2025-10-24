# BaseOnPageLinkItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**domain_from** | **string** | referring domain<br>the link was found on this domain |[optional]|
**domain_to** | **string** | referenced domain<br>the link is pointing to this domain |[optional]|
**page_from** | **string** | referring page<br>relative URL of the page on which the link was found |[optional]|
**page_to** | **string** | referenced page<br>relative URL of the page to which the link is pointing |[optional]|
**link_from** | **string** | referring page<br>absolute URL of the page on which the link was found |[optional]|
**link_to** | **string** | referenced page<br>absolute URL of the page to which the link is pointing |[optional]|
**dofollow** | **boolean** | indicates whether the link is dofollow<br>if the value is true, the link doesn’t have a rel='nofollow' attribute |[optional]|
**page_from_scheme** | **string** | url scheme of the referring page |[optional]|
**page_to_scheme** | **string** | url scheme of the referenced page |[optional]|
**direction** | **string** | direction of the link<br>possible values: internal, external |[optional]|
**is_broken** | **boolean** | link is broken<br>indicates whether a link is directing to a broken page or resource |[optional]|
**is_link_relation_conflict** | **boolean** | indicates that the link may have a conflict with another link<br>if true, at least one link pointing to link_to has a rel='nofollow' attribute and at least one is dofollow |[optional]|
**page_to_status_code** | **number** | status code of the referenced page<br>status code of the page to which the link is pointing |[optional]|