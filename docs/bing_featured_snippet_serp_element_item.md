# BingFeaturedSnippetSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **StrictStr** | <em>domain of the ad element in SERP</em> |[optional]|
**title** | **StrictStr** | <em>title of the ad element in SERP</em> |[optional]|
**description** | **StrictStr** | <em>description of the ad element in SERP</em> |[optional]|
**url** | **StrictStr** | <em>relevant URL of the ad element in SERP</em> |[optional]|
**breadcrumb** | **StrictStr** | <em>breadcrumb of the ad element in SERP</em> |[optional]|
**featured_title** | **StrictStr** | <em>the title of the featured snippets source page</em> |[optional]|
**timestamp** | **StrictStr** | <em>date and time when the result was published</em><br>            in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>            example:<br>            <code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | <em>images of the element</em><br>            if there are none, equals <code>null</code> |[optional]|
**table** | **Table** | <em>results table</em><br>            if there are none, equals <code>null</code> |[optional]|