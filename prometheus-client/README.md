# Prometheus Client Examples

This directory contains Python examples for instrumenting applications with Prometheus metrics.

## Files

- **counter.py**: Example of using Prometheus Counter metric type
- **gauge.py**: Example of using Prometheus Gauge metric type

## Requirements

```
prometheus-client==0.17.1
```

## Usage

Each example runs a simple HTTP server that exposes both an application endpoint and a metrics endpoint.

### Counter Example

```bash
python counter.py
```

- Application server runs on port 18080
- Metrics server runs on port 18081
- Access http://localhost:18080 to increment the counter
- Access http://localhost:18081 to view the metrics

### Gauge Example

```bash
python gauge.py
```

- Application server runs on port 18080
- Metrics server runs on port 18081
- Access http://localhost:18080 to see the gauge in action
- Access http://localhost:18081 to view the metrics

## Metrics Exposed

### Counter Example
- `app_requests_count`: Total number of HTTP requests received

### Gauge Example
- `app_request_inprogress`: Number of requests currently being processed
- `app_last_served`: Timestamp of when the last request was served
