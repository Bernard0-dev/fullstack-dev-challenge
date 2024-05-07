# Full-stack web developer challenge

In this test, you'll write a small web application to manage a shoe store.

## Backend implementation

1. The backend should consist of two tables: Shoes and Orders.

   - The shoes should have at least an id, brand, available sizes, and price.
   - The orders should have at least an order id, client, shoe reference, size and shipping information.

2. Implement at least one GQL query to get a list of shoes that can be filtered by brand and one GQL mutation to create orders. Initial data in the DynamoDB tables can be hardcoded.
3. When creating an order, generate an invoice file (a JSON with the order fields and the shoe is enough) and push it to an S3 bucket.
4. The implementation should be completely serverless, using AWS AppSync, Lambda and DynamoDB services. Please provide a CloudFormation template or CDK script to provision the infrastructure and run the code.
5. You can ignore the user authentication and use randomly generated and hardcoded user ids.

## Frontend implementation

Implement a small React app to consume the GQL API you developed.

1. Display the list of shoes and allow to filter them by brand (from the backend).
2. Select shoes from the list to create an order, make sure to require the shipping information.
4. Implement a global state to store the data.
5. Deploy and host the application from an S3 bucket.

## Requirements

- Use Python 3.9+
- Use AWS services: AWS AppSync, Lambda, DynamoDB
- Use Typescript
- Use React
- Include instructions on how to deploy and run the code
- Include the link from which the application can be accessed
