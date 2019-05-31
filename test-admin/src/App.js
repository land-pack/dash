import React from "react";
// import { Admin, Resource, ListGuesser } from "react-admin";
import jsonServerProvider from "ra-data-json-server";
import { Admin, Resource, Login } from "react-admin";
import { UserList, UserEdit, UserPost } from "./users";
import { CourseCreate, CourseEdit, CourseList } from "./course";
import Dashboard from "./Dashboard";
import authProvider from "./authProvider";

import PostIcon from "@material-ui/icons/Book";
import UserIcon from "@material-ui/icons/Group";
import AssistantIcon from "@material-ui/icons/Assistant";

const MyLoginPage = () => (
  <Login backgroundImage="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTsiKd1YOrLDrq7eI3XQitlsj-nJ6hi1dqZ76h0pCBt1QChYx_" />
);

// import { PostList, PostEdit, PostCreate } from "./posts";

// const dataProvider = jsonServerProvider("http://jsonplaceholder.typicode.com");
const dataProvider = jsonServerProvider("http://localhost:19001");
const App = () => (
  <Admin
    dataProvider={dataProvider}
    dashboard={Dashboard}
    authProvider={authProvider}
    // loginPage={MyLoginPage}
  >
    <Resource
      name="users"
      list={UserList}
      edit={UserEdit}
      create={UserPost}
      icon={UserIcon}
    />

    <Resource
      name="course"
      create={CourseCreate}
      edit={CourseEdit}
      list={CourseList}
      icon={AssistantIcon}
    />
  </Admin>
);
export default App;
