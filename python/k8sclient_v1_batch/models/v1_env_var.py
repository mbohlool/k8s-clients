# coding: utf-8

"""
    Kubernetes /apis/batch/v1

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


class V1EnvVar(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, value=None, value_from=None):
        """
        V1EnvVar - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'value': 'str',
            'value_from': 'V1EnvVarSource'
        }

        self.attribute_map = {
            'name': 'name',
            'value': 'value',
            'value_from': 'valueFrom'
        }

        self._name = name
        self._value = value
        self._value_from = value_from

    @property
    def name(self):
        """
        Gets the name of this V1EnvVar.
        Name of the environment variable. Must be a C_IDENTIFIER.

        :return: The name of this V1EnvVar.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1EnvVar.
        Name of the environment variable. Must be a C_IDENTIFIER.

        :param name: The name of this V1EnvVar.
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """
        Gets the value of this V1EnvVar.
        Variable references $(VAR_NAME) are expanded using the previous defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to \"\".

        :return: The value of this V1EnvVar.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this V1EnvVar.
        Variable references $(VAR_NAME) are expanded using the previous defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to \"\".

        :param value: The value of this V1EnvVar.
        :type: str
        """

        self._value = value

    @property
    def value_from(self):
        """
        Gets the value_from of this V1EnvVar.
        Source for the environment variable's value. Cannot be used if value is not empty.

        :return: The value_from of this V1EnvVar.
        :rtype: V1EnvVarSource
        """
        return self._value_from

    @value_from.setter
    def value_from(self, value_from):
        """
        Sets the value_from of this V1EnvVar.
        Source for the environment variable's value. Cannot be used if value is not empty.

        :param value_from: The value_from of this V1EnvVar.
        :type: V1EnvVarSource
        """

        self._value_from = value_from

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
