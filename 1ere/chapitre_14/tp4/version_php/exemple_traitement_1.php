<?php

if (isset($_POST["nom"])) {
    echo("Paramètre \"nom\" bien reçu : " . $_POST["nom"]);
} elseif (isset($_GET["nom"])) {
    echo("Le paramètre \"nom\" (" . $_GET["nom"] . ") doit être envoyé selon la méthode POST.");
} else {
    echo("En attente du paramètre \"nom\".");
}