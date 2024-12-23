import json
import os

import boto3

SHOES = [
    {"id": "1", "brand": "Nike", "available_sizes": ["40", "41", "42"], "price": 100},
    {"id": "2", "brand": "Adidas", "available_sizes": ["39", "40", "43"], "price": 120},
    {"id": "3", "brand": "Puma", "available_sizes": ["38", "39", "40"], "price": 90},
]

ORDERS = [
    {
        "order_id": "1",
        "client": "John Doe",
        "shoe_reference": "1",
        "size": "41",
        "shipping_info": "123 Main St",
    },
    {
        "order_id": "2",
        "client": "Jane Doe",
        "shoe_reference": "2",
        "size": "40",
        "shipping_info": "456 Elm St",
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
