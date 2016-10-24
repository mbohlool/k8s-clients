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
from k8sclient.apis.v1alpha1_policy_api import V1alpha1PolicyApi


class TestV1alpha1PolicyApi(unittest.TestCase):
    """ V1alpha1PolicyApi unit test stubs """

    def setUp(self):
        self.api = k8sclient.apis.v1alpha1_policy_api.V1alpha1PolicyApi()

    def tearDown(self):
        pass

    def test_create_policy_v1alpha1_namespaced_pod_disruption_budget(self):
        """
        Test case for create_policy_v1alpha1_namespaced_pod_disruption_budget

        
        """
        pass

    def test_delete_policy_v1alpha1_collection_namespaced_pod_disruption_budget(self):
        """
        Test case for delete_policy_v1alpha1_collection_namespaced_pod_disruption_budget

        
        """
        pass

    def test_delete_policy_v1alpha1_namespaced_pod_disruption_budget(self):
        """
        Test case for delete_policy_v1alpha1_namespaced_pod_disruption_budget

        
        """
        pass

    def test_get_policy_v1alpha1_api_resources(self):
        """
        Test case for get_policy_v1alpha1_api_resources

        
        """
        pass

    def test_list_policy_v1alpha1_namespaced_pod_disruption_budget(self):
        """
        Test case for list_policy_v1alpha1_namespaced_pod_disruption_budget

        
        """
        pass

    def test_list_policy_v1alpha1_pod_disruption_budget_for_all_namespaces(self):
        """
        Test case for list_policy_v1alpha1_pod_disruption_budget_for_all_namespaces

        
        """
        pass

    def test_patch_policy_v1alpha1_namespaced_pod_disruption_budget(self):
        """
        Test case for patch_policy_v1alpha1_namespaced_pod_disruption_budget

        
        """
        pass

    def test_patch_policy_v1alpha1_namespaced_pod_disruption_budget_status(self):
        """
        Test case for patch_policy_v1alpha1_namespaced_pod_disruption_budget_status

        
        """
        pass

    def test_read_policy_v1alpha1_namespaced_pod_disruption_budget(self):
        """
        Test case for read_policy_v1alpha1_namespaced_pod_disruption_budget

        
        """
        pass

    def test_read_policy_v1alpha1_namespaced_pod_disruption_budget_status(self):
        """
        Test case for read_policy_v1alpha1_namespaced_pod_disruption_budget_status

        
        """
        pass

    def test_replace_policy_v1alpha1_namespaced_pod_disruption_budget(self):
        """
        Test case for replace_policy_v1alpha1_namespaced_pod_disruption_budget

        
        """
        pass

    def test_replace_policy_v1alpha1_namespaced_pod_disruption_budget_status(self):
        """
        Test case for replace_policy_v1alpha1_namespaced_pod_disruption_budget_status

        
        """
        pass

    def test_watch_policy_v1alpha1_namespaced_pod_disruption_budget(self):
        """
        Test case for watch_policy_v1alpha1_namespaced_pod_disruption_budget

        
        """
        pass

    def test_watch_policy_v1alpha1_namespaced_pod_disruption_budget_list(self):
        """
        Test case for watch_policy_v1alpha1_namespaced_pod_disruption_budget_list

        
        """
        pass

    def test_watch_policy_v1alpha1_pod_disruption_budget_list_for_all_namespaces(self):
        """
        Test case for watch_policy_v1alpha1_pod_disruption_budget_list_for_all_namespaces

        
        """
        pass


if __name__ == '__main__':
    unittest.main()