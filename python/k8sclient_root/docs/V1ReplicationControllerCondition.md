# V1ReplicationControllerCondition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_probe_time** | [**UnversionedTime**](UnversionedTime.md) | Last time we probed the condition. | [optional] 
**last_transition_time** | [**UnversionedTime**](UnversionedTime.md) | The last time the condition transitioned from one status to another. | [optional] 
**message** | **str** | A human readable message indicating details about the transition. | [optional] 
**reason** | **str** | The reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | Status of the condition, one of True, False, Unknown. | 
**type** | **str** | Type of replication controller condition. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


