<?php
$python = "C:\\Python313\\python.exe"; # set this to your python.exe file location
$serverScript = "C:\\xampp\\htdocs\\CS 361 Main Program\\lunar_microservice\\server.py"; # set this to your server.py file location
$host = "127.0.0.1";
$port = 5000;

$fp = false;
$maxRetries = 5;
for ($i = 0; $i < $maxRetries; $i++) {
    $fp = @fsockopen($host, $port, $errno, $errstr, 3);
    if ($fp) break; 
    sleep(1);      
}

if (!$fp) {
    echo json_encode(["error" => "Could not connect to the lunar microservice"]);
    exit();
}

$request = '{"command":"moon_info","params":{}}' . "\n";
fwrite($fp, $request);

$response = '';
stream_set_timeout($fp, 3); 
while (!feof($fp)) {
    $line = fgets($fp);
    if ($line === false) break;
    $response .= $line;
}
fclose($fp);

header('Content-Type: application/json');
echo $response;
?>