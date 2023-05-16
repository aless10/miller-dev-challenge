import { ListItem, ListItemSuffix, IconButton } from "@material-tailwind/react";
import { TrashIcon } from "@heroicons/react/24/solid";

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
};

export default function CarItem({ car }: Props) {
  return (
    <>
      <ListItem ripple={false} className="py-1 pr-1 pl-4">
        {car.license_plate}
        <ListItemSuffix>
          <IconButton variant="text" color="blue-gray">
            <TrashIcon className="h-5 w-5" />
          </IconButton>
        </ListItemSuffix>
      </ListItem>
    </>
  );
}
