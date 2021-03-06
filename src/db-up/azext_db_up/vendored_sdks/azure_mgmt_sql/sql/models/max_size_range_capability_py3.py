# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MaxSizeRangeCapability(Model):
    """The maximum size range capability.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar min_value: Minimum value.
    :vartype min_value: ~azure.mgmt.sql.models.MaxSizeCapability
    :ivar max_value: Maximum value.
    :vartype max_value: ~azure.mgmt.sql.models.MaxSizeCapability
    :ivar scale_size: Scale/step size for discrete values between the minimum
     value and the maximum value.
    :vartype scale_size: ~azure.mgmt.sql.models.MaxSizeCapability
    :ivar log_size: Size of transaction log.
    :vartype log_size: ~azure.mgmt.sql.models.LogSizeCapability
    :ivar status: The status of the capability. Possible values include:
     'Visible', 'Available', 'Default', 'Disabled'
    :vartype status: str or ~azure.mgmt.sql.models.CapabilityStatus
    :param reason: The reason for the capability not being available.
    :type reason: str
    """

    _validation = {
        'min_value': {'readonly': True},
        'max_value': {'readonly': True},
        'scale_size': {'readonly': True},
        'log_size': {'readonly': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'min_value': {'key': 'minValue', 'type': 'MaxSizeCapability'},
        'max_value': {'key': 'maxValue', 'type': 'MaxSizeCapability'},
        'scale_size': {'key': 'scaleSize', 'type': 'MaxSizeCapability'},
        'log_size': {'key': 'logSize', 'type': 'LogSizeCapability'},
        'status': {'key': 'status', 'type': 'CapabilityStatus'},
        'reason': {'key': 'reason', 'type': 'str'},
    }

    def __init__(self, *, reason: str=None, **kwargs) -> None:
        super(MaxSizeRangeCapability, self).__init__(**kwargs)
        self.min_value = None
        self.max_value = None
        self.scale_size = None
        self.log_size = None
        self.status = None
        self.reason = reason
