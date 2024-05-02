from kafka import KafkaProducer
import json


class MessageProducer:
    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=self.broker,
            value_serializer=lambda x: json.dumps(x).encode("utf-8"),
            acks=0,
            api_version=(2, 5, 0),
            retries=3,
        )

    def send_message(self, msg, auto_close=True):
        try:
            future = self.producer.send(self.topic, msg)
            self.producer.flush()  # 비우는 작업
            if auto_close:
                self.producer.close()
            future.get(timeout=2)
            return {"status_code": 200, "error": None}
        except Exception as exc:
            raise exc

if __name__ == '__main__':
    # 브로커와 토픽명을 지정한다.
    broker = ["kafka01:9092", "kafka02:9092", "kafka03:9092"]
    topic = "employees"
    pd = MessageProducer(broker, topic)

    msg = {"name": "John", "age": 30}
    res = pd.send_message(msg)
    print(res)

