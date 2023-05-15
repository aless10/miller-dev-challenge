// @ts-ignore
import React from "react"
import { AuthContext, TokenContext } from '../Context';
import Cookies from "js-cookie"

function Header() {
  const { auth, setAuth } = React.useContext(AuthContext);
  const { setToken } = React.useContext(TokenContext);
  const handleLogout = () => {
      setAuth(false);
      setToken('');
      Cookies.remove("access_token");
  }
  
  return (
    <div className="navbar-fixed">
      <nav className="white">
        <div className="nav-wrapper">
          <a href="#" className="brand-logo"><img style={{width: "15%", marginLeft: "-810px"}} src="logo.png"/></a>
          {auth && <button onClick={handleLogout}>Logout</button>}
        </div>
      </nav>
    </div>
  );
}

export default Header
