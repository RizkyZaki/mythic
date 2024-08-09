import sqlite3
import matplotlib.pyplot as plt
from prettytable import PrettyTable

DATABASE_FILE = "karakter_anime.sqlite3"
conn = sqlite3.connect(DATABASE_FILE)
curs = conn.cursor()
def create_table():
    """Membuat table (dan database jika file belum ada)
    Args: None
    Output: Success message
    Returns: None
    """
    # Buat kode untuk membuat tabel anime pada database karakter_anime.sqlite3
    curs.execute("""
                  CREATE TABLE IF NOT EXISTS table_anime(
                    id INTEGER NOT NULL PRIMARY KEY,
                    nama TEXT NOT NULL,
                    anime TEXT NOT NULL,
                    power_level INTEGER(11) NOT NULL,
                    health INTEGER(100) NOT NULL
                    )
                """)
    print("Table Berhasil Dibuat")
    conn.commit()
    

def insert_character(nama, anime, power_level, health):
    """Menyisipkan karakter baru ke dalam database
    Args:
        nama: str, nama karakter
        anime: str, judul anime
        power_level: float, tingkat kekuatan karakter
        health: int, tingkat kesehatan karakter
    Output: Success message
    Returns: None
    """
    # Buat kode untuk memasukkan 4 karakter legendaris secara otomatis ke dalam tabel anime
    curs.execute("INSERT INTO table_anime(nama,anime,power_level,health) VALUES (?,?,?,?)",(nama, anime, power_level, health))
    conn.commit()

def select_all_characters():
    """Mengambil dan mencetak semua karakter dari database
    Args: None
    Output: Informasi karakter dalam database
    Returns: None
    """
    # Buat kode untuk menampilkan isi dari semua tabel anime
    curs.execute("SELECT * FROM table_anime")
    rows = curs.fetchall()
    if rows:
        table = PrettyTable()
        table.field_names = ["ID", "Nama", "Anime", "Power Level", "Health"]
        for row in rows:
            table.add_row(row)
        print(table)
    else:
        print("Data Kosong.")
        
    conn.commit()

def simulate_battle(character_id, enemy_id):
    """Mensimulasikan pertempuran antara karakter dengan musuh
    Args:
        character_id: int, id karakter yang menyerang
        enemy_id: int, id musuh yang diserang
    Output: Hasil pertempuran
    Returns: None
    """
    # Buat kode untuk mengambil informasi karakter yang menyerang (character_id) dan musuh yang diserang (enemy_id)
    character = curs.execute(f"SELECT * FROM table_anime WHERE  {character_id}")
    enemy = curs.execute(f"SELECT * FROM table_anime WHERE  {enemy_id}")
    
    char = character.fetchone()
    enem = enemy.fetchone()
    # Mengurangi health musuh berdasarkan power level karakter
    resultBattle = (enem[4] - char[3])
    
    # Buat kode untuk mengupdate kesehatan musuh dalam database setelah
    curs.execute(f"UPDATE table_anime SET health = {resultBattle} WHERE id = {enem[0]}")

    # print hasil pertempuran
    print(f"{char[1]} menyerang {enem[1]}! , {enem[1]} health berkurang menjadi {resultBattle}")
    conn.commit()

def visualize_health():
    """Visualisasi kesehatan karakter setelah semua pertarungan selesai dilakukan"""

    # Buat kode untuk menampilkan visualisasi (bar chart) dimana nama karakter di sumbu x dan tingkat kesehatan di sumbu y.
    curs.execute("""
                  SELECT nama, health FROM table_anime
                """)
    rows = curs.fetchall()
    nama = [row[0] for row in rows]
    health = [row[1] for row in rows]
    plt.figure(figsize=(10, 6))
    plt.bar(nama,health, color='skyblue')
    plt.xlabel('Health')
    plt.ylabel('Nama Karakter')
    plt.title('Kesehatan Karakter Setelah Pertempuran')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    conn.commit()
    


# Buat pemanggilan fungsi sesuai dengan operasi yang diminta pada soal latihan

create_table()
insert_character('Son Goku','Dragon Ball',5000, 10000)
insert_character('Naruto Uzumaki','Naruto',4000, 7500)
insert_character('Monkey D Luffy','One Piece',3000, 6000)
insert_character('Ichigo','Bleach',3500, 5000)
simulate_battle(1,2)
select_all_characters()
visualize_health()

conn.close()

