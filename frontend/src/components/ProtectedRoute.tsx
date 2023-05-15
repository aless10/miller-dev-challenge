// @ts-ignore
import React, { Component, useContext } from 'react'
// @ts-ignore
import { Route, Navigate, Outlet } from 'react-router-dom'
import { AuthContext } from '../Context';

type Props = {
  children: JSX.Element
}


const ProtectedRoute = () => {
  const { auth } = useContext(AuthContext)
  if (!auth) {
    return <Navigate to="/login" replace />;
  }
  return <Outlet></Outlet>
};

export default ProtectedRoute
