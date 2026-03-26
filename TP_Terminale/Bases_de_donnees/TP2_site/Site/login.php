<?php
// on teste si les variables sont définies
if (isset($_POST['login']) && isset($_POST['pwd'])) {
	try
	{
		require('acces_base.php');
		$conn = new PDO ($dsn, $username, $password);
		if($conn)
		{
			$sql = 'SELECT nom, mot_de_passe from logs WHERE nom=$_POST["login"] and mot_de_passe=$_POST["pwd"];';
			$results = $conn->prepare($sql);
			$results->execute();
			$res = $results->fetch();
			var_dump($res);

/* Commentaire pour Monsieur DE CECCO : j'ai tester toutes les variable grâce à var_dump. les données récupérées
du formulaires sont bien jean 123. Je ne sais donc pas ou est le problème...*/

			if($res == NULL)
			{  
				echo '<meta http-equiv="refresh" content="0;URL=index.htm">';
				header ('location: non.php');
			} 
			else
			{
				// on redirige l'utilisateur vers la page 2.
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
