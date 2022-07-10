import json
import requests


def hello(event, context):
    return {"statusCode": 200, "body": "Hello"}


def characters(event, context):
    res = requests.get("https://rickandmortyapi.com/api/character")
    return {"statusCode": 200, "body": res.text}

# def test(event, context):
#     body = {
#         "message": "Go Serverless v3.0! Your function executed successfully!",
#         "input": event,
#     }

#     return {"statusCode": 200, "body": json.dumps(body)}
