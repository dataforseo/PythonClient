# AppendixStatusResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**api** | **StrictStr** | <em>name of the API</em><br>the list of APIs:<br>`serp`<br>`keywords_data`<br>`appendix`<br>`dataforseo_labs`<br>`domain_analytics`<br>`merchant`<br>`on_page`<br>`business_data`<br>`backlinks`<br>`app_data`<br>`content_analysis`<br>`content_generation` |[optional]|
**status** | **StrictStr** | <em>current status</em><br>you can find all information about the statuses of our endpoints for the last 60 days <a href='https://status.dataforseo.com/' rel='noopener noreferrer' target='_blank'>here</a><br>the list of possible current statuses:<br>`major_outage`<br>`partial_outage`<br>`long_response_time`<br>`long_execution_time`<br>`webhook_delay`<br>`send_delay` |[optional]|
**endpoints** | **List[Optional[AppendixStatusEndpointsInfo]]** | <em>array of objects that contain status information for API endpoints</em> |[optional]|