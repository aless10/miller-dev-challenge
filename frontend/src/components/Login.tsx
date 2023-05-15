import { FormEvent, useContext, useState } from "react"
import { Navigate } from 'react-router-dom'
import { AuthContext, TokenContext } from "../Context"
import { login } from '../lib/requests'
import Cookies from "js-cookie"


function Login() {

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const { token, setToken } = useContext(TokenContext)
  const { auth, setAuth } = useContext(AuthContext)

  const handleSubmit = async (username: string, password: string, e: FormEvent) => {
    e.preventDefault()
    const response = await login(username, password)
    console.log(response)
    setAuth(true)
    Cookies.set("access_token", response.access_token);
    setToken(response.access_token)
  }

  if (auth) {
    return <Navigate to={"/"}/>
  }
  return (
    <div className="container center">
      <form className="col s8 offset-s2" method="post" onSubmit={e => handleSubmit(username, password, e)}>
        <div className='row'>
          <div className='input-field col s8 offset-s2'>
            <input className='validate' type='text' name='username' id='username'
                   onChange={(e) => setUsername(e.target.value)}/>
            <label htmlFor='username'>Enter your name</label>
          </div>
        </div>

        <div className='row'>
          <div className='input-field col s8 offset-s2'>
            <input className='validate' type='password' name='password' id='password'
                   onChange={(e) => setPassword(e.target.value)}/>
            <label htmlFor='password'>Enter your password</label>
          </div>
        </div>
        <br/>
        <div className='row'>
          <button type='submit' className='col s8 offset-s2 btn btn-large waves-effect indigo'>Login
          </button>
        </div>
      </form>
    </div>
  )
}

export default Login
