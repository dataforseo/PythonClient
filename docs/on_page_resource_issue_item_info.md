# OnPageResourceIssueItemInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**line** | **StrictInt** | line where the error was found |[optional]|
**column** | **StrictInt** | column where the error was found |[optional]|
**message** | **StrictStr** | text message of the error<br>the full list of possible HTML errors can be found here |[optional]|
**status_code** | **StrictInt** | general status code<br>you can find the full list of the response codes here<br>Note: we strongly recommend designing a necessary system for handling related exceptional or error conditions |[optional]|