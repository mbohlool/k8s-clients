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

[[ -d bin ]] || mkdir bin
[[ -f bin/swagger-codegen-cli.jar ]] || curl http://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.2.1/swagger-codegen-cli-2.2.1.jar > bin/swagger-codegen-cli.jar

if [[ ! -n ${KUBE_ROOT-} ]]; then
  echo "\$KUBE_ROOT variable is not set"
  exit
fi

echo "Generating client ..."
fname="$KUBE_ROOT/api/openapi-spec/swagger.json"
pkg_name=k8sclient
echo "{\"packageName\": \"$pkg_name\", \"sortParamsByRequiredFlag\": true}" > /tmp/config
java -jar bin/swagger-codegen-cli.jar generate -l python --config /tmp/config -o . -i $fname
rm ./git_push.sh
echo "Client generated on ./$fname"
cp $KUBE_ROOT/LICENSE .

