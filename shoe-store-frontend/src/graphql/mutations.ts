import {  gql } from '@apollo/client';

export const CREATE_ORDER = gql`
  mutation CreateOrder($client: String!, $shoeId: String!, $size: String!, $shippingInfo: String!) {
    createOrder(client: $client, shoeId: $shoeId, size: $size, shippingInfo: $shippingInfo) {
      orderId
      client
    }
  }
`;