#!/bin/bash

# Copyright 2015 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Script to fetch latest swagger spec.
# Puts the updated spec at api/swagger-spec/

set -o errexit
set -o nounset
set -o pipefail

SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
CLIENT_ROOT=${SCRIPT_ROOT}/..

[[ -d ${CLIENT_ROOT}/bin ]] || mkdir bin
[[ -f ${CLIENT_ROOT}/bin/swagger-codegen-cli.jar ]] || curl http://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.2.1/swagger-codegen-cli-2.2.1.jar > ${CLIENT_ROOT}/bin/swagger-codegen-cli.jar

if [[ ! -n ${SWAGGER_FILE-} ]]; then
  if [[ ! -n ${KUBE_ROOT-} ]]; then
    echo "\$KUBE_ROOT variable is not set"
    exit
  fi
  SWAGGER_FILE=${KUBE_ROOT}/api/openapi-spec/swagger.json
  FROM_KUBE="True"
fi

pkg_name=k8sclient
echo "Cleaning up previously generated folders"
rm -rf ${CLIENT_ROOT}/${pkg_name}
rm -rf ${CLIENT_ROOT}/docs
rm -rf ${CLIENT_ROOT}/tests
echo "Generating client ..."
pkg_name=k8sclient
java -jar ${CLIENT_ROOT}/bin/swagger-codegen-cli.jar generate -l python --config ${SCRIPT_ROOT}/config -o ${CLIENT_ROOT} -i ${SWAGGER_FILE}
rm ${CLIENT_ROOT}/git_push.sh
echo "Client generated on ${CLIENT_ROOT}/"
if [[ -n ${FROM_KUBE-} ]]; then
  cp $KUBE_ROOT/LICENSE ${CLIENT_ROOT}
fi
