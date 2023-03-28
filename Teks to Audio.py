# pip install gtts untuk menjalankan code di bawah
# Import modul yang diperlukan untuk mengelola text agar dapat diubah menjadi audio
from gtts import gTTS

# import module yang penting dan di perlukan untuk memutar audio yang sudah di buat
import os

# user memasukkan inputan
kalimat = input("Masukkan kalimat Anda : ")

# kalimat yang dimasukkan di ubah menjadi list agar dapat di manipulasi
# data = list(kalimat)
# data array yang sudah terbentuk di satukan kembali dengan tanda hubung spasi antar charakter
# dataJoin = " ".join(data)

# text yang sudah di gabungkkan di masukkan kedalam variabel yang akan diconvert menjadi audio
text = kalimat
# mencetak text untuk memastikan hasil yang di olah sudah benar
# print(textNIM)

# memilih bahasa yang digunakan dalam audio
# pilih bahasa
# print("")
# print("---------------------")
# print("No Bahasa")
# print("---------------------")
# print(" 1 Bahasa Inggris")
# print(" 2 Bahasa Indonesia")
# print(" 3 Bahasa Jepang")
# print(" 4 Bahasa Mandarin")
# print("---------------------")

#user di minta untuk memilih bahasa yang ingin digunakan di dalam audio
# pilihan = int(input("Masukkan Pilihan Anda : "))
# if pilihan == 1:
#       language = 'en' #menggunakan bahasa inggris
#       # passing object text, bahasa dan setingan kecepatan dalam berbicara pada audio yang akan di buat
#       # dan di simpan kedalam variabel objAudio
#       # bicara cepat dalam audio jika slow = true
#       # bicara lambat dalam audio jika slow = false
#       objAudio = gTTS(text=textNIM, lang=language, slow=True)
#       objAudio.save("sayNim.mp3") #membuat file audio yang berekstensi .mp3 dengan nama sayNim.mp3
#       os.system("start sayNim.mp3") #memainkan file sayNim.mp3
# elif pilihan == 2:
#       language = 'id' #menggunakan bahasa indonesia
#       # passing object text, bahasa dan setingan kecepatan dalam berbicara pada audio yang akan di buat
#       # dan di simpan kedalam variabel objAudio
#       # bicara cepat dalam audio jika slow = true
#       # bicara lambat dalam audio jika slow = false
#       objAudio = gTTS(text=textNIM, lang=language, slow=False)
#       objAudio.save("sayNim.mp3") #membuat file audio yang berekstensi .mp3 dengan nama sayNim.mp3
#       os.system("start sayNim.mp3") #memainkan file sayNim.mp3
# elif pilihan == 3:
#       language = 'ja' #menggunakan bahasa jepang
#       # passing object text, bahasa dan setingan kecepatan dalam berbicara pada audio yang akan di buat
#       # dan di simpan kedalam variabel objAudio
#       # bicara cepat dalam audio jika slow = true
#       # bicara lambat dalam audio jika slow = false
#       objAudio = gTTS(text=textNIM, lang=language, slow=True)
#       objAudio.save("sayNim.mp3") #membuat file audio yang berekstensi .mp3 dengan nama sayNim.mp3
#       os.system("start sayNim.mp3") #memainkan file sayNim.mp3
# elif pilihan == 4:
#       language = 'zh-CN' #menggunakan bahasa mandarin/china
#       # passing object text, bahasa dan setingan kecepatan dalam berbicara pada audio yang akan di buat
#       # dan di simpan kedalam variabel objAudio
#       # bicara cepat dalam audio jika slow = true
#       # bicara lambat dalam audio jika slow = false
#       objAudio = gTTS(text=textNIM, lang=language, slow=True)
#       objAudio.save("sayNim.mp3") #membuat file audio yang berekstensi .mp3 dengan nama sayNim.mp3
#       os.system("start sayNim.mp3") #memainkan file sayNim.mp3
# else :
#       # default nya program akan menggunakan bahasa indonesia
#       language = 'id' #menggunakan bahasa indonesia
#       # passing object text, bahasa dan setingan kecepatan dalam berbicara pada audio yang akan di buat
#       # dan di simpan kedalam variabel objAudio
#       # bicara cepat dalam audio jika slow = true
#       # bicara lambat dalam audio jika slow = false
#       objAudio = gTTS(text=textNIM, lang=language, slow=True)
#       objAudio.save("sayNim.mp3") #membuat file audio yang berekstensi .mp3 dengan nama sayNim.mp3
#       os.system("start sayNim.mp3") #memainkan file sayNim.mp3

language = 'id' #menggunakan bahasa indonesia
objAudio = gTTS(text=text, lang=language, slow=False)
objAudio.save("kalimat.mp3") #membuat file audio yang berekstensi .mp3 dengan nama kalimat.mp3
os.system("start kalimat.mp3") #memainkan file kalimat.mp3