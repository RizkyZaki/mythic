<?php

include_once '../controllers/MahasiswaController.php';
include_once '../config/database.php';

$controller = new MahasiswaController($conn);

$requestUri = $_SERVER['REQUEST_URI'];

if ($_SERVER['REQUEST_METHOD'] == 'GET' && isset($_GET['id'])) {
    $controller->getMahasiswaById($_GET['id']);
} elseif ($_SERVER['REQUEST_METHOD'] == 'GET') {
    $controller->getMahasiswa();
} elseif ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_GET['action']) && $_GET['action'] == 'delete' && isset($_GET['id'])) {
    $controller->deleteMahasiswa($_GET['id']);
} elseif ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_GET['id'])) {
    $controller->updateMahasiswa($_GET['id']);
} elseif ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $controller->createMahasiswa();
}
?>
