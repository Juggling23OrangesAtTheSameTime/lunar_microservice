<html>
    <head>
        <title> Home Page </title>
        <link rel="stylesheet" href="css/styles.css">
    </head>
<body>
    <div id="body">
    <button id="moon_info"> Click here to see information about tonight's moon! </button>
    </div>

    <script>
      

        const moon_info = document.getElementById("moon_info");
        moon_info.addEventListener("click", function () {
            fetch("start_lunar.php")
            .then(response => response.json())
            .then(data => {
            if (data.error) {
                alert("Error: " + data.error);
            } else {
                const msg = `
Date: ${data.date}
Illumination: ${data.illumination_percent}%
Phase: ${data.phase}
Next Full Moon: ${data.next_full_moon}
Next New Moon: ${data.next_new_moon}
                `;
                alert(msg);
            }
        })
        .catch(err => {
            alert("Error fetching moon data");
            console.error(err);
        });
});
    </script>


</body>
</html>