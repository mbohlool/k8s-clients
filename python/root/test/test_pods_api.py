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
from k8sclient.apis.pods_api import PodsApi


class TestPodsApi(unittest.TestCase):
    """ PodsApi unit test stubs """

    def setUp(self):
        self.api = k8sclient.apis.pods_api.PodsApi()

    def tearDown(self):
        pass

    def test_connect_delete_namespaced_pod_proxy(self):
        """
        Test case for connect_delete_namespaced_pod_proxy

        
        """
        pass

    def test_connect_delete_namespaced_pod_proxy_with_path(self):
        """
        Test case for connect_delete_namespaced_pod_proxy_with_path

        
        """
        pass

    def test_connect_get_namespaced_pod_attach(self):
        """
        Test case for connect_get_namespaced_pod_attach

        
        """
        pass

    def test_connect_get_namespaced_pod_exec(self):
        """
        Test case for connect_get_namespaced_pod_exec

        
        """
        pass

    def test_connect_get_namespaced_pod_portforward(self):
        """
        Test case for connect_get_namespaced_pod_portforward

        
        """
        pass

    def test_connect_get_namespaced_pod_proxy(self):
        """
        Test case for connect_get_namespaced_pod_proxy

        
        """
        pass

    def test_connect_get_namespaced_pod_proxy_with_path(self):
        """
        Test case for connect_get_namespaced_pod_proxy_with_path

        
        """
        pass

    def test_connect_head_namespaced_pod_proxy(self):
        """
        Test case for connect_head_namespaced_pod_proxy

        
        """
        pass

    def test_connect_head_namespaced_pod_proxy_with_path(self):
        """
        Test case for connect_head_namespaced_pod_proxy_with_path

        
        """
        pass

    def test_connect_options_namespaced_pod_proxy(self):
        """
        Test case for connect_options_namespaced_pod_proxy

        
        """
        pass

    def test_connect_options_namespaced_pod_proxy_with_path(self):
        """
        Test case for connect_options_namespaced_pod_proxy_with_path

        
        """
        pass

    def test_connect_post_namespaced_pod_attach(self):
        """
        Test case for connect_post_namespaced_pod_attach

        
        """
        pass

    def test_connect_post_namespaced_pod_exec(self):
        """
        Test case for connect_post_namespaced_pod_exec

        
        """
        pass

    def test_connect_post_namespaced_pod_portforward(self):
        """
        Test case for connect_post_namespaced_pod_portforward

        
        """
        pass

    def test_connect_post_namespaced_pod_proxy(self):
        """
        Test case for connect_post_namespaced_pod_proxy

        
        """
        pass

    def test_connect_post_namespaced_pod_proxy_with_path(self):
        """
        Test case for connect_post_namespaced_pod_proxy_with_path

        
        """
        pass

    def test_connect_put_namespaced_pod_proxy(self):
        """
        Test case for connect_put_namespaced_pod_proxy

        
        """
        pass

    def test_connect_put_namespaced_pod_proxy_with_path(self):
        """
        Test case for connect_put_namespaced_pod_proxy_with_path

        
        """
        pass

    def test_create_namespaced_binding_binding(self):
        """
        Test case for create_namespaced_binding_binding

        
        """
        pass

    def test_create_namespaced_eviction_eviction(self):
        """
        Test case for create_namespaced_eviction_eviction

        
        """
        pass

    def test_delete_namespaced_pod(self):
        """
        Test case for delete_namespaced_pod

        
        """
        pass

    def test_patch_namespaced_pod(self):
        """
        Test case for patch_namespaced_pod

        
        """
        pass

    def test_patch_namespaced_pod_status(self):
        """
        Test case for patch_namespaced_pod_status

        
        """
        pass

    def test_proxy_delete_namespaced_pod(self):
        """
        Test case for proxy_delete_namespaced_pod

        
        """
        pass

    def test_proxy_delete_namespaced_pod_with_path(self):
        """
        Test case for proxy_delete_namespaced_pod_with_path

        
        """
        pass

    def test_proxy_get_namespaced_pod(self):
        """
        Test case for proxy_get_namespaced_pod

        
        """
        pass

    def test_proxy_get_namespaced_pod_with_path(self):
        """
        Test case for proxy_get_namespaced_pod_with_path

        
        """
        pass

    def test_proxy_head_namespaced_pod(self):
        """
        Test case for proxy_head_namespaced_pod

        
        """
        pass

    def test_proxy_head_namespaced_pod_with_path(self):
        """
        Test case for proxy_head_namespaced_pod_with_path

        
        """
        pass

    def test_proxy_options_namespaced_pod(self):
        """
        Test case for proxy_options_namespaced_pod

        
        """
        pass

    def test_proxy_options_namespaced_pod_with_path(self):
        """
        Test case for proxy_options_namespaced_pod_with_path

        
        """
        pass

    def test_proxy_post_namespaced_pod(self):
        """
        Test case for proxy_post_namespaced_pod

        
        """
        pass

    def test_proxy_post_namespaced_pod_with_path(self):
        """
        Test case for proxy_post_namespaced_pod_with_path

        
        """
        pass

    def test_proxy_put_namespaced_pod(self):
        """
        Test case for proxy_put_namespaced_pod

        
        """
        pass

    def test_proxy_put_namespaced_pod_with_path(self):
        """
        Test case for proxy_put_namespaced_pod_with_path

        
        """
        pass

    def test_read_namespaced_pod(self):
        """
        Test case for read_namespaced_pod

        
        """
        pass

    def test_read_namespaced_pod_log(self):
        """
        Test case for read_namespaced_pod_log

        
        """
        pass

    def test_read_namespaced_pod_status(self):
        """
        Test case for read_namespaced_pod_status

        
        """
        pass

    def test_replace_namespaced_pod(self):
        """
        Test case for replace_namespaced_pod

        
        """
        pass

    def test_replace_namespaced_pod_status(self):
        """
        Test case for replace_namespaced_pod_status

        
        """
        pass

    def test_watch_namespaced_pod(self):
        """
        Test case for watch_namespaced_pod

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
