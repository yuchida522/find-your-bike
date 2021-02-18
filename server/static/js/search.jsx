
const { InstantSearch, SearchBox, Hits } = ReactInstantSearchDOM;

const searchClient = algoliasearch('WLGD92S6H5', 'b6a74de09f93e62f736558f7ef67f80f');

const App = () => (
  <InstantSearch searchClient={searchClient} indexName="testing">
    <SearchBox />
    <Hits />
  </InstantSearch>
);
