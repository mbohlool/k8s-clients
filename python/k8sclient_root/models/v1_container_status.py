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


class V1ContainerStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, container_id=None, image=None, image_id=None, last_state=None, name=None, ready=None, restart_count=None, state=None):
        """
        V1ContainerStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'container_id': 'str',
            'image': 'str',
            'image_id': 'str',
            'last_state': 'V1ContainerState',
            'name': 'str',
            'ready': 'bool',
            'restart_count': 'int',
            'state': 'V1ContainerState'
        }

        self.attribute_map = {
            'container_id': 'containerID',
            'image': 'image',
            'image_id': 'imageID',
            'last_state': 'lastState',
            'name': 'name',
            'ready': 'ready',
            'restart_count': 'restartCount',
            'state': 'state'
        }

        self._container_id = container_id
        self._image = image
        self._image_id = image_id
        self._last_state = last_state
        self._name = name
        self._ready = ready
        self._restart_count = restart_count
        self._state = state

    @property
    def container_id(self):
        """
        Gets the container_id of this V1ContainerStatus.
        Container's ID in the format 'docker://<container_id>'. More info: http://kubernetes.io/docs/user-guide/container-environment#container-information

        :return: The container_id of this V1ContainerStatus.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """
        Sets the container_id of this V1ContainerStatus.
        Container's ID in the format 'docker://<container_id>'. More info: http://kubernetes.io/docs/user-guide/container-environment#container-information

        :param container_id: The container_id of this V1ContainerStatus.
        :type: str
        """

        self._container_id = container_id

    @property
    def image(self):
        """
        Gets the image of this V1ContainerStatus.
        The image the container is running. More info: http://kubernetes.io/docs/user-guide/images

        :return: The image of this V1ContainerStatus.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this V1ContainerStatus.
        The image the container is running. More info: http://kubernetes.io/docs/user-guide/images

        :param image: The image of this V1ContainerStatus.
        :type: str
        """

        self._image = image

    @property
    def image_id(self):
        """
        Gets the image_id of this V1ContainerStatus.
        ImageID of the container's image.

        :return: The image_id of this V1ContainerStatus.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this V1ContainerStatus.
        ImageID of the container's image.

        :param image_id: The image_id of this V1ContainerStatus.
        :type: str
        """

        self._image_id = image_id

    @property
    def last_state(self):
        """
        Gets the last_state of this V1ContainerStatus.
        Details about the container's last termination condition.

        :return: The last_state of this V1ContainerStatus.
        :rtype: V1ContainerState
        """
        return self._last_state

    @last_state.setter
    def last_state(self, last_state):
        """
        Sets the last_state of this V1ContainerStatus.
        Details about the container's last termination condition.

        :param last_state: The last_state of this V1ContainerStatus.
        :type: V1ContainerState
        """

        self._last_state = last_state

    @property
    def name(self):
        """
        Gets the name of this V1ContainerStatus.
        This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be updated.

        :return: The name of this V1ContainerStatus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1ContainerStatus.
        This must be a DNS_LABEL. Each container in a pod must have a unique name. Cannot be updated.

        :param name: The name of this V1ContainerStatus.
        :type: str
        """

        self._name = name

    @property
    def ready(self):
        """
        Gets the ready of this V1ContainerStatus.
        Specifies whether the container has passed its readiness probe.

        :return: The ready of this V1ContainerStatus.
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """
        Sets the ready of this V1ContainerStatus.
        Specifies whether the container has passed its readiness probe.

        :param ready: The ready of this V1ContainerStatus.
        :type: bool
        """

        self._ready = ready

    @property
    def restart_count(self):
        """
        Gets the restart_count of this V1ContainerStatus.
        The number of times the container has been restarted, currently based on the number of dead containers that have not yet been removed. Note that this is calculated from dead containers. But those containers are subject to garbage collection. This value will get capped at 5 by GC.

        :return: The restart_count of this V1ContainerStatus.
        :rtype: int
        """
        return self._restart_count

    @restart_count.setter
    def restart_count(self, restart_count):
        """
        Sets the restart_count of this V1ContainerStatus.
        The number of times the container has been restarted, currently based on the number of dead containers that have not yet been removed. Note that this is calculated from dead containers. But those containers are subject to garbage collection. This value will get capped at 5 by GC.

        :param restart_count: The restart_count of this V1ContainerStatus.
        :type: int
        """

        self._restart_count = restart_count

    @property
    def state(self):
        """
        Gets the state of this V1ContainerStatus.
        Details about the container's current condition.

        :return: The state of this V1ContainerStatus.
        :rtype: V1ContainerState
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this V1ContainerStatus.
        Details about the container's current condition.

        :param state: The state of this V1ContainerStatus.
        :type: V1ContainerState
        """

        self._state = state

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
