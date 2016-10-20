# coding: utf-8

"""
    Kubernetes /apis

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


class UnversionedGroupVersionForDiscovery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, group_version=None, version=None):
        """
        UnversionedGroupVersionForDiscovery - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'group_version': 'str',
            'version': 'str'
        }

        self.attribute_map = {
            'group_version': 'groupVersion',
            'version': 'version'
        }

        self._group_version = group_version
        self._version = version

    @property
    def group_version(self):
        """
        Gets the group_version of this UnversionedGroupVersionForDiscovery.
        groupVersion specifies the API group and version in the form \"group/version\"

        :return: The group_version of this UnversionedGroupVersionForDiscovery.
        :rtype: str
        """
        return self._group_version

    @group_version.setter
    def group_version(self, group_version):
        """
        Sets the group_version of this UnversionedGroupVersionForDiscovery.
        groupVersion specifies the API group and version in the form \"group/version\"

        :param group_version: The group_version of this UnversionedGroupVersionForDiscovery.
        :type: str
        """

        self._group_version = group_version

    @property
    def version(self):
        """
        Gets the version of this UnversionedGroupVersionForDiscovery.
        version specifies the version in the form of \"version\". This is to save the clients the trouble of splitting the GroupVersion.

        :return: The version of this UnversionedGroupVersionForDiscovery.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this UnversionedGroupVersionForDiscovery.
        version specifies the version in the form of \"version\". This is to save the clients the trouble of splitting the GroupVersion.

        :param version: The version of this UnversionedGroupVersionForDiscovery.
        :type: str
        """

        self._version = version

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
