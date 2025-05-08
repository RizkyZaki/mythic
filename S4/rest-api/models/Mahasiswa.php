<?php

class Mahasiswa
{
    private $conn;

    public function __construct($conn)
    {
        $this->conn = $conn;
    }

    public function getAll()
    {
        $sql = "SELECT * FROM mahasiswa";
        $result = $this->conn->query($sql);
        return $result->fetch_all(MYSQLI_ASSOC);
    }

    public function getById($id)
    {
        $stmt = $this->conn->prepare("SELECT * FROM mahasiswa WHERE id = ?");
        $stmt->bind_param("i", $id);
        $stmt->execute();
        return $stmt->get_result()->fetch_assoc();
    }

    public function create($nim, $nama, $no_hp)
    {
        $stmt = $this->conn->prepare("INSERT INTO mahasiswa (nim, nama, no_hp) VALUES (?, ?, ?)");
        $stmt->bind_param("sss", $nim, $nama, $no_hp);
        return $stmt->execute();
    }

    public function update($id, $nim, $nama, $no_hp)
    {
        $stmt = $this->conn->prepare("UPDATE mahasiswa SET nim = ?, nama = ?, no_hp = ? WHERE id = ?");
        $stmt->bind_param("sssi", $nim, $nama, $no_hp, $id);
        return $stmt->execute();
    }

    public function delete($id)
    {
        $stmt = $this->conn->prepare("DELETE FROM mahasiswa WHERE id = ?");
        $stmt->bind_param("i", $id);
        return $stmt->execute();
    }
}
?>
