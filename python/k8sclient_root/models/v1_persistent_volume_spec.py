# coding: utf-8

"""
    Kubernetes

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: unversioned
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1PersistentVolumeSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, access_modes=None, capacity=None, claim_ref=None, persistent_volume_reclaim_policy=None):
        """
        V1PersistentVolumeSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'access_modes': 'list[str]',
            'capacity': 'dict(str, ResourceQuantity)',
            'claim_ref': 'V1ObjectReference',
            'persistent_volume_reclaim_policy': 'str'
        }

        self.attribute_map = {
            'access_modes': 'accessModes',
            'capacity': 'capacity',
            'claim_ref': 'claimRef',
            'persistent_volume_reclaim_policy': 'persistentVolumeReclaimPolicy'
        }

        self._access_modes = access_modes
        self._capacity = capacity
        self._claim_ref = claim_ref
        self._persistent_volume_reclaim_policy = persistent_volume_reclaim_policy

    @property
    def access_modes(self):
        """
        Gets the access_modes of this V1PersistentVolumeSpec.
        AccessModes contains all ways the volume can be mounted. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#access-modes

        :return: The access_modes of this V1PersistentVolumeSpec.
        :rtype: list[str]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """
        Sets the access_modes of this V1PersistentVolumeSpec.
        AccessModes contains all ways the volume can be mounted. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#access-modes

        :param access_modes: The access_modes of this V1PersistentVolumeSpec.
        :type: list[str]
        """

        self._access_modes = access_modes

    @property
    def capacity(self):
        """
        Gets the capacity of this V1PersistentVolumeSpec.
        A description of the persistent volume's resources and capacity. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#capacity

        :return: The capacity of this V1PersistentVolumeSpec.
        :rtype: dict(str, ResourceQuantity)
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this V1PersistentVolumeSpec.
        A description of the persistent volume's resources and capacity. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#capacity

        :param capacity: The capacity of this V1PersistentVolumeSpec.
        :type: dict(str, ResourceQuantity)
        """

        self._capacity = capacity

    @property
    def claim_ref(self):
        """
        Gets the claim_ref of this V1PersistentVolumeSpec.
        ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#binding

        :return: The claim_ref of this V1PersistentVolumeSpec.
        :rtype: V1ObjectReference
        """
        return self._claim_ref

    @claim_ref.setter
    def claim_ref(self, claim_ref):
        """
        Sets the claim_ref of this V1PersistentVolumeSpec.
        ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#binding

        :param claim_ref: The claim_ref of this V1PersistentVolumeSpec.
        :type: V1ObjectReference
        """

        self._claim_ref = claim_ref

    @property
    def persistent_volume_reclaim_policy(self):
        """
        Gets the persistent_volume_reclaim_policy of this V1PersistentVolumeSpec.
        What happens to a persistent volume when released from its claim. Valid options are Retain (default) and Recycle. Recycling must be supported by the volume plugin underlying this persistent volume. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#recycling-policy

        :return: The persistent_volume_reclaim_policy of this V1PersistentVolumeSpec.
        :rtype: str
        """
        return self._persistent_volume_reclaim_policy

    @persistent_volume_reclaim_policy.setter
    def persistent_volume_reclaim_policy(self, persistent_volume_reclaim_policy):
        """
        Sets the persistent_volume_reclaim_policy of this V1PersistentVolumeSpec.
        What happens to a persistent volume when released from its claim. Valid options are Retain (default) and Recycle. Recycling must be supported by the volume plugin underlying this persistent volume. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#recycling-policy

        :param persistent_volume_reclaim_policy: The persistent_volume_reclaim_policy of this V1PersistentVolumeSpec.
        :type: str
        """

        self._persistent_volume_reclaim_policy = persistent_volume_reclaim_policy

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
