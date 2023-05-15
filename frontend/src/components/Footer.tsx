import { Typography } from "@material-tailwind/react";

export default function Footer() {
  return (
    <footer className="w-full flex-row flex-wrap items-center justify-center gap-y-6 gap-x-12 border-t border-blue-gray-50 py-6 text-center md:justify-between">
      <Typography color="blue-gray" className="font-normal p-3">
        <span className="grey-text">
          Made with ❤️ by{" "}
          <a href="https://github.com/aless10">
            <strong>&lt;aless.io&gt;</strong>
          </a>
        </span>
      </Typography>
    </footer>
  );
}
