import React from "react";
// import { Admin, Resource, ListGuesser } from "react-admin";
import jsonServerProvider from "ra-data-json-server";
import { Admin, Resource, Login } from "react-admin";
import { UserList, UserEdit, UserPost } from "./users";
import { myTheme } from "./theme";
import { CourseCreate, CourseEdit, CourseList, CourseShow } from "./course";
import Dashboard from "./Dashboard";
import authProvider from "./authProvider";
import Menu from "./Menu";

import blogHome, { blogshow, bloglist, blogedit } from "./blogHome";

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
    // appLayout={MyLayout}
    theme={myTheme}
    dataProvider={dataProvider}
    dashboard={Dashboard}
    authProvider={authProvider}
    title="Admin Center"
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
      show={CourseShow}
      icon={AssistantIcon}
    />

    <Resource name="blogHome" show={blogshow} list={bloglist} edit={blogedit} />
  </Admin>
);
export default App;
