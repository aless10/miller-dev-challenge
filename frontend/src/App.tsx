import React from "react";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import "./App.css";
import Footer from "./components/Footer";
import { AuthContext, TokenContext } from "./Context";
import Header from "./components/Header";
import ProtectedRoute from "./components/ProtectedRoute";
import Cookies from "js-cookie";
import Login from "./components/Login";
import Signup from "./components/Signup";
import Home from "./components/Home";

const Profile = () => {
  return <h1>Profile</h1>;
};

function App() {
  const [auth, setAuth] = React.useState(false);
  const [token, setToken] = React.useState("");

  const readCookie = () => {
    let token = Cookies.get("access_token");
    if (token) {
      setAuth(true);
      setToken(token);
    }
  };
  React.useEffect(() => {
    readCookie();
  }, []);

  return (
    <AuthContext.Provider value={{ auth, setAuth }}>
      <TokenContext.Provider value={{ token, setToken }}>
        <Router>
          <main className="App">
            {auth && <Header />}
            <Routes>
              <Route element={<ProtectedRoute />}>
                <Route path="" element={<Home />} />
                <Route path="profile" element={<Profile />} />
              </Route>
              <Route path="/login" element={<Login />} />
              <Route path="/signup" element={<Signup />} />
            </Routes>
          </main>
          <Footer />
        </Router>
      </TokenContext.Provider>
    </AuthContext.Provider>
  );
}

export default App;
