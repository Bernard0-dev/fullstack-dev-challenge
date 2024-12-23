import {  gql } from '@apollo/client';

export const LIST_SHOES = gql`
  query ListShoes($brand: String) {
    listShoes(brand: $brand) {
      id
      brand
      sizes
      price
    }
  }
`;