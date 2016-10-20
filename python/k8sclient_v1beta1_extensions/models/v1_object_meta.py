# coding: utf-8

"""
    Kubernetes /apis/extensions/v1beta1

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


class V1ObjectMeta(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, annotations=None, cluster_name=None, creation_timestamp=None, deletion_grace_period_seconds=None, deletion_timestamp=None, finalizers=None, generate_name=None, generation=None, labels=None, name=None, namespace=None, owner_references=None, resource_version=None, self_link=None, uid=None):
        """
        V1ObjectMeta - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'annotations': 'dict(str, str)',
            'cluster_name': 'str',
            'creation_timestamp': 'UnversionedTime',
            'deletion_grace_period_seconds': 'int',
            'deletion_timestamp': 'UnversionedTime',
            'finalizers': 'list[str]',
            'generate_name': 'str',
            'generation': 'int',
            'labels': 'dict(str, str)',
            'name': 'str',
            'namespace': 'str',
            'owner_references': 'list[V1OwnerReference]',
            'resource_version': 'str',
            'self_link': 'str',
            'uid': 'str'
        }

        self.attribute_map = {
            'annotations': 'annotations',
            'cluster_name': 'clusterName',
            'creation_timestamp': 'creationTimestamp',
            'deletion_grace_period_seconds': 'deletionGracePeriodSeconds',
            'deletion_timestamp': 'deletionTimestamp',
            'finalizers': 'finalizers',
            'generate_name': 'generateName',
            'generation': 'generation',
            'labels': 'labels',
            'name': 'name',
            'namespace': 'namespace',
            'owner_references': 'ownerReferences',
            'resource_version': 'resourceVersion',
            'self_link': 'selfLink',
            'uid': 'uid'
        }

        self._annotations = annotations
        self._cluster_name = cluster_name
        self._creation_timestamp = creation_timestamp
        self._deletion_grace_period_seconds = deletion_grace_period_seconds
        self._deletion_timestamp = deletion_timestamp
        self._finalizers = finalizers
        self._generate_name = generate_name
        self._generation = generation
        self._labels = labels
        self._name = name
        self._namespace = namespace
        self._owner_references = owner_references
        self._resource_version = resource_version
        self._self_link = self_link
        self._uid = uid

    @property
    def annotations(self):
        """
        Gets the annotations of this V1ObjectMeta.
        Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations

        :return: The annotations of this V1ObjectMeta.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """
        Sets the annotations of this V1ObjectMeta.
        Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations

        :param annotations: The annotations of this V1ObjectMeta.
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def cluster_name(self):
        """
        Gets the cluster_name of this V1ObjectMeta.
        The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.

        :return: The cluster_name of this V1ObjectMeta.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """
        Sets the cluster_name of this V1ObjectMeta.
        The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.

        :param cluster_name: The cluster_name of this V1ObjectMeta.
        :type: str
        """

        self._cluster_name = cluster_name

    @property
    def creation_timestamp(self):
        """
        Gets the creation_timestamp of this V1ObjectMeta.
        CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.  Populated by the system. Read-only. Null for lists. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :return: The creation_timestamp of this V1ObjectMeta.
        :rtype: UnversionedTime
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """
        Sets the creation_timestamp of this V1ObjectMeta.
        CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.  Populated by the system. Read-only. Null for lists. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :param creation_timestamp: The creation_timestamp of this V1ObjectMeta.
        :type: UnversionedTime
        """

        self._creation_timestamp = creation_timestamp

    @property
    def deletion_grace_period_seconds(self):
        """
        Gets the deletion_grace_period_seconds of this V1ObjectMeta.
        Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.

        :return: The deletion_grace_period_seconds of this V1ObjectMeta.
        :rtype: int
        """
        return self._deletion_grace_period_seconds

    @deletion_grace_period_seconds.setter
    def deletion_grace_period_seconds(self, deletion_grace_period_seconds):
        """
        Sets the deletion_grace_period_seconds of this V1ObjectMeta.
        Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.

        :param deletion_grace_period_seconds: The deletion_grace_period_seconds of this V1ObjectMeta.
        :type: int
        """

        self._deletion_grace_period_seconds = deletion_grace_period_seconds

    @property
    def deletion_timestamp(self):
        """
        Gets the deletion_timestamp of this V1ObjectMeta.
        DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource will be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field. Once set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. Once the resource is deleted in the API, the Kubelet will send a hard termination signal to the container. If not set, graceful deletion of the object has not been requested.  Populated by the system when a graceful deletion is requested. Read-only. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :return: The deletion_timestamp of this V1ObjectMeta.
        :rtype: UnversionedTime
        """
        return self._deletion_timestamp

    @deletion_timestamp.setter
    def deletion_timestamp(self, deletion_timestamp):
        """
        Sets the deletion_timestamp of this V1ObjectMeta.
        DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource will be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field. Once set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. Once the resource is deleted in the API, the Kubelet will send a hard termination signal to the container. If not set, graceful deletion of the object has not been requested.  Populated by the system when a graceful deletion is requested. Read-only. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :param deletion_timestamp: The deletion_timestamp of this V1ObjectMeta.
        :type: UnversionedTime
        """

        self._deletion_timestamp = deletion_timestamp

    @property
    def finalizers(self):
        """
        Gets the finalizers of this V1ObjectMeta.
        Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed.

        :return: The finalizers of this V1ObjectMeta.
        :rtype: list[str]
        """
        return self._finalizers

    @finalizers.setter
    def finalizers(self, finalizers):
        """
        Sets the finalizers of this V1ObjectMeta.
        Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed.

        :param finalizers: The finalizers of this V1ObjectMeta.
        :type: list[str]
        """

        self._finalizers = finalizers

    @property
    def generate_name(self):
        """
        Gets the generate_name of this V1ObjectMeta.
        GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.  If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).  Applied only if Name is not specified. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#idempotency

        :return: The generate_name of this V1ObjectMeta.
        :rtype: str
        """
        return self._generate_name

    @generate_name.setter
    def generate_name(self, generate_name):
        """
        Sets the generate_name of this V1ObjectMeta.
        GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.  If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).  Applied only if Name is not specified. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#idempotency

        :param generate_name: The generate_name of this V1ObjectMeta.
        :type: str
        """

        self._generate_name = generate_name

    @property
    def generation(self):
        """
        Gets the generation of this V1ObjectMeta.
        A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.

        :return: The generation of this V1ObjectMeta.
        :rtype: int
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """
        Sets the generation of this V1ObjectMeta.
        A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.

        :param generation: The generation of this V1ObjectMeta.
        :type: int
        """

        self._generation = generation

    @property
    def labels(self):
        """
        Gets the labels of this V1ObjectMeta.
        Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        :return: The labels of this V1ObjectMeta.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this V1ObjectMeta.
        Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        :param labels: The labels of this V1ObjectMeta.
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def name(self):
        """
        Gets the name of this V1ObjectMeta.
        Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names

        :return: The name of this V1ObjectMeta.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1ObjectMeta.
        Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names

        :param name: The name of this V1ObjectMeta.
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """
        Gets the namespace of this V1ObjectMeta.
        Namespace defines the space within each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.  Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces

        :return: The namespace of this V1ObjectMeta.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this V1ObjectMeta.
        Namespace defines the space within each name must be unique. An empty namespace is equivalent to the \"default\" namespace, but \"default\" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.  Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces

        :param namespace: The namespace of this V1ObjectMeta.
        :type: str
        """

        self._namespace = namespace

    @property
    def owner_references(self):
        """
        Gets the owner_references of this V1ObjectMeta.
        List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.

        :return: The owner_references of this V1ObjectMeta.
        :rtype: list[V1OwnerReference]
        """
        return self._owner_references

    @owner_references.setter
    def owner_references(self, owner_references):
        """
        Sets the owner_references of this V1ObjectMeta.
        List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.

        :param owner_references: The owner_references of this V1ObjectMeta.
        :type: list[V1OwnerReference]
        """

        self._owner_references = owner_references

    @property
    def resource_version(self):
        """
        Gets the resource_version of this V1ObjectMeta.
        An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.  Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#concurrency-control-and-consistency

        :return: The resource_version of this V1ObjectMeta.
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """
        Sets the resource_version of this V1ObjectMeta.
        An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.  Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#concurrency-control-and-consistency

        :param resource_version: The resource_version of this V1ObjectMeta.
        :type: str
        """

        self._resource_version = resource_version

    @property
    def self_link(self):
        """
        Gets the self_link of this V1ObjectMeta.
        SelfLink is a URL representing this object. Populated by the system. Read-only.

        :return: The self_link of this V1ObjectMeta.
        :rtype: str
        """
        return self._self_link

    @self_link.setter
    def self_link(self, self_link):
        """
        Sets the self_link of this V1ObjectMeta.
        SelfLink is a URL representing this object. Populated by the system. Read-only.

        :param self_link: The self_link of this V1ObjectMeta.
        :type: str
        """

        self._self_link = self_link

    @property
    def uid(self):
        """
        Gets the uid of this V1ObjectMeta.
        UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.  Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids

        :return: The uid of this V1ObjectMeta.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this V1ObjectMeta.
        UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.  Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids

        :param uid: The uid of this V1ObjectMeta.
        :type: str
        """

        self._uid = uid

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
