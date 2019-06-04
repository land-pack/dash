import React from "react";
import { render } from "react-dom";
import { simpleRestClient, Admin, Resource } from "admin-on-rest";
import jsonServerProvider from "ra-data-json-server";
import { UserList, UserEdit, UserPost } from "./users";
import { PostCreate, PostList, PostEdit, PostIcon } from "./ps";

// const dataProvider = jsonServerProvider("http://jsonplaceholder.typicode.com");
const dataProvider = jsonServerProvider("http://localhost:19001");
// restClient={simpleRestClient("http://localhost:19001")}
const App = () => (
  <Admin dataProvider={dataProvider}>
    <Resource
      name="posts"
      list={PostList}
      edit={PostEdit}
      create={PostCreate}
      icon={PostIcon}
    />
    />
  </Admin>
  //   document.getElementById("root")
);
export default App;
