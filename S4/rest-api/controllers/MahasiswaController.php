<?php

include_once '../models/Mahasiswa.php';

class MahasiswaController
{
    private $mahasiswa;

    public function __construct($conn)
    {
        $this->mahasiswa = new Mahasiswa($conn);
    }

    public function getMahasiswa()
    {
        $data = $this->mahasiswa->getAll();
        echo json_encode($data);
    }

    public function getMahasiswaById($id)
    {
        $data = $this->mahasiswa->getById($id);
        echo json_encode($data);
    }

    public function createMahasiswa()
    {
        $data = json_decode(file_get_contents("php://input"), true);
        if (isset($data['nim'], $data['nama'], $data['no_hp'])) {
            $nim = $data['nim'];
            $nama = $data['nama'];
            $no_hp = $data['no_hp'];

            if ($this->mahasiswa->create($nim, $nama, $no_hp)) {
                echo json_encode(["message" => "Mahasiswa created successfully"]);
            } else {
                echo json_encode(["message" => "Failed to create mahasiswa"]);
            }
        }
    }

    public function updateMahasiswa($id)
    {
        $data = json_decode(file_get_contents("php://input"), true);
        if (isset($data['nim'], $data['nama'], $data['no_hp'])) {
            $nim = $data['nim'];
            $nama = $data['nama'];
            $no_hp = $data['no_hp'];

            if ($this->mahasiswa->update($id, $nim, $nama, $no_hp)) {
                echo json_encode(["message" => "Mahasiswa updated successfully"]);
            } else {
                echo json_encode(["message" => "Failed to update mahasiswa"]);
            }
        }
    }

    public function deleteMahasiswa($id)
    {
        if ($this->mahasiswa->delete($id)) {
            echo json_encode(["message" => "Mahasiswa deleted successfully"]);
        } else {
            echo json_encode(["message" => "Failed to delete mahasiswa"]);
        }
    }

}
?>
