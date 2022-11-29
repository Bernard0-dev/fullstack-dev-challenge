# Full-stack web developer challenge

In this test, you'll write a small web application to manage a shoe store.

## Backend implementation

1. The backend should consist of two tables: Shoes and Orders.

   - The shoes should have at least a reference, brand, available sizes, and price.
   - The orders should have at least an order id, client, shoe reference, size, shipping information.

2. Implement at least 2 endpoints - one for getting a list of shoes that can be filtered by brand, and one for creating orders. Initial data in the DynamoDB tables can be hardcoded.
3. In the endpoint for creating an order, generate an invoice file (a JSON with the fields of the order and the shoe is enough) and push it to an S3 bucket.
4. The implementation should be completely serverless, use AWS API Gateway, Lambda and DynamoDB services. Please provide CloudFormation template or CDK script to provision the infrastructure and run the code.
5. You can ignore the user authentication and use randomly generated and hardcoded user ids.

## Frontend implementation

Implement a small frontend application to consume the API you developed above.

1. Display the list of shoes and allow to filter them by brand (from the
   backend).
2. Split the order creation into two steps:

   - the first step must allow choosing the shoe reference or references
   - the second step must require the shipping information

3. Implement a global state to store the data.
4. Deploy and host the application from an S3 bucket

## Requirements

- Use Python 3.8+
- Use Typescript
- Include instructions for how to deploy and run the code
- Include the link from which the application can be accessed
