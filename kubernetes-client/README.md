# Kubernetes Client Examples

This directory contains Python examples for interacting with Kubernetes clusters using the official Kubernetes Python client.

## Files

- **pod_list_all_namespace.py**: Interactive CLI tool to monitor Kubernetes resources including nodes, pods, deployments, daemonsets, statefulsets, and real-time events.

## Requirements

```
kubernetes==29.0.0
tabulate==0.9.0
```

## Usage

Make sure you have a valid kubeconfig file set up with access to your Kubernetes cluster.

```bash
# Run the interactive Kubernetes monitoring tool
python pod_list_all_namespace.py
```

## Features

- List nodes with resource information
- List pods across all namespaces
- List deployments with replica status
- List daemonsets with ready/desired counts
- List statefulsets with replica status
- Watch real-time Kubernetes events
