<?php
include("config.php");
	
if(isset($_POST['name']) && isset($_POST['address'])){
	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);
	
	// Check connection
	if ($conn->connect_error) {
	    die("Connection failed: " . $conn->connect_error);
	}
	
	// prepare and bind
	$stmt = $conn->prepare("INSERT INTO abooktable (name, address) VALUES (?, ?)");
	$stmt->bind_param("ss", $name, $address);
	
	$name = $_POST['name'];
	$address = $_POST['address'];
	$stmt->execute();
	
	$stmt->close();
	$conn->close();

	echo "Inserted: $name";
}
?>

<h2>Address book submission form</h2>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
  Name: <input type="text" name="name" value=""><br><br>
  Address: <input type="text" name="address" value=""><br><br>
  <input type="submit" name="submit" value="Submit">
</form>


<br>
<a href="/select.php">click to see addressbook</a>

