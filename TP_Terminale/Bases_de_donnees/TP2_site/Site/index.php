<!DOCTYPE html>
<!-- index.php -->
<HTML lang="fr">
	<HEAD>
		<TITLE>SITE EN PHP</TITLE>
		<meta charset="UTF-8">
		<link rel="stylesheet" type="text/css" href="./static/css/index.css">
	</HEAD>
	<h1>CONNEXION</h1>
	<body background="./static/images/fond1.jpg">
		<?php require('tete.php'); ?>
		
		<form action="login.php" method="POST">
			<input name="login" class="login" placeholder="votre login ici" required></input>
			<input name="pwd" class="pwd" placeholder="votre mot de passe ici" required></input>
			<button class="btnS">OK</button>
		</form>

		<a href="/creer_compte.php"><label class="compte">Je n'ai pas de compte : Creer un compte</label></a>


		<?php require('pied.php'); ?>
	</body>
</html>


