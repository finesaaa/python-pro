meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "ROFL digunakan sebagai reaksi terhadap sesuatu yang lucu, mirip dengan LOL"
            }

word = input("Ketik kata modern yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Kita belum memiliki kata ini... Tapi kita sedang mengusahakannya!")
