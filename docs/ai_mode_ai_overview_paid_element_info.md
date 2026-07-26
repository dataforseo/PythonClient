# AiModeAiOverviewPaidElementInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | <em>title of the element in SERP</em> |[optional]|
**url** | **StrictStr** | <em>reference page URL</em> |[optional]|
**domain** | **StrictStr** | <em>domain name of the reference</em> |[optional]|
**ad_aclk** | **StrictStr** | <em>unique ad click referral parameter</em><br>using this parameter you can get a URL of the advertisement in <a href='https://docs.dataforseo.com/v3/merchant/google/sellers/ad_url/' rel='noopener noreferrer' target='_blank'>Google Shopping Sellers Ad URL</a> |[optional]|
**website_name** | **StrictStr** | <em>displayed name of the advertiser's website</em> |[optional]|
**breadcrumb** | **StrictStr** | <em>breadcrumb path displayed in the ad</em> |[optional]|
**snippet** | **StrictStr** | <em>description text of the ad</em> |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | <em>images present in the ad</em><br>if there are none, equals <code>null</code> |[optional]|