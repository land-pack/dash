import React from "react";
import {
  Create,
  Edit,
  SimpleForm,
  DisabledInput,
  TextInput,
  DateInput,
  LongTextInput,
  ReferenceManyField,
  Datagrid,
  TextField,
  DateField,
  EditButton,
  List,
  DateTimeInput,
  ImageInput,
  ImageField,
  Show,
  SimpleShowLayout,
  RichTextField
  //   Typography
} from "react-admin";
import RichTextInput from "ra-input-rich-text";
import ShoppingList from "./common/field";
import { connect } from "react-redux";

const required = (message = "Required") => value =>
  value ? undefined : message;

const PostTitle = ({ record }) => {
  return <span>Post {record ? `"${record.title}"` : ""}</span>;
};

export const CourseList = props => (
  <List {...props}>
    <Datagrid>
      <ShoppingList source="id" defaultValue="xxxx" label="IDs" />
      <TextField source="title" />
      <EditButton />
    </Datagrid>
  </List>
);

export const CourseCreate = props => (
  <Create {...props}>
    <SimpleForm>
      <ShoppingList source="xxx" defaultValue="xxxx" name="xxxx" />
      <TextInput source="title" defaultValue="Hello World" />
      <TextInput source="trainer" defaultValue="Frank AK" />
      <TextInput source="course_fee" defaultValue="$ 279.0" />
      <DateTimeInput source="Schedule" defaultValue={new Date()} />
      <ImageInput source="pictures" label="Related pictures" accept="image/*">
        <ImageField source="src" title="title" />
      </ImageInput>
      <RichTextInput
        source="Objections"
        defaultValue="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. "
      />
      <DateInput
        label="Publication date"
        source="published_at"
        defaultValue={new Date()}
      />
    </SimpleForm>
  </Create>
);

export const CourseShow = props => (
  <Show {...props}>
    <SimpleShowLayout>
      <ShoppingList source="xxx" defaultValue="xxxx" />
      <TextField source="title" />
      <TextField source="trainer" />
      <TextField source="course_fee" />
      <RichTextField source="Objections" />
    </SimpleShowLayout>
  </Show>
);

// const Aside = () => (
//   <div style={{ width: 200, margin: "1em" }}>
//     <Typography variant="title">Post details</Typography>
//     <Typography variant="body1">
//       Posts will only be published one an editor approves them
//     </Typography>
//   </div>
// );

export const CourseEdit = props => (
  // aside={<Aside />}
  <Edit title={<PostTitle />} {...props}>
    <SimpleForm>
      <DisabledInput label="Id" source="id" />
      <TextInput source="course_fee" validate={required()} />
      <RichTextInput source="Objections" validate={required()} />
    </SimpleForm>
  </Edit>
);
