<?php

if (isset($_POST["nom"])) {
    $message = "Paramètre <strong>nom</strong> bien reçu : " . $_POST["nom"] . ".";
} elseif (isset($_GET["nom"])) {
    $message = "Le paramètre <strong>nom</strong> (" . $_GET["nom"] . ") doit être envoyé selon la méthode <code>POST</code>.";
} else {
    $message = "En attente du paramètre <strong>nom</strong>.";
}

?>
<!doctype html>

<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>Titre de votre page</title>
</head>

<body>
<h1>Réponse</h1>
<p>La force de PHP est de pouvoir associer facilement du code PHP et du code HTML.</p>
<p><?php echo($message) ?></p>
</body>
</html>