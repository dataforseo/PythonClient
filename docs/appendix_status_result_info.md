# AppendixStatusResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**api** | **StrictStr** | name of the API<br>the list of APIs:<br>serp<br>keywords_data<br>appendix<br>dataforseo_labs<br>domain_analytics<br>merchant<br>on_page<br>business_data<br>backlinks<br>app_data<br>content_analysis<br>content_generation |[optional]|
**status** | **StrictStr** | current status<br>you can find all information about your API statuses for the last 60 days here<br>the list of possible current statuses:<br>major_outage<br>partial_outage<br>long_response_time<br>long_execution_time<br>webhook_delay<br>send_delay |[optional]|
**endpoints** | **List[Optional[AppendixStatusEndpointsInfo]]** | array of objects that contain status information for API endpoints |[optional]|