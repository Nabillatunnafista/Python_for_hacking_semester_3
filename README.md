# 🐍🖥️Python-for-Hacking — PRAKTEK KONSEP JARINGAN (TCP & UDP) semester 3

* ### NAME : Nabillatun Nafista
* ### NRP : 3124521027
  ---
## 📁 Struktur Project

```
PYTHON FOR HACKING/
│── Tcp_client.py      # Client TCP
│── Tcp_server.py      # Server TCP
│── Tcp_socket.py      # Modul socket TCP (versi modular)
│── Udp_client.py      # Client/Socket UD
│── Udp_server.py      # Server UDP
│── readme.md          # Dokumentasi project
```
---
## 📝 TCP dan UDP
Pada praktikum ini, kita akan mendalami dua protokol kunci di lapisan Transport: UDP (User Datagram Protocol) dan TCP (Transmission Control Protocol), yang keduanya memfasilitasi komunikasi Klien-Server.
* **UDP** adalah protokol yang tanpa koneksi (connectionless). Ia tidak memerlukan handshake dan fokus pada kecepatan transfer data. Karena tidak ada mekanisme pengecekan, UDP tidak menjamin pengiriman data, urutan, maupun integritasnya. Protokol ini ideal untuk aplikasi yang sensitif terhadap waktu (real-time) seperti game online, streaming video, dan VoIP.
* **TCP** sebaliknya, adalah protokol berorientasi koneksi (connection-oriented). Protokol ini memulai komunikasi dengan three-way handshake dan secara ketat menjamin bahwa semua data terkirim dengan lengkap dan berurutan. TCP digunakan pada aplikasi yang menuntut keandalan tinggi, seperti Web (HTTP), email, dan transfer fil
---
## 🎯 Tujuan
Proyek ini dirancang untuk mencapai tujuan-tujuan praktikum berikut:
1. Memahami secara praktik perbedaan fundamental antara protokol TCP (Connection-Oriented) dan UDP (Connectionless).
2. Menguasai penggunaan socket pada Python untuk membangun komunikasi jaringan yang sederhana.
3. Mengimplementasikan fungsi dasar Server (Bind, Listen, Accept) dan Klien (Connect, Send, Recv) untuk masing-masing protokol.
---
## 🚀 Cara Menjalankan
1. TCP Server
   ```bash
    Python Tcp_server.py
    ```
   #### Outputnya
   <img width="600" height="195" alt="image" src= https://github.com/Nabillatunnafista/Python_for_hacking_semester_3/blob/4ddb60252aa8b68ddec75900e2473ec39505ccf4/gambar/Tcp%20server.png>
2. TCP Client
   ```bash
    Python Tcp_client.py
    ```
   #### Outputnya
   <img width="600" height="195" alt="image" src= https://github.com/Nabillatunnafista/Python_for_hacking_semester_3/blob/4ddb60252aa8b68ddec75900e2473ec39505ccf4/gambar/Tcp%20client%20.png >
3. UDP Server
   ```bash
    Python Udp_server.py
    ```
   #### Outputnya
   <img width="600" height="195" alt="image" src= https://github.com/Nabillatunnafista/Python_for_hacking_semester_3/blob/4ddb60252aa8b68ddec75900e2473ec39505ccf4/gambar/Udp%20server.png >
4. UDP Client
   ```bash
    Python Udp_client.py
    ```
   #### Outputnya
   <img width="600" height="195" alt="image" src= https://github.com/Nabillatunnafista/Python_for_hacking_semester_3/blob/4ddb60252aa8b68ddec75900e2473ec39505ccf4/gambar/Udp%20client.png>

---
## ✅ Requirement
* Python 3.8 atau lebih baru
* Tidak butuh library tambahan
  Menggunakan built-in module:

```python
import socket
```
---
## 🖥️ Referensi Video Pembelajaran
* TCP: https://youtu.be/GlVfVn17_ug?si=KDHRpRAikI445ey2
* UDP SERVER: https://youtu.be/i1AOd7AQcok?si=mJ859eniuPcbnWoG
* UDP CLIENT: https://youtu.be/bKfDS1lOSho?si=SH-mh0x65_jg-bur
---
