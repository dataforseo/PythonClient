# OnPageResourceIssueItemInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**line** | **StrictFloat** | line where the error was found |[optional]|
**column** | **StrictFloat** | column where the error was found |[optional]|
**message** | **StrictStr** | text message of the error<br>the full list of possible HTML errors can be found here |[optional]|
**status_code** | **StrictFloat** | status code of the error<br>possible values:<br>0 — Unidentified Error;<br>501 — Html Parse Error;<br>1501 — JS Parse Error;<br>2501 — CSS Parse Error;<br>3501 — Image Parse Error;<br>3502 — Image Scale Is Zero;<br>3503 — Image Size Is Zero;<br>3504 — Image Format Invalid |[optional]|