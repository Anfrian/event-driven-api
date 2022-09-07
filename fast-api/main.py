from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=['https://localhost:8800'],
    allow_methods=['*'],
    allow_headers=['*']
)

redis = get_redis_connection(
    host = "redis-15324.c300.eu-central-1-1.ec2.cloud.redislabs.com",
    port = 15324,
    password="uppy6O13c4AwnaCZm3jWbOAaDaNDi4Vq",
    decode_responses=True
)

class Delivery(HashModel):
    budget: int = 0,
    notes: str = ""

    class Meta:
        database = redis

class Event(HashModel):
    delivery_id: str = None
    type: str
    date: str

    class Meta:
        database = redis

@app.post('/deliveries/create')
async def create(request: Request):
    body = await request.json()
    delivery = Delivery(
        budget = body['data']['budget']
    )

