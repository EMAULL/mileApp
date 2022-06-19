# mileApp
QA Engineer Test
# JAWABAN QA ENGINEER TEST MILEAPP

1. Sebutkan 3 kesalahan besar yang paling sering dilakukan oleh QA, dan berikan solusinya agar
tidak terjadi atau terulang kembali.

Jawaban :
- Sulit untuk menyampaikan atau berkomunikasi dan Takut bertanya. Solusinya pahami apa yang mau ditanyakan sebelum bertanya dan beranikan bahwa ini merupakan tanggung jawab sebagai QA itu sendiri.
- Memulai testing sebelum memahami ruang environment dan requirement. Solusinya selalu pastikan semuanya sudah tidak ada yang mengganjal sebelum memulai testing dan selalu bertanya kepada team dan senior atau manager QA.
- Penulisan defect report yang kurang baik dan saat menulis test case terlupakan beberapa requirement. Solusinya mempelajari dokumentasi sebelumnya agar menjadi referensi, terus belajar dan tidak malu bertanya.

2. Jelaskan poin-poin terpenting yang harus diperhatikan dalam menganalisa dan membuat
skenario test.

Jawaban :
- Tulis kasus uji dengan perspektif end-users.
- Tulis langkah-langkah test dengan cara yang sederhana sehingga siapapun dapat mengerti.
- Jadikan Test case dapat digunakan kembali.
- Tetapkan priority.
- Memberikan test case description, test data, expected result, precondition, postcondition.
- Tulis test case yang invalid bersama dengan test case yang valid atau secara keseluruhan tidak ada yang ter-lewat sesuai dengan requirement.
- Menggunakan penamaan yang tepat.
- Review test case secara teratur, update dan apabila perlu di review oleh team.

3. Buatlah Skenario Test UI, Skenario Test API, dan Automation Testing.

Jawaban :

a. Login organisasi memasukkan nama organisasi
- Login menggunakan dengan nama organisasi yang valid.
- Login menggunakan dengan nama organisasi yang invalid.
- Login dengan mengosongkan field nama organisasi yang valid.

b. Login user dan password
- Login menggunakan dengan username/email dan password yang valid.
- Login menggunakan dengan username/email yang invalid dan password yang valid.
- Login menggunakan dengan username/email yang valid dan password yang invalid.
- Login dengan mengosongkan field username/email dan password.
- Login dengan mengosongkan field username/email.
- Login dengan mengosongkan field password.
- Verify tombol SHOW/HIDE field password berfungsi.

TEST API

Test Name : Failed Login

End point : https://apidev.mile.app/v1/login

response  : {"status":false,"message":"Login failed, please check your email or password."}

