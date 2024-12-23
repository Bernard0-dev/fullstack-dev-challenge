import {  useState } from 'react';
import { useQuery, useMutation } from '@apollo/client';
import { LIST_SHOES } from './graphql/queries';
import { CREATE_ORDER } from './graphql/mutations';

export const ShoeList = () => {
  const [brand, setBrand] = useState('');
  const { loading, error, data } = useQuery(LIST_SHOES, { variables: { brand } });
  const [createOrder] = useMutation(CREATE_ORDER);

  const handleOrder = (shoeId: string) => {
    const shippingInfo = prompt('Enter shipping info:');
    if (shippingInfo) {
      createOrder({ variables: { client: 'random-client-id', shoeId, size: 'M', shippingInfo } });
      alert('Order created!');
    }
  };

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <div>
      <input type="text" value={brand} onChange={(e) => setBrand(e.target.value)} placeholder="Filter by brand" />
      <ul>
        {data.listShoes.map((shoe: any) => (
          <li key={shoe.id}>
            {shoe.brand} - ${shoe.price}
            <button onClick={() => handleOrder(shoe.id)}>Order</button>
          </li>
        ))}
      </ul>
    </div>
  );
};