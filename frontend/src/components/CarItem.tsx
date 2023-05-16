import { Typography } from "@material-tailwind/react";

export type Car = {
  id: string;
  license_plate: string;
  owner: string;
  daily_price: number;
  pick_up_place: string;
  put_down_place: string;
};

type Props = {
  car: Car;
  classes: string;
};

export function CarItem({ car, classes }: Props) {
  return (
    <>
      <tr key={car.id}>
        <td className={classes}>
          <Typography variant="small" color="blue-gray" className="font-normal">
            {car.license_plate}
          </Typography>
        </td>
        <td className={classes}>
          <Typography variant="small" color="blue-gray" className="font-normal">
            {car.owner}
          </Typography>
        </td>
        <td className={classes}>
          <Typography variant="small" color="blue-gray" className="font-normal">
            {car.daily_price}
          </Typography>
        </td>
        <td className={classes}>
          <Typography variant="small" color="blue-gray" className="font-normal">
            {car.pick_up_place}
          </Typography>
        </td>
        <td className={classes}>
          <Typography variant="small" color="blue-gray" className="font-normal">
            {car.put_down_place}
          </Typography>
        </td>
        <td className={classes}>
          <Typography
            as="a"
            href="#"
            variant="small"
            color="blue"
            className="font-medium"
          >
            Request
          </Typography>
        </td>
      </tr>
    </>
  );
}
