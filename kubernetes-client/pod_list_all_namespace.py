#!/usr/bin/env python

import sys
import time
from kubernetes import client, config, watch
from tabulate import tabulate


def main_menu():
    """메인 메뉴를 출력하고 사용자 입력을 받는다."""
    print("\n=== Kubernetes Monitoring Tool ===")
    print("1) List Nodes")
    print("2) List Pods")
    print("3) List Deployments")
    print("4) List DaemonSets")
    print("5) List StatefulSets")
    print("6) Watch Events (real-time)")
    print("Q) Quit")
    return input("Select an option: ").strip()


def list_nodes():
    """노드 목록을 tabulate로 깔끔하게 출력."""
    v1 = client.CoreV1Api()
    nodes = v1.list_node()
    table = []
    for node in nodes.items:
        name = node.metadata.name
        # 예시로 Allocatable CPU, Memory도 함께 출력
        alloc_cpu = node.status.allocatable.get("cpu", "?")
        alloc_mem = node.status.allocatable.get("memory", "?")
        table.append([name, alloc_cpu, alloc_mem])

    print("\n[Nodes]")
    print(tabulate(table, headers=["Name", "CPU", "Memory"], tablefmt="github"))


def list_pods():
    """파드 목록을 tabulate로 깔끔하게 출력."""
    v1 = client.CoreV1Api()
    pods = v1.list_pod_for_all_namespaces(watch=False)
    table = []
    for pod in pods.items:
        ns = pod.metadata.namespace
        name = pod.metadata.name
        phase = pod.status.phase
        restarts = 0
        if pod.status.container_statuses:
            restarts = sum(cs.restart_count for cs in pod.status.container_statuses)
        table.append([ns, name, phase, restarts])

    print("\n[Pods]")
    print(
        tabulate(
            table,
            headers=["Namespace", "Pod Name", "Phase", "Restarts"],
            tablefmt="github",
        )
    )


def list_deployments():
    """디플로이먼트 목록을 tabulate로 출력."""
    apps_v1 = client.AppsV1Api()
    deps = apps_v1.list_deployment_for_all_namespaces()
    table = []
    for d in deps.items:
        ns = d.metadata.namespace
        name = d.metadata.name
        replicas = f"{d.status.ready_replicas or 0}/{d.spec.replicas}"
        table.append([ns, name, replicas])
    print("\n[Deployments]")
    print(
        tabulate(table, headers=["Namespace", "Name", "Ready/Total"], tablefmt="github")
    )


def list_daemonsets():
    """데몬셋 목록"""
    apps_v1 = client.AppsV1Api()
    dss = apps_v1.list_daemon_set_for_all_namespaces()
    table = []
    for ds in dss.items:
        ns = ds.metadata.namespace
        name = ds.metadata.name
        desired = ds.status.desired_number_scheduled
        ready = ds.status.number_ready
        table.append([ns, name, f"{ready}/{desired}"])
    print("\n[DaemonSets]")
    print(
        tabulate(
            table, headers=["Namespace", "Name", "Ready/Desired"], tablefmt="github"
        )
    )


def list_statefulsets():
    """스테이트풀셋 목록"""
    apps_v1 = client.AppsV1Api()
    sts_list = apps_v1.list_stateful_set_for_all_namespaces()
    table = []
    for sts in sts_list.items:
        ns = sts.metadata.namespace
        name = sts.metadata.name
        replicas = f"{sts.status.ready_replicas or 0}/{sts.spec.replicas}"
        table.append([ns, name, replicas])
    print("\n[StatefulSets]")
    print(
        tabulate(table, headers=["Namespace", "Name", "Ready/Total"], tablefmt="github")
    )


def watch_events():
    """이벤트를 실시간으로 감시하여 콘솔에 표시."""
    v1 = client.CoreV1Api()
    w = watch.Watch()
    print("\n[Watching Events - press Ctrl+C to stop]")
    try:
        for event in w.stream(v1.list_event_for_all_namespaces):
            evt_obj = event["object"]
            # 이벤트 이름, 타입, 메시지, 발생 네임스페이스, 리소스 참조 등을 출력
            ns = evt_obj.metadata.namespace
            reason = evt_obj.reason
            message = evt_obj.message
            involved = (
                evt_obj.involved_object.kind
                + "/"
                + (evt_obj.involved_object.name or "")
            )
            print(f"* [{ns or 'cluster'}] {reason}: {message} (involved: {involved})")
    except KeyboardInterrupt:
        print("\nStopped watching events.")


def main():
    # kubeconfig 로드 (로컬 환경)
    config.load_kube_config()

    while True:
        choice = main_menu()
        if choice == "1":
            list_nodes()
        elif choice == "2":
            list_pods()
        elif choice == "3":
            list_deployments()
        elif choice == "4":
            list_daemonsets()
        elif choice == "5":
            list_statefulsets()
        elif choice == "6":
            watch_events()
        elif choice.lower() == "q":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
