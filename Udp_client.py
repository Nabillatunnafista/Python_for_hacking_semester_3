import socket

target_Host = "127.0.0.1"
target_Port = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP

#kirim data
client.sendto(b"Hallo semua saya Nabillatun Nafista", (target_Host, target_Port))

#menerima data
data, addr = client.recvfrom(4096)
print ("pesan dari server: \"{}\"".format(data.decode()))

client.close()