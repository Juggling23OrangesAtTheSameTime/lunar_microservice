import net from "net";

const request = {
    command: "moon_info" 
};

const client = new net.Socket();

client.connect(5000, "127.0.0.1", () => {
    console.log("Connected to microservice");
    client.write(JSON.stringify(request));  //request is sent to the microservice via the python socket as JSON data
});

client.on("data", (data) => {  // 
    console.log("Response from server:");
    console.log(data.toString());
    client.end(); 
});

client.on("error", (err) => {              // catches any errors when running the microservice
    console.error("Client error:", err.message);
});
