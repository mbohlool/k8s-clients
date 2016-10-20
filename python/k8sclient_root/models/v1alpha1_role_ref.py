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


class V1alpha1RoleRef(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_group=None, kind=None, name=None):
        """
        V1alpha1RoleRef - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_group': 'str',
            'kind': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'api_group': 'apiGroup',
            'kind': 'kind',
            'name': 'name'
        }

        self._api_group = api_group
        self._kind = kind
        self._name = name

    @property
    def api_group(self):
        """
        Gets the api_group of this V1alpha1RoleRef.
        APIGroup is the group for the resource being referenced

        :return: The api_group of this V1alpha1RoleRef.
        :rtype: str
        """
        return self._api_group

    @api_group.setter
    def api_group(self, api_group):
        """
        Sets the api_group of this V1alpha1RoleRef.
        APIGroup is the group for the resource being referenced

        :param api_group: The api_group of this V1alpha1RoleRef.
        :type: str
        """

        self._api_group = api_group

    @property
    def kind(self):
        """
        Gets the kind of this V1alpha1RoleRef.
        Kind is the type of resource being referenced

        :return: The kind of this V1alpha1RoleRef.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1alpha1RoleRef.
        Kind is the type of resource being referenced

        :param kind: The kind of this V1alpha1RoleRef.
        :type: str
        """

        self._kind = kind

    @property
    def name(self):
        """
        Gets the name of this V1alpha1RoleRef.
        Name is the name of resource being referenced

        :return: The name of this V1alpha1RoleRef.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1alpha1RoleRef.
        Name is the name of resource being referenced

        :param name: The name of this V1alpha1RoleRef.
        :type: str
        """

        self._name = name

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
