<!DOCTYPE html>
<!-- index.php -->
<HTML lang="fr">
	<HEAD>
		<TITLE>SITE EN PHP</TITLE>
		<meta charset="UTF-8">
		<link rel="stylesheet" type="text/css" href="./static/css/index.css">
	</HEAD>
	
	<h1>Creer un compte</h1>
	<body background="./static/images/fond1.jpg">
		<?php require('tete.php'); ?>
		
		<form action="signup.php" method="POST">
			<input name="login" class="login1" placeholder="votre login ici" required></input>
			<input name="pwd1" class="pwd1" placeholder="votre mot de passe ici" required></input>
			<input name="pwd2" class="pwd2" placeholder="confirmer le mot de passe" required></input>
			<button class="btnS">OK</button>
		</form>

		<a href="/"><label class="compte">Deja un compte : Me connecter</label></a>


		<?php require('pied.php'); ?>
	</body>
</html>


