<?php
// on teste si les variables sont définies
if (isset($_POST["login"]) && isset($_POST["pwd1"]) && isset($_POST["pwd2"])) {
	try
	{
		require('acces_base.php');
		$conn = new PDO($dsn, $username, $password);
		if($conn)
		{
			$sql = 'SELECT nom from logs;';
			$results = $conn->prepare($sql);
			$results->execute();
			$res = $results->fetch();
			foreach($res as $r)
			{
				$nom = $r['nom'];
			}
			if($_POST['login'] == $nom)
			{  
				echo '<meta http-equiv="refresh" content="0;URL=index.htm">';
				header ('location: non.php');
			} 
			else
			{
				// on redirige l'utilisateur vers la page 2.
                $sql = 'INSERT INTO logs (nom, mot_de_passe) VALUES ($_POST["login"], $_POST["pwd1"])';
				$results = $conn->prepare($sql);
				$results->execute();
				session_start();
				$_SESSION["id"] = session_id();
				header ('location: oui.php');
			}
		}
	}
	catch (PDOException $e)
	{
		echo $e->getMessage();
	}
}

else {

	echo 'Les variables du formulaire ne sont pas déclarées.';
}
?>
