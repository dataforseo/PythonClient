# BaseOnPageLinkItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**domain_from** | **StrictStr** | <em>referring domain</em><br>the link was found on this domain |[optional]|
**domain_to** | **StrictStr** | <em>referenced domain</em><br>the link is pointing to this domain |[optional]|
**page_from** | **StrictStr** | <em>referring page</em><br>relative URL of the page on which the link was found |[optional]|
**page_to** | **StrictStr** | <em>referenced page</em><br>relative URL of the page to which the link is pointing |[optional]|
**link_from** | **StrictStr** | <em>referring page</em><br>absolute URL of the page on which the link was found |[optional]|
**link_to** | **StrictStr** | <em>referenced page</em><br>absolute URL of the page to which the link is pointing |[optional]|
**dofollow** | **StrictBool** | <em>indicates whether the link is dofollow</em><br>if the value is <code>true</code>, the link doesn't have a <code>rel='nofollow'</code> attribute |[optional]|
**page_from_scheme** | **StrictStr** | <em><a href='https://en.wikipedia.org/wiki/List_of_URI_schemes' target='_blank' rel='noopener noreferrer'>url scheme</a> of the referring page</em> |[optional]|
**page_to_scheme** | **StrictStr** | <em><a href='https://en.wikipedia.org/wiki/List_of_URI_schemes' target='_blank' rel='noopener noreferrer'>url scheme</a> of the referenced page</em> |[optional]|
**direction** | **StrictStr** | <em>direction of the link</em><br>possible values: <code>internal</code>, <code>external</code> |[optional]|
**is_broken** | **StrictBool** | <em>link is broken</em><br>indicates whether a link is directing to a broken page or resource |[optional]|
**is_link_relation_conflict** | **StrictBool** | <em>indicates that the link may have a conflict with another link</em><br>if <code>true</code>, at least one link pointing to <code>link_to</code> has a <code>rel='nofollow'</code> attribute <strong>and</strong> at least one is dofollow |[optional]|
**page_to_status_code** | **StrictInt** | <em>status code of the referenced page</em><br>status code of the page to which the link is pointing |[optional]|