# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6198, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class AttestationProvidersOperations:
    """AttestationProvidersOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~attestation_management_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get(
        self,
        resource_group_name: str,
        provider_name: str,
        **kwargs
    ) -> "models.AttestationProvider":
        """Get the status of Attestation Provider.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param provider_name: Name of the attestation service instance.
        :type provider_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationProvider or the result of cls(response)
        :rtype: ~attestation_management_client.models.AttestationProvider
        :raises: ~attestation_management_client.models.CloudErrorException:
        """
        cls: ClsType["models.AttestationProvider"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern='^[-\w\._\(\)]+$'),
            'providerName': self._serialize.url("provider_name", provider_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('AttestationProvider', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Attestation/attestationProviders/{providerName}'}

    async def create(
        self,
        resource_group_name: str,
        provider_name: str,
        attestation_policy: Optional[str] = None,
        keys: Optional[List["JSONWebKey"]] = None,
        **kwargs
    ) -> "models.AttestationProvider":
        """Creates or updates the Attestation Provider.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param provider_name: Name of the attestation service instance.
        :type provider_name: str
        :param attestation_policy: Name of attestation policy.
        :type attestation_policy: str
        :param keys: The value of the "keys" parameter is an array of JWK values.  By
         default, the order of the JWK values within the array does not imply
         an order of preference among them, although applications of JWK Sets
         can choose to assign a meaning to the order for their purposes, if
         desired.
        :type keys: list[~attestation_management_client.models.JSONWebKey]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationProvider or AttestationProvider or the result of cls(response)
        :rtype: ~attestation_management_client.models.AttestationProvider or ~attestation_management_client.models.AttestationProvider
        :raises: ~attestation_management_client.models.CloudErrorException:
        """
        cls: ClsType["models.AttestationProvider"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        creation_params = models.AttestationServiceCreationParams(attestation_policy=attestation_policy, keys=keys)
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern='^[-\w\._\(\)]+$'),
            'providerName': self._serialize.url("provider_name", provider_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if creation_params is not None:
            body_content = self._serialize.body(creation_params, 'AttestationServiceCreationParams')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('AttestationProvider', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('AttestationProvider', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Attestation/attestationProviders/{providerName}'}

    async def delete(
        self,
        resource_group_name: str,
        provider_name: str,
        **kwargs
    ) -> None:
        """Delete Attestation Service.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param provider_name: Name of the attestation service instance.
        :type provider_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~attestation_management_client.models.CloudErrorException:
        """
        cls: ClsType[None] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern='^[-\w\._\(\)]+$'),
            'providerName': self._serialize.url("provider_name", provider_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Attestation/attestationProviders/{providerName}'}

    async def list(
        self,
        **kwargs
    ) -> "models.AttestationProviderListResult":
        """Returns a list of attestation providers in a subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationProviderListResult or the result of cls(response)
        :rtype: ~attestation_management_client.models.AttestationProviderListResult
        :raises: ~attestation_management_client.models.CloudErrorException:
        """
        cls: ClsType["models.AttestationProviderListResult"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.list.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('AttestationProviderListResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Attestation/attestationProviders'}

    async def list_by_resource_group(
        self,
        resource_group_name: str,
        **kwargs
    ) -> "models.AttestationProviderListResult":
        """Returns attestation providers list in a resource group.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AttestationProviderListResult or the result of cls(response)
        :rtype: ~attestation_management_client.models.AttestationProviderListResult
        :raises: ~attestation_management_client.models.CloudErrorException:
        """
        cls: ClsType["models.AttestationProviderListResult"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.list_by_resource_group.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern='^[-\w\._\(\)]+$'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.CloudErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('AttestationProviderListResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Attestation/attestationProviders'}
