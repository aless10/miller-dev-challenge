// @ts-ignore
import React from 'react'
// @ts-ignore
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom'
import './App.css'
// @ts-ignore
import StickyFooter from './components/Footer'
import { AuthContext, TokenContext } from './Context';
import Header from './components/Header'
import ProtectedRoute from './components/ProtectedRoute'
import Cookies from "js-cookie";
import Login from './components/Login';

const Home = () => {
  return(
      <h1>home</h1>
  )
}

const Profile = () => {
  return(
      <h1>Profile</h1>
  )
}

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
            <Header/>
            <Routes>
                <Route element={<ProtectedRoute />}>
                  <Route path="" element={<Home />} />
                  <Route path="profile" element={<Profile />} />
                </Route>
              <Route path='/login' element={<Login />}/>
            </Routes>
          </main>
          <StickyFooter/>
        </Router>
        </TokenContext.Provider>
      </AuthContext.Provider>
  )
}

export default App