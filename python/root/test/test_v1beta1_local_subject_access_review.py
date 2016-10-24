# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

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

import os
import sys
import unittest

import k8sclient
from k8sclient.rest import ApiException
from k8sclient.models.v1beta1_local_subject_access_review import V1beta1LocalSubjectAccessReview


class TestV1beta1LocalSubjectAccessReview(unittest.TestCase):
    """ V1beta1LocalSubjectAccessReview unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1LocalSubjectAccessReview(self):
        """
        Test V1beta1LocalSubjectAccessReview
        """
        model = k8sclient.models.v1beta1_local_subject_access_review.V1beta1LocalSubjectAccessReview()


if __name__ == '__main__':
    unittest.main()
