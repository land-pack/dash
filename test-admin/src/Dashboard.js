import React from "react";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import { Title, SelectField } from "react-admin";
import { DialogContent } from "@material-ui/core/DialogContent";
import { Dialog } from "@material-ui/core";

export default () => (
  <Card>
    <Title title="Welcome to the administration" />
    <CardContent>Can we drop the masquerade!</CardContent>
  </Card>
);
