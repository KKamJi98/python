from kubernetes import client, config
from tabulate import tabulate

config.load_kube_config()

v1 = client.CoreV1Api()
pods = v1.list_pod_for_all_namespaces(watch=False)

# 데이터를 리스트 형태로 준비
table = []
for pod in pods.items:
    table.append([pod.metadata.namespace, pod.metadata.name])

# 테이블 출력 (GitHub 스타일)
print(tabulate(table, headers=["Namespace", "Pod Name"], tablefmt="github"))
