# coding: utf-8

"""
    Kubernetes /apis/authorization.k8s.io/v1beta1

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

from __future__ import absolute_import

# import models into sdk package
from .models.unversioned_api_resource import UnversionedAPIResource
from .models.unversioned_api_resource_list import UnversionedAPIResourceList
from .models.unversioned_time import UnversionedTime
from .models.v1_object_meta import V1ObjectMeta
from .models.v1_owner_reference import V1OwnerReference
from .models.v1beta1_local_subject_access_review import V1beta1LocalSubjectAccessReview
from .models.v1beta1_non_resource_attributes import V1beta1NonResourceAttributes
from .models.v1beta1_resource_attributes import V1beta1ResourceAttributes
from .models.v1beta1_self_subject_access_review import V1beta1SelfSubjectAccessReview
from .models.v1beta1_self_subject_access_review_spec import V1beta1SelfSubjectAccessReviewSpec
from .models.v1beta1_subject_access_review import V1beta1SubjectAccessReview
from .models.v1beta1_subject_access_review_spec import V1beta1SubjectAccessReviewSpec
from .models.v1beta1_subject_access_review_status import V1beta1SubjectAccessReviewStatus

# import apis into sdk package
from .apis.default_api import DefaultApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()