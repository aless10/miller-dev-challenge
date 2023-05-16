import { useState, useContext, useEffect } from "react";
import { Typography } from "@material-tailwind/react";
import { getAvailableCars } from "../lib/requests";
import { TokenContext } from "../Context";
import { CarItem, Car } from "./CarItem";

const TABLE_HEAD = [
  "License Plate",
  "Owner",
  "Daily Price",
  "Pick up",
  "Put down",
  "Action",
];

export default function Home() {
  const { token } = useContext(TokenContext);
  const [availableCars, setAvailableCars] = useState<Car[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await getAvailableCars(token);
      if (response.details !== undefined) return;
      setAvailableCars(response);
    };

    fetchData().catch(console.error);
  }, []);

  return (
    <>
      <div className="mx-auto max-w-screen-md py-12">
        <Typography variant="h2" color="blue-gray" className="mb-2">
          Available Cars
        </Typography>
        <table className="w-full min-w-max table-auto text-left">
          <thead>
            <tr>
              {TABLE_HEAD.map((head) => (
                <th
                  key={head}
                  className="border-b border-blue-gray-100 bg-blue-gray-50 p-4"
                >
                  <Typography
                    variant="small"
                    color="blue-gray"
                    className="font-normal leading-none opacity-70"
                  >
                    {head}
                  </Typography>
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {availableCars.map((car, index) => {
              const isLast = index === availableCars.length - 1;
              const classes = isLast
                ? "p-4"
                : "p-4 border-b border-blue-gray-50";
              return <CarItem key={car.id} car={car} classes={classes} />;
            })}
          </tbody>
        </table>
      </div>
    </>
  );
}
