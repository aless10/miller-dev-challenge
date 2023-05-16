// @ts-ignore
import { useContext } from "react";
import { Navigate, Outlet } from "react-router-dom";
import { AuthContext } from "../Context";

const ProtectedRoute = () => {
  const { auth } = useContext(AuthContext);
  if (!auth) {
    return <Navigate to="/login" replace />;
  }
  return <Outlet></Outlet>;
};

export default ProtectedRoute;
