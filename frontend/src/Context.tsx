import React from "react"

export type Token = {
  token: string
  setToken: (value: string) => void
}

export type Auth = {
  auth: boolean
  setAuth: (value: boolean) => void
}



export const AuthContext = React.createContext<Auth>(
  {
    auth: false, 
    setAuth: () => {}
  }
);
export const TokenContext = React.createContext<Token>(
  {
    token: "",
    setToken: () => {}
  }
);