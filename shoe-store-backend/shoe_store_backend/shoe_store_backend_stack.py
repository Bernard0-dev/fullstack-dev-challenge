from aws_cdk import Stack, aws_appsync, aws_dynamodb
from constructs import Construct


class ShoeStoreBackendStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # DYNAMODB
        shoes_table = aws_dynamodb.Table(
            self,
            "Shoes",
            partition_key=aws_dynamodb.Attribute(
                name="id", type=aws_dynamodb.AttributeType.STRING
            ),
            billing_mode=aws_dynamodb.BillingMode.PAY_PER_REQUEST,
        )

        orders_table = aws_dynamodb.Table(
            self,
            "Orders",
            partition_key=aws_dynamodb.Attribute(
                name="id", type=aws_dynamodb.AttributeType.STRING
            ),
            billing_mode=aws_dynamodb.BillingMode.PAY_PER_REQUEST,
        )

        # APPSYNC
        api = aws_appsync.GraphqlApi(
            self,
            "ShoeStoreApi",
            name="ShoeStoreApi",
            schema=aws_appsync.Schema.from_asset("schema.graphql"),
            authorization_config=aws_appsync.AuthorizationConfig(
                default_authorization=aws_appsync.AuthorizationMode.API_KEY,
            ),
        )

        api.add_dynamo_db_data_source("ShoesDataSource", shoes_table)
        api.add_dynamo_db_data_source("OrdersDataSource", orders_table)
