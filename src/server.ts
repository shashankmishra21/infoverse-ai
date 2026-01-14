import { env } from "./config/env";
import app from "./app";
//import dotenv from "dotenv"


//dotenv.config()
const PORT = env.PORT || 4000;

app.listen( PORT , () => {
    console.log(`Server is running on Port ${PORT}`);
})