# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6198, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

VERSION = "unknown"

class AttestationManagementClientConfiguration(Configuration):
    """Configuration for AttestationManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    """

    def __init__(
        self,
        subscription_id: str,
        **kwargs: Any
    ) -> None:
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        super(AttestationManagementClientConfiguration, self).__init__(**kwargs)

        self.subscription_id = subscription_id
        self.api_version = "2018-09-01-preview"
        self._configure(**kwargs)
        self.user_agent_policy.add_user_agent('azsdk-python-attestationmanagementclient/{}'.format(VERSION))

    def _configure(
        self,
        **kwargs: Any
    ) -> None:
        self.user_agent_policy = kwargs.get('user_agent_policy') or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get('headers_policy') or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get('proxy_policy') or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get('logging_policy') or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get('retry_policy') or policies.AsyncRetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get('custom_hook_policy') or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get('redirect_policy') or policies.AsyncRedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get('authentication_policy')
