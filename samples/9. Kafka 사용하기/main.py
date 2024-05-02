
from fastapi import FastAPI
from kafka_producer import MessageProducer

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/send/{message}")
def read_item(message: str):
    
    # 브로커와 토픽명을 지정한다.
    broker = ["kafka01:9092", "kafka02:9092", "kafka03:9092"]
    topic = "employees"
    pd = MessageProducer(broker, topic)

    msg = {"message": message}
    res = pd.send_message(msg)
    print(res)
    
    return {"res": res}


# https://fastapi.tiangolo.com/ko/