# AppendixStatusEndpointsInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**endpoint** | **StrictStr** | <em>name of the endpoint</em><br>the list of possible endpoints:<br>`task_get`<br>`task_post`<br>`live`<br>`postback/pingback` |[optional]|
**status** | **StrictStr** | <em>current status</em><br>you can find all information about your API statuses for the last 60 days <a href='https://status.dataforseo.com/' rel='noopener noreferrer' target='_blank'>here</a><br>the list of possible current statuses:<br>`major_outage`<br>`partial_outage`<br>`long_response_time`<br>`long_execution_time`<br>`webhook_delay`<br>`send_delay` |[optional]|