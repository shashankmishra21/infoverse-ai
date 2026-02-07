import dotenv from "dotenv";
dotenv.config();

import app from "./app";
import { env } from "./config/env";

const PORT = env.PORT || 4000;

app.listen(PORT, () => {
  console.log(`Server is running on Port ${PORT}`);
});