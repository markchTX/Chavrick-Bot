
import { Connection } from "@solana/web3.js";
import dotenv from "dotenv";
dotenv.config();

const WSS_ENDPOINT = process.env.WSS_ENDPOINT;
const connection = new Connection(WSS_ENDPOINT);

console.log("Connecting to Solana WebSocket...");

connection.onLogs("all", (log) => {
    console.log("New log:", log);
});
