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
  DateTimeInput
} from "react-admin";
import RichTextInput from "ra-input-rich-text";

const required = (message = "Required") => value =>
  value ? undefined : message;

const PostTitle = ({ record }) => {
  return <span>Post {record ? `"${record.title}"` : ""}</span>;
};

export const CourseList = props => (
  <List {...props}>
    <Datagrid>
      <TextField source="id" />
      <TextField source="title" />
      <EditButton />
    </Datagrid>
  </List>
);

export const CourseCreate = props => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="title" defaultValue="Hello World" />
      <TextInput source="trainer" defaultValue="Frank AK" />
      <TextInput source="course_fee" defaultValue="$ 279.0" />
      <DateTimeInput source="Schedule" defaultValue={new Date()} />
      <TextInput source="teaser" options={{ multiLine: true }} />
      <RichTextInput source="Objections" />
      <DateInput
        label="Publication date"
        source="published_at"
        defaultValue={new Date()}
      />
    </SimpleForm>
  </Create>
);

export const CourseEdit = props => (
  <Edit title={<PostTitle />} {...props}>
    <SimpleForm>
      <DisabledInput label="Id" source="id" />
      <TextInput source="title" validate={required()} />
      <LongTextInput source="teaser" validate={required()} />
      <RichTextInput source="body" validate={required()} />
      <DateInput label="Publication date" source="published_at" />
      <ReferenceManyField
        label="Comments"
        reference="comments"
        target="post_id"
      >
        <Datagrid>
          <TextField source="body" />
          <DateField source="created_at" />
          <EditButton />
        </Datagrid>
      </ReferenceManyField>
    </SimpleForm>
  </Edit>
);
