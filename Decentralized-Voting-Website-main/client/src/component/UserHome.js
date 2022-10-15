import React from "react";

function UserHome(props) {
  return (
    <div>
      <div className="container-main">
        <div className="container-list title">
          <h1>{props.el.electionTitle}</h1>
          <br />
          <center>{props.el.organizationTitle}</center>
          <table style={{ marginTop: "21px" }}>
            <tr>
              <th>Admin name :</th>
              <td style={{ textTransform: "none" }}>{props.el.adminName}</td>
            </tr>
            <tr>
              <th>Contact :</th>
              <td style={{ textTransform: "none" }}>{props.el.adminEmail}</td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  );
}

export default UserHome;
