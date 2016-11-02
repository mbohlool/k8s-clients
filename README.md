# k8s-clients

## Quick Install

To give this Kubernetes Python client a quick go, here is a walkthrough:

Use `virtualenv`, make sure your `pip` is up to date

```
$ virtualenv kube
$ cd kube
$ . bin/activate
$ pip install --upgrade pip
```

Clone this repository and get in the Python directory

```
$ git clone https://github.com/mbohlool/k8s-clients.git
$ cd k8s-clients/python
```

Now install the client module like so:

```
$ pip install .
```

You are now ready to run your first Python script that talks to the Kubernetes API.
Use a `proxy` to talk to your Kubernetes endpoint locally

```
$ kubectl proxy
```

And in a separate terminal, run the following Python script which will list your Pods in the default namespace.

```
import k8sclient

k8sclient.configuration.host="http://127.0.0.1:8001"

api_instance=k8sclient.CoreV1Api()

resp = api_instance.list_core_v1_namespaced_pod('default')
for pod in resp.items:
	print pod.metadata.name
	for container in pod.spec.containers:
		print container.name
```
