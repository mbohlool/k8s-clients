# coding: utf-8

"""
    Kubernetes /apis/autoscaling/v1

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


class V1DeleteOptions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, grace_period_seconds=None, orphan_dependents=None, preconditions=None):
        """
        V1DeleteOptions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'grace_period_seconds': 'int',
            'orphan_dependents': 'bool',
            'preconditions': 'V1Preconditions'
        }

        self.attribute_map = {
            'grace_period_seconds': 'gracePeriodSeconds',
            'orphan_dependents': 'orphanDependents',
            'preconditions': 'preconditions'
        }

        self._grace_period_seconds = grace_period_seconds
        self._orphan_dependents = orphan_dependents
        self._preconditions = preconditions

    @property
    def grace_period_seconds(self):
        """
        Gets the grace_period_seconds of this V1DeleteOptions.
        The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.

        :return: The grace_period_seconds of this V1DeleteOptions.
        :rtype: int
        """
        return self._grace_period_seconds

    @grace_period_seconds.setter
    def grace_period_seconds(self, grace_period_seconds):
        """
        Sets the grace_period_seconds of this V1DeleteOptions.
        The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.

        :param grace_period_seconds: The grace_period_seconds of this V1DeleteOptions.
        :type: int
        """

        self._grace_period_seconds = grace_period_seconds

    @property
    def orphan_dependents(self):
        """
        Gets the orphan_dependents of this V1DeleteOptions.
        Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list.

        :return: The orphan_dependents of this V1DeleteOptions.
        :rtype: bool
        """
        return self._orphan_dependents

    @orphan_dependents.setter
    def orphan_dependents(self, orphan_dependents):
        """
        Sets the orphan_dependents of this V1DeleteOptions.
        Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list.

        :param orphan_dependents: The orphan_dependents of this V1DeleteOptions.
        :type: bool
        """

        self._orphan_dependents = orphan_dependents

    @property
    def preconditions(self):
        """
        Gets the preconditions of this V1DeleteOptions.
        Must be fulfilled before a deletion is carried out. If not possible, a 409 Conflict status will be returned.

        :return: The preconditions of this V1DeleteOptions.
        :rtype: V1Preconditions
        """
        return self._preconditions

    @preconditions.setter
    def preconditions(self, preconditions):
        """
        Sets the preconditions of this V1DeleteOptions.
        Must be fulfilled before a deletion is carried out. If not possible, a 409 Conflict status will be returned.

        :param preconditions: The preconditions of this V1DeleteOptions.
        :type: V1Preconditions
        """

        self._preconditions = preconditions

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
