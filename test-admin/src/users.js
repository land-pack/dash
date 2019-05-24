// in src/users.js
import React from "react";
import {
  List,
  Datagrid,
  TextField,
  SimpleForm,
  Edit,
  Create,
  DisabledInput,
  TextInput,
  LongTextInput,
  EmailField,
  UrlField
} from "react-admin";

import MyUrlField from "./MyUrlField";

export const UserList = props => (
  <List {...props}>
    <Datagrid rowClick="edit">
      <TextField source="id" />
      <TextField source="name" />
      {/* <TextField source="username" /> */}
      <EmailField source="email" />
      {/* <TextField source="address.street" /> */}
      <TextField source="phone" />
      <MyUrlField source="website" />
      <TextField source="company.name" />
    </Datagrid>
  </List>
);

const UserTitle = ({ record }) => {
  return <span>User {record ? `"${record.name}"` : ""}</span>;
};

export const UserEdit = props => (
  <Edit title={<UserTitle />} {...props}>
    <SimpleForm>
      <DisabledInput source="id" />
      <TextInput source="phone" />
      <LongTextInput source="website" />
    </SimpleForm>
  </Edit>
);

export const UserPost = pros => (
  <Create {...pros}>
    <SimpleForm>
      <TextInput source="name" defaultValue="frank" />
      <TextInput source="username" defaultValue="frank ak" />
      <TextInput source="address.street" defaultValue="HongKong ..518" />
      <TextInput source="email" defaultValue="klook@gmail.com" />
      <TextInput source="phone" defaultValue="123456" />
      <TextInput source="website" defaultValue="klook.com" />
      <TextInput source="company.name" defaultValue="klook" />
    </SimpleForm>
  </Create>
);
