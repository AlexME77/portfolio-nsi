
<?php
	try
	{
		require('acces_base.php');
		$conn = new PDO($dsn);
		if($conn)
		{
			$sql = 'SELECT ;';
			$results = $conn->prepare($sql);
			$results->execute();
			$res = $results->fetchOne();
			foreach($res as $r)
			{
				$pw = $r['mot_passe'];
			}
			if(empty($pw))
			{  
				echo '<script type="text/javascript">alert("Erreur : login et/ou mot de passe inconnu");</script>';
			} 
			else
			{
				........................................... ??
			}
		}
	}
	catch (PDOException $e)
	{
		echo $e->getMessage();
	}
?>
