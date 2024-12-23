import os

import aws_cdk.aws_appsync as appsync
import aws_cdk.aws_dynamodb as dynamodb
import aws_cdk.aws_iam as iam
import aws_cdk.aws_lambda as aws_lambda
import aws_cdk.custom_resources as cr
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

        self.setup_initial_data(shoes_table=shoes_table, orders_table=orders_table)

    def setup_initial_data(self, shoes_table: str, orders_table: str):
        initial_data_lambda = aws_lambda.Function(
            self,
            "InitialDataLambda",
            runtime=aws_lambda.Runtime.PYTHON_3_12,
            handler="insert.handler",
            code=aws_lambda.Code.from_asset("lambda/initial_data"),
            environment={
                "SHOES_TABLE_NAME": shoes_table.table_name,
                "ORDERS_TABLE": orders_table.table_name,
            },
        )
        shoes_table.grant_write_data(initial_data_lambda)

        custom_resource_role = iam.Role(
            self,
            "CustomResourceRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        )
        custom_resource_role.add_to_policy(
            iam.PolicyStatement(
                actions=["lambda:InvokeFunction"],
                resources=[initial_data_lambda.function_arn],
            )
        )

        cr.AwsCustomResource(
            self,
            "InvokeInitialDataLambda",
            on_create={
                "service": "Lambda",
                "action": "invoke",
                "parameters": {
                    "FunctionName": initial_data_lambda.function_name,
                    "InvocationType": "Event",
                },
                "physical_resource_id": cr.PhysicalResourceId.of(
                    "InitialDataLambdaInvoke"
                ),
            },
            role=custom_resource_role,
        )
