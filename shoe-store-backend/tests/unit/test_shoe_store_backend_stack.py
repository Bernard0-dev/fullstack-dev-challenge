import aws_cdk.assertions as assertions
import pytest
from aws_cdk import App

from shoe_store_backend.shoe_store_backend_stack import ShoeStoreBackendStack


@pytest.fixture
def cdk_app():
    app = App()
    stack = ShoeStoreBackendStack(app, "ShoeStoreBackendStack")
    return stack


def test_shoes_table_created(cdk_app):
    template = assertions.Template.from_stack(cdk_app)
    template.has_resource_properties(
        "AWS::DynamoDB::Table",
        {
            "TableName": "Shoes",
            "BillingMode": "PAY_PER_REQUEST",
            "AttributeDefinitions": [{"AttributeName": "id", "AttributeType": "S"}],
            "KeySchema": [{"AttributeName": "id", "KeyType": "HASH"}],
        },
    )


def test_orders_table_created(cdk_app):
    template = assertions.Template.from_stack(cdk_app)
    template.has_resource_properties(
        "AWS::DynamoDB::Table",
        {
            "TableName": "Orders",
            "BillingMode": "PAY_PER_REQUEST",
            "AttributeDefinitions": [{"AttributeName": "id", "AttributeType": "S"}],
            "KeySchema": [{"AttributeName": "id", "KeyType": "HASH"}],
        },
    )


def test_appsync_api_created(cdk_app):
    template = assertions.Template.from_stack(cdk_app)
    template.has_resource_properties(
        "AWS::AppSync::GraphQLApi", {"Name": "ShoeStoreApi"}
    )


def test_shoes_data_source_created(cdk_app):
    template = assertions.Template.from_stack(cdk_app)
    template.resource_count_is("AWS::AppSync::DataSource", 2)


def test_initial_data_lambda_created(cdk_app):
    template = assertions.Template.from_stack(cdk_app)
    template.has_resource_properties(
        "AWS::Lambda::Function", {"Handler": "insert.handler", "Runtime": "python3.12"}
    )


def test_lambda_invocation_role(cdk_app):
    template = assertions.Template.from_stack(cdk_app)
    template.has_resource_properties(
        "AWS::IAM::Role",
        {
            "AssumeRolePolicyDocument": {
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {"Service": "lambda.amazonaws.com"},
                        "Action": "sts:AssumeRole",
                    }
                ]
            }
        },
    )
