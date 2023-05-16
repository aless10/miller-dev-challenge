// @ts-ignore
import React from "react";
import { AuthContext, TokenContext } from "../Context";
import Cookies from "js-cookie";

import {
  Navbar,
  Typography,
  Popover,
  PopoverHandler,
  PopoverContent,
  Button,
  IconButton,
} from "@material-tailwind/react";

type Props = {
  text: string;
};

function AlertButton({ text }: Props) {
  return (
    <Popover>
      <PopoverHandler>
        <Typography
          as="li"
          style={{ cursor: "pointer" }}
          variant="small"
          color="blue-gray"
          className="p-1 font-normal"
        >
          {text}
        </Typography>
      </PopoverHandler>
      <PopoverContent>
        This is doing nothing at the moment. Sorry!
      </PopoverContent>
    </Popover>
  );
}

export default function Header() {
  const [openNav, setOpenNav] = React.useState(false);

  const { setAuth } = React.useContext(AuthContext);
  const { setToken } = React.useContext(TokenContext);
  const handleLogout = () => {
    setAuth(false);
    setToken("");
    Cookies.remove("access_token");
  };

  React.useEffect(() => {
    window.addEventListener(
      "resize",
      () => window.innerWidth >= 960 && setOpenNav(false)
    );
  }, []);

  const navList = (
    <ul className="mb-4 mt-2 flex flex-col gap-2 lg:mb-0 lg:mt-0 lg:flex-row lg:items-center lg:gap-6">
      <AlertButton text={"My Cars"} />
      <AlertButton text={"My Requests"} />
    </ul>
  );

  return (
    <>
      <Navbar className="sticky text-black inset-0 z-10 h-max max-w-full rounded-none py-2 px-4 lg:px-8 lg:py-4">
        <div className="flex items-center justify-between text-blue-gray-900">
          <Typography
            as="a"
            href="#"
            className="mr-4 cursor-pointer py-1.5 font-medium"
          >
            <img
              className="mx-auto h-10 w-auto"
              src="https://millergroup.it/wp-content/uploads/2022/05/MILLER_logo-clear.svg"
              alt="Your Company"
            />
          </Typography>
          <div className="flex items-center gap-4">
            <div className="mr-4  lg:block">{navList}</div>
            <Button
              variant="gradient"
              size="sm"
              onClick={handleLogout}
              className="hidden text-black lg:inline-block"
              style={{ backgroundColor: "#11a4da" }}
            >
              <span>Logout</span>
            </Button>
            <IconButton
              variant="text"
              className="ml-auto h-6 w-6 hover:bg-transparent focus:bg-transparent active:bg-transparent lg:hidden"
              ripple={false}
              onClick={() => setOpenNav(!openNav)}
            >
              {openNav ? (
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  className="h-6 w-6"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  strokeWidth={2}
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    d="M6 18L18 6M6 6l12 12"
                  />
                </svg>
              ) : (
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-6 w-6"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth={2}
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    d="M4 6h16M4 12h16M4 18h16"
                  />
                </svg>
              )}
            </IconButton>
          </div>
        </div>
      </Navbar>
    </>
  );
}
