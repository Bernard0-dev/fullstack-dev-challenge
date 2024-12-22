import os

import aws_cdk.aws_appsync as appsync
import aws_cdk.aws_dynamodb as dynamodb
from aws_cdk import Stack
from constructs import Construct


class ShoeStoreBackendStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # DYNAMODB
        shoes_table = dynamodb.Table(
            self,
            "Shoes",
            partition_key=dynamodb.Attribute(
                name="id", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
        )

        orders_table = dynamodb.Table(
            self,
            "Orders",
            partition_key=dynamodb.Attribute(
                name="id", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
        )

        # APPSYNC
        schema_file_path = os.path.join(os.path.dirname(__file__), "schema.graphql")

        api = appsync.GraphqlApi(
            self,
            "ShoeStoreApi",
            name="ShoeStoreApi",
            definition=appsync.Definition.from_file(schema_file_path),
        )

        api.add_dynamo_db_data_source("ShoesDataSource", shoes_table)
        api.add_dynamo_db_data_source("OrdersDataSource", orders_table)
