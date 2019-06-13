import React from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";

/*
 Build my own Component 
 Just wri
*/
class BlogInput extends React.Component {
  render() {
    const { rate, record } = this.props;
    console.log(this.props);
    return (
      <div>
        <h1>BlogInput List for {this.props.name}</h1>
        <ul>
          <li> {record.id}</li>
          <li>Instagram</li>
          <li>Wechat</li>
          <li>ss</li>
          <li>
            <button>sss</button>
          </li>
          <li>{rate}</li>
        </ul>
      </div>
    );
  }
}

export default connect(
  null,
  {}
)(BlogInput);
