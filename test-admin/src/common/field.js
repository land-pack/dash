import React from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";

const MyTextField = ({ source, record = {} }) => <span>{record[source]}</span>;

class ShoppingList extends React.Component {
  render() {
    const { rate } = this.props;
    return (
      <div className="shopping-list">
        <h1>Shopping List for {this.props.name}</h1>
        <ul>
          <li>Instagram</li>
          <li>WhatsApp</li>
          <li>{rate}</li>
        </ul>
      </div>
    );
  }
}

export default connect(
  null,
  {
    name: "xxxx",
    rate: 190
  }
)(ShoppingList);

// MyTextField.propTypes = {
//   label: PropTypes.string,
//   record: PropTypes.object,
//   source: PropTypes.string.isRequired
// };

// export default MyTextField;
