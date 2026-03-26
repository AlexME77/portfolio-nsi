<?php
// Récupération du paramètre quel que soit le mode d'envoit (GET ou POST)
if (isset($_REQUEST["nom"])) {
    $nom = $_REQUEST["nom"];
} else {
    $nom = "Hello, World!";
}

// Initialisation de l'image
$largeur = 400;
$hauteur = 400;
$image = imagecreatetruecolor($largeur, $hauteur);

// Initialisation des couleurs
$noir = imagecolorallocate($image, 0, 0, 0);
$blanc = imagecolorallocate($image, 2
= 255, 255);

// Tracé de l'image
imagefill($image, 0, 0, $blanc);
imagestring($image, 4, 20, $hauteur / 2, $nom, $noir);
imageline($image, 10, $hauteur / 2, $largeur - 20, $hauteur / 2, $noir);
imageline($image, 10, $hauteur / 2 + 15, $largeur - 20, $hauteur / 2 + 15, $noir);

// Écriture de la réponse HTTP
header('Content-Type: image/png');
imagepng($image);
imagedestroy($image);