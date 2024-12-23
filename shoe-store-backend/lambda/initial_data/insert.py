import json
import os

import boto3

SHOES = [
    {"id": "1", "brand": "Nike", "availableSizes": ["40", "41", "42"], "price": 100},
    {"id": "2", "brand": "Adidas", "availableSizes": ["39", "40", "43"], "price": 120},
    {"id": "3", "brand": "Puma", "availableSizes": ["38", "39", "40"], "price": 90},
]

ORDERS = [
    {
        "id": "1",
        "client": "John Doe",
        "shoeReference": "1",
        "size": "41",
        "shippingInfo": "123 Main St",
    },
    {
        "id": "2",
        "client": "Jane Doe",
        "shoeReference": "2",
        "size": "40",
        "shippingInfo": "456 Elm St",
    },
]


def handler(event, context):
    shoes_table_name = os.environ["SHOES_TABLE"]
    orders_table_name = os.environ["ORDERS_TABLE"]

    dynamodb = boto3.resource("dynamodb")
    shoes_table = dynamodb.Table(shoes_table_name)
    orders_table = dynamodb.Table(orders_table_name)

    for shoe in SHOES:
        shoes_table.put_item(Item=shoe)

    for order in ORDERS:
        orders_table.put_item(Item=order)

    return {"statusCode": 200, "body": json.dumps("Initial data inserted")}
