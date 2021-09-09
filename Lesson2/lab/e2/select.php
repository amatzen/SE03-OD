 <?php
include("config.php");

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT *  FROM abooktable";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    echo "<center><table width=\"50%\" border=\"1\">";
    while($row = $result->fetch_assoc()) {
	    echo "<tr><td>" . $row['name'] . "</td><td>". $row['address']."</td></tr>";
    }
    echo "</table></center>";
} else {
    echo "0 results";
}
$conn->close();
?> 

