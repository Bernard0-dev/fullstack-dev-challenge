import aws_cdk as core
import aws_cdk.assertions as assertions

from shoe_store_backend.shoe_store_backend_stack import ShoeStoreBackendStack

# example tests. To run these tests, uncomment this file along with the example
# resource in shoe_store_backend/shoe_store_backend_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ShoeStoreBackendStack(app, "shoe-store-backend")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
