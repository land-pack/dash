import React from "react";
// import { Admin, Resource, ListGuesser } from "react-admin";
import jsonServerProvider from "ra-data-json-server";
import { Admin, Resource } from "react-admin";
import { UserList, UserEdit, UserPost } from "./users";
// import { PostList, PostEdit, PostCreate } from "./posts";

// const dataProvider = jsonServerProvider("http://jsonplaceholder.typicode.com");
const dataProvider = jsonServerProvider("http://localhost:19001");
const App = () => (
  <Admin dataProvider={dataProvider}>
    <Resource name="users" list={UserList} edit={UserEdit} create={UserPost} />
  </Admin>
);
export default App;
