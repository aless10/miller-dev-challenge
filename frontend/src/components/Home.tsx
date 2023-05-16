import { useState, useContext, useEffect } from "react";
import { Card, List, Typography } from "@material-tailwind/react";
import { getAvailableCars } from "../lib/requests";
import { TokenContext } from "../Context";
import CarItem, { Car } from "./CarItem";

export default function Home() {
  const { token } = useContext(TokenContext);
  const [availableCars, setAvailableCars] = useState<Car[]>([]);

  const loadAvailableCars = async () => {
    const response = await getAvailableCars(token);
    setAvailableCars(response);
  };

  useEffect(() => {
    const fetchData = async () => {
      await loadAvailableCars();
    };

    // call the function
    fetchData()
      // make sure to catch any error
      .catch(console.error);
  }, []);

  return (
    <>
      <div className="mx-auto max-w-screen-md py-12">
        <Typography variant="h2" color="blue-gray" className="mb-2">
          Available Cars
        </Typography>
        <Card className="w-96">
          <List>
            {availableCars.map((car) => (
              <CarItem key={car.license_plate} car={car} />
            ))}
          </List>
        </Card>
      </div>
    </>
  );
}
