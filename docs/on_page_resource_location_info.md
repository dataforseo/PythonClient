# OnPageResourceLocationInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**line** | **StrictInt** | line number<br>the number of the line on which the resource is located |[optional]|
**offset_left** | **StrictInt** | position in line<br>the number of line characters before the resource;<br>sometimes referred to as column<br>Note: counts from 1, i.e. if the resource doesn’t have any characters to the left, the value will be 1 |[optional]|
**offset_top** | **StrictInt** | position in the document<br>the total number of characters between the resource and the top of HTML |[optional]|