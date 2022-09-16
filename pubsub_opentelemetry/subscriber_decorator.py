from __future__ import annotations

from typing import Any, Callable

from google.cloud.pubsub_v1.subscriber.message import Message
from opentelemetry import propagate, trace
from opentelemetry.semconv.trace import SpanAttributes


class SubscriberDecorator:
    """
    Apply the SubscriberClient decorator
    """

    def __init__(self, tracer: trace.Tracer):
        self._tracer = tracer

    def _decorate_callback(
        self, subscription: str, callback: Callable[[Message], Any]
    ) -> Callable[[Message], Any]:
        """
        Decorate the 'subscribe()' callback, start a new span
        """

        def _decorated_callback(message: Message):
            ctx = propagate.extract(message.attributes)
            attributes = {
                SpanAttributes.MESSAGING_SYSTEM: 'pubsub',
                SpanAttributes.MESSAGING_OPERATION: 'process',
                SpanAttributes.MESSAGING_DESTINATION: subscription,
                SpanAttributes.MESSAGING_DESTINATION_KIND: 'subscription',
                SpanAttributes.MESSAGING_MESSAGE_ID: message.message_id,
                SpanAttributes.MESSAGING_PROTOCOL: 'pubsub',
                SpanAttributes.MESSAGING_MESSAGE_PAYLOAD_SIZE_BYTES: len(message.data),
            }
            span = self._tracer.start_span(
                f'{subscription} process',
                kind=trace.SpanKind.CONSUMER,
                attributes=attributes,
                context=ctx,
            )
            with trace.use_span(span, end_on_exit=True):
                return callback(message)

        return _decorated_callback

    def decorate(self, subscribe: Callable) -> Callable:
        """
        Decorate the 'publish()' function, start a new span
        """

        def _decorated_subscribe(
            subscription: str, callback: Callable[[Message], Any], *args, **kwargs
        ):
            decorated_callback = self._decorate_callback(subscription, callback)
            return subscribe(subscription, decorated_callback, *args, **kwargs)

        return _decorated_subscribe
