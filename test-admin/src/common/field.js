import React from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";

const MyTextField = ({ source, record = {} }) => <span>{record[source]}</span>;

/*
 Build my own Component 
 Just wri
*/
class ShoppingList extends React.Component {
  render() {
    const { rate, record } = this.props;
    console.log(this.props);
    return (
      <div className="shopping-list">
        <h1>Shopping List for {this.props.name}</h1>
        <ul>
          <li> {record.id}</li>
          <li>
            <img src="https://ui-avatars.com/api/?background=0D8ABC&color=fff" />
          </li>
          <li>WhatsApp</li>
          <li>{rate}</li>
        </ul>
      </div>
    );
  }
}

const mapStateToProps = function(state) {
  return {
    rate: state.rate
  };
};
export default connect(
  null,
  {}
)(ShoppingList);

// MyTextField.propTypes = {
//   label: PropTypes.string,
//   record: PropTypes.object,
//   source: PropTypes.string.isRequired
// };

// export default MyTextField;
