<!DOCTYPE html>
<!-- oui.php -->
<HTML lang="fr">
	<HEAD>
		<TITLE>SITE EN PHP</TITLE>
		<meta charset="UTF-8">
		<link rel="stylesheet" type="text/css" href="./static/css/index.css">
	</HEAD>
	<?php
		session_start();
		if(session_id() != $_SESSION["id"]) {
			header ('location: index.php');
		}
	?>
	<h1>BRAVO</h1>
	<body background="./static/images/fond2.png">
		<?php require('tete.php'); ?>
		
        <label class="lab">CONNEXION REUSSIE</label>
		<button class="deconn" onclick="logout()">Deconnexion</button>

		<?php require('pied.php'); ?>
		<script src="./static/js/index.js"></script>
	</body>
</html>


