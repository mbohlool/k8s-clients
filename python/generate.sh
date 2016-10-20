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

skip_list="swagger_root version api apis apps version"

for i in $KUBE_ROOT/api/openapi-spec/*; 
do   
  echo "Generating client for $i ..."
  fname=$(basename $i)
  fname="${fname%.*}"
  fname=${fname/.k8s.io/}
  fname=${fname/./_}
  fname=${fname/root_swagger/root}
  pkg_name=k8sclient_$fname
  [[ -d $pkg_name ]] && rm -rf $pkg_name
  temp_dir=$(mktemp -d)
  echo "{\"packageName\": \"$pkg_name\", \"sortParamsByRequiredFlag\": true}" > /tmp/config
  java -jar bin/swagger-codegen-cli.jar generate -l python --config /tmp/config -o $temp_dir -i $i  1>&2 2>/dev/null
  cp -r $temp_dir/$pkg_name $pkg_name
  cp -r $temp_dir/docs $pkg_name/docs
  rm -rf $temp_dir
  echo "Client generated on ./$fname"
done

