# Open Telemetry GCP PubSub Instrumentation for Python

This package provides automatic instrumentation for the [`google-cloud-pubsub`](https://pypi.org/project/google-cloud-pubsub/) client library.

## Installation
```bash
pip install opentelemetry-instrumentation-pubsub
```

## Usage
Initiate the instrumentor after configuring your [Open Telemetry](https://opentelemetry.io/docs/instrumentation/python/manual/) trace provider.

```python
from google.cloud import pubsub_v1
from pubsub_opentelemetry import PubSubInstrumentationProvider


# Instrument PubSub
PubSubInstrumentationProvider().instrument()

# Publish creates a span with PubSub specific attributes
with pubsub_v1.PublisherClient() as publisher:
    publisher.publish(topic_name, b'My first message!')

# Subscribe propagates the context from the received message
with pubsub_v1.SubscriberClient() as subscriber:
    subscriber.subscribe(subscription_name, callback)
```
---

[License](LICENSE)
