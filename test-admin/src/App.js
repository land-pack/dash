import React from "react";
// import { Admin, Resource, ListGuesser } from "react-admin";
import jsonServerProvider from "ra-data-json-server";
import { Admin, Resource } from "react-admin";
import { UserList, UserEdit, UserPost } from "./users";
import Dashboard from "./Dashboard";
import authProvider from "./authProvider";

import PostIcon from "@material-ui/icons/Book";
import UserIcon from "@material-ui/icons/Group";
// import { PostList, PostEdit, PostCreate } from "./posts";

// const dataProvider = jsonServerProvider("http://jsonplaceholder.typicode.com");
const dataProvider = jsonServerProvider("http://localhost:19001");
const App = () => (
  <Admin
    dataProvider={dataProvider}
    dashboard={Dashboard}
    authProvider={authProvider}
  >
    <Resource
      name="users"
      list={UserList}
      edit={UserEdit}
      create={UserPost}
      icon={UserIcon}
    />
  </Admin>
);
export default App;
