import { ApolloProvider } from '@apollo/client';
import client from './graphql/client';
import { ShoeList } from './ShoeList';

const App = () => (
  <ApolloProvider client={client}>
    <ShoeList />
  </ApolloProvider>
);

export default App;