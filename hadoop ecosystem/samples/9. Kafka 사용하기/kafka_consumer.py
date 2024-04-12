from kafka import KafkaConsumer


class MessageConsumer:
    def __init__(self, broker, topic):
        self.broker = broker
        self.consumer = KafkaConsumer(
            topic,  # Topic to consume
            bootstrap_servers=self.broker,
            value_deserializer=lambda x: x.decode(
                "utf-8"
            ),  # Decode message value as utf-8
            group_id="my-group",  # Consumer group ID
            auto_offset_reset="earliest",  # Start consuming from earliest available message
            enable_auto_commit=True,  # Commit offsets automatically
        )

    def receive_message(self):
        try:
            for message in self.consumer:
                print(message.value)
        except Exception as exc:
            raise exc

if __name__ == '__main__':
    # 브로커와 토픽명을 지정한다.
    broker = ["kafka01:9092", "kafka02:9092", "kafka03:9092"]
    topic = "employees"
    cs = MessageConsumer(broker, topic)
    cs.receive_message()
