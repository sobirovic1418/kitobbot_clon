
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

start_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("☎️ Murojat uchun tel raqam")
        ],
        [
            KeyboardButton("✅Foydali kanallar va ulardan foydalanish")
        ],
        [
            KeyboardButton("🇬🇧 English")
        ],
        [
            KeyboardButton("📚 O'zbek adabiyoti"),
            KeyboardButton("📚 Jahon adabiyoti")
        ],
        [
            KeyboardButton("📚 Bolalar adabiyoti"),
            KeyboardButton("📚 Muntoz adabiyot")
        ],
        [
            KeyboardButton("🎧 Audio kitoblar"),
            KeyboardButton("💯 Top 100 kitoblar")
        ],
        [
            KeyboardButton("📚 Maktab darsliklari"),
            KeyboardButton("📚 Islomiy kitoblar")
        ],
        [
            KeyboardButton("🔍 Lug'atlar")
        ],
        [
            KeyboardButton("📝 She'riyat"),
            KeyboardButton("📜 Alisher Navoiy asarlari")
        ],
        [
            KeyboardButton("📜O'zbekiston Milliy Ensiklopediyasi"),
            KeyboardButton("📋 O'zbek tilining izohli lug'atlari")
        ],
        [
            KeyboardButton("🔍 O'zbek tilining imlo lug'ati")
        ],
        [
            KeyboardButton("Islom Karimov asarlari"),
            KeyboardButton("Shavkat Mirziyoyev asarlari")
        ],
        [
            KeyboardButton("📥 Kitob o'qish uchun dasturlar")
        ],
        [
            KeyboardButton("🤖 Botni guruhga qo'shish"),
            KeyboardButton("↗️ Botni do'stlarga ulashish")
        ],
        [
            KeyboardButton("♻️ Takliflar"),
            KeyboardButton("⭐ Botni baholash")
        ]
    ],
    resize_keyboard=True
)

english_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📚 Grammatika"),
            KeyboardButton("📚 IELTS")
        ],
        [
            KeyboardButton("📚 Vocabulary"),
            KeyboardButton("📚 Testlar")
        ],
        [
            KeyboardButton("📚 Fiction Books")
        ],
        [
            KeyboardButton("🇬🇧 Ingliz tilidan foydali kanallar")
        ],
        [
            KeyboardButton("Go Back")
        ]
    ],
    resize_keyboard=True
)

ozb_adb=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👤 Abdulla Qodiriy"),
            KeyboardButton("👤 Cho'lpon")
        ],
        [
            KeyboardButton("👤 Oybek"),
            KeyboardButton("👤 G'afur G'ulom")
        ],
        [
            KeyboardButton("👤 Abdulla Qahhor"),
            KeyboardButton("👤 Said Ahmad")
        ],
        [
            KeyboardButton("👤 O'tkir Hoshimov"),
            KeyboardButton("👤 Pirimqul Qodirov")
        ],
        [
            KeyboardButton("👤 Asqad Muxtor"),
            KeyboardButton("👤 Odil Yoqubov")
        ],
        [
            KeyboardButton("👤 Tog'ay Murod"),
            KeyboardButton("👤 Tohir Malik")
        ],
        [
            KeyboardButton("👤 O'lmas Umarbekov")
        ],
        [
            KeyboardButton("Go Back")
        ]
    ],
    resize_keyboard=True
)

jahon_adb=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👤 Lev Tolstoy"),
            KeyboardButton("👤 Aleksandr Pushkin")
        ],
        [
            KeyboardButton("👤 Fyodor Dostoyevskiy"),
            KeyboardButton("👤 Mixail Bulgakov")
        ],
        [
            KeyboardButton("👤 Chingiz Aytmatov"),
            KeyboardButton("👤 Nodar Dumbadze")
        ],
        [
            KeyboardButton("👤 Jek London"),
            KeyboardButton("👤 Gabriel Garsia Markes")
        ],
        [
            KeyboardButton("👤 Alber Kamyu"),
            KeyboardButton("👤 Kobo Abe")
        ],
        [
            KeyboardButton("👤 Lao She"),
            KeyboardButton("👤 Artur Konan Doyl")
        ],
        [
            KeyboardButton("👤 Agata Kristi"),
            KeyboardButton("👤 Gi De Mopassan")
        ],
        [
            KeyboardButton("👤 Onor De Balzak"),
            KeyboardButton("👤 Ernest Xeminguey")
        ],
        [
            KeyboardButton("👤 Jeyms Joys"),
            KeyboardButton("👤 Jonatan Svift")
        ],
        [
            KeyboardButton("👤 Jyul Vern"),
            KeyboardButton("👤 Somerset Moem")
        ],
        [
            KeyboardButton("👤 Robindranat Tagor")
        ],
        [
            KeyboardButton("Go Back")
        ]
    ],
    resize_keyboard=True
)

bola_adb=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📚 Ertaklar")
        ],
        [
            KeyboardButton("🤓 Qiziqarli kitoblar | Bolalar ensiklopediyasi")
        ],
        [
            KeyboardButton("Go Back")
        ]
    ],
    resize_keyboard=True
)

mun_adb=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📓 Boburnoma")
        ],
        [
            KeyboardButton("📓 Shohnoma")
        ],
        [
            KeyboardButton("📓 Zarbulmasal")
        ],
        [
            KeyboardButton("📓 To'rt ulus tarixi")
        ],
        [
            KeyboardButton("📓 Devoni lug'otut turk")
        ],
        [
            KeyboardButton("📓 Qutadg'u bilig")
        ],
        [
            KeyboardButton("Go Back")
        ]
    ],
    resize_keyboard=True
)

aud_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🇺🇿 O'zbek adabiyoti")
        ],
        [
            KeyboardButton("🌐 Jahon adabiyoti")
        ],
        [
            KeyboardButton("Go Back")
        ]
    ],
    resize_keyboard=True
)

mak_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🇺🇿 O'zbekcha")
        ],
        [
            KeyboardButton("🇷🇺 Ruscha")
        ],
        [
            KeyboardButton("Go Back")
        ]
    ],
    resize_keyboard=True
)

din_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Tafsiri Hilol"),
            KeyboardButton("Jannat vasfi")
        ],
        [
            KeyboardButton("Keng rizq va baraka omillari")
        ],
        [
            KeyboardButton("Istig'forning 40 xosiyati | Salovotlar")
        ],
        [
            KeyboardButton("Qur'on - qalblar shifosi")
        ],
        [
            KeyboardButton("Baxtli hayot sari")
        ],
        [
            KeyboardButton("Payg'ambar uyida bir kun")
        ],
        [
            KeyboardButton("Shamoili Muhammadiy")
        ],
        [
            KeyboardButton("Abu Bakr Siddiq")
        ],
        [
            KeyboardButton("Sunani Termiziy")
        ],
        [
            KeyboardButton("Hazrati Umar ibn Xattob")
        ],
        [
            KeyboardButton("Musnad")
        ],
        [
            KeyboardButton("Mukoshafat-ul qulub")
        ],
        [
            KeyboardButton("Ramazon va taqvo")
        ],
        [
            KeyboardButton("Go Back")
        ]
    ],
    resize_keyboard=True
)

lug_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🗂 Pdf lug'atlar"),
            KeyboardButton("🗂 Pdf lug'atlar")
        ],
        [
            KeyboardButton("🌐 Google tarjimon")
        ],
        [
            KeyboardButton("Go Back")
        ]
    ],
    resize_keyboard=True
)
sher_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👤 Erkin Vohidov"),
            KeyboardButton("👤 Abdulla Oripov")
        ],
        [
            KeyboardButton("👤 Rauf Parfi"),
            KeyboardButton("👤 Shavkat Rahmon")
        ],
        [
            KeyboardButton("👤 Muhammad Yusuf"),
        ],
        [
            KeyboardButton("Go Back")
        ]
    ],
    resize_keyboard=True
)

kit_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📒 Pdf kitoblar uchun")
        ],
        [
            KeyboardButton("📒 Djvu kitoblar uchun")
        ],
        [
            KeyboardButton("📒 Epub kitoblar uchun")
        ],
        [
            KeyboardButton("📒 Zip kitoblar uchun")
        ],
        [
            KeyboardButton("Go Back")
        ]
    ],
    resize_keyboard=True
)

tex_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Done")
        ],
        [
            KeyboardButton("Bekor qilish")
        ]
    ],
    resize_keyboard=True
)

baho_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("⭐⭐⭐⭐⭐ | A'lo")
        ],
        [
            KeyboardButton("⭐⭐⭐⭐ | Yaxshi")
        ],
        [
            KeyboardButton("⭐⭐⭐ | O'rtacha")
        ],
        [
            KeyboardButton("⭐⭐ | Qoniqarli")
        ],
        [
            KeyboardButton("Bekor qilish")
        ],
        [
            KeyboardButton("Go Back")
        ]
    ],
    resize_keyboard=True
)

taklif_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Done")
        ],
        [
            KeyboardButton("Bekor qilish")
        ]
    ],
    resize_keyboard=True
)

uzb_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Romanlar")
        ],
        [
            KeyboardButton("Hikoyala")
        ],
        [
            KeyboardButton("Qissalar")
        ],
        [
            KeyboardButton("Back")
        ],
    ],
    resize_keyboard=True
)
russ_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Romanlar")
        ],
        [
            KeyboardButton("Hikoyalar")
        ],
        [
            KeyboardButton("Qissalar")
        ],
        [
            KeyboardButton("Back")
        ],
    ],
    resize_keyboard=True
)

rom_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🌐 Romanlar")
        ],
        [
            KeyboardButton("🌐 Qissalar")
        ],
        [
            KeyboardButton("🌐 Hikoyalar")
        ],
        [
            KeyboardButton("Back")
        ]
    ],
    resize_keyboard=True
)
fan_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🔢 Sinflar bo'yicha")
        ],
        [
            KeyboardButton("📔 Fanlar bo'yicha")
        ],
        [
            KeyboardButton("orqaga")
        ]
    ],
    resize_keyboard=True
)
rus_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🔢 Sinflar bo'yicha 🇷🇺")
        ],
        [
            KeyboardButton("⬅️")
        ]
    ],
    resize_keyboard=True
)
sinf_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📙 1-sinf")
        ],
        [
            KeyboardButton("📙 2-sinf")
        ],
        [
            KeyboardButton("📙 3-sinf")
        ],
        [
            KeyboardButton("📙 4-sinf")
        ],
        [
            KeyboardButton("📙 5-sinf")
        ],
        [
            KeyboardButton("📙 6-sinf")
        ],
        [
            KeyboardButton("📙 7-sinf")
        ],
        [
            KeyboardButton("📙 8-sinf")
        ],
        [
            KeyboardButton("📙 9-sinf")
        ],
        [
            KeyboardButton("📙 10-sinf")
        ],
        [
            KeyboardButton("📙 11-sinf")
        ],
        [
            KeyboardButton("ortga")
        ]
    ],
    resize_keyboard=True
)
ozb_btn=ReplyKeyboardMarkup(
    keyboard=[
[
            KeyboardButton("📗 1-sinf")
        ],
        [
            KeyboardButton("📗 2-sinf")
        ],
        [
            KeyboardButton("📗 3-sinf")
        ],
        [
            KeyboardButton("📗 4-sinf")
        ],
        [
            KeyboardButton("📗 5-sinf")
        ],
        [
            KeyboardButton("📗 6-sinf")
        ],
        [
            KeyboardButton("📗 7-sinf")
        ],
        [
            KeyboardButton("📗 8-sinf")
        ],
        [
            KeyboardButton("📗 9-sinf")
        ],
        [
            KeyboardButton("📗 10-sinf")
        ],
        [
            KeyboardButton("📗 11-sinf")
        ],
        [
            KeyboardButton("⬅️")
        ]
    ],
    resize_keyboard=True
)
fanl_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🇺🇿 Ona tili")
        ],
        [
            KeyboardButton("📚 Adabiyot")
        ],
        [
            KeyboardButton("🇬🇧 Ingliz tili")
        ],
        [
            KeyboardButton("🇩🇪 Nemis tili")
        ],
        [
            KeyboardButton("🇫🇷 Fransuz tili")
        ],
        [
            KeyboardButton("🇷🇺 Rus tili")
        ],
        [
            KeyboardButton("🗺 Geografiya")
        ],
        [
            KeyboardButton("🔍 Tarix")
        ],
        [
            KeyboardButton("🔬 Fizika")
        ],
        [
            KeyboardButton("🔢 Matematika")
        ],
        [
            KeyboardButton("🩺 Biologiya")
        ],
        [
            KeyboardButton("🌡 Kimyo")
        ],
        [
            KeyboardButton("🏃‍♂ Jismoniy tarbiya")
        ],
        [
            KeyboardButton("⬅️")
        ]
    ]
)

roman_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Abdulla Qodiriy - Otkan kunlar")
        ],
        [
            KeyboardButton("Abdulla Qodiriy - Mehrobdan chayon")
        ],
        [
            KeyboardButton("Oybek - Navoiy")
        ],
        [
            KeyboardButton("Pirimqul Qodirov - Yulduzli tunlar")
        ],
        [
            KeyboardButton("Said Ahmad - Ufq")
        ],
        [
            KeyboardButton("Tohir Malik - Shaytanat")
        ],
        [
            KeyboardButton("Cho'lpon - Kecha va kunduz")
        ],
        [
            KeyboardButton("GO Back")
        ]
    ],
    resize_keyboard=True
)

qissa_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("G'afur G'ulom - Shum bola")
        ],
        [
            KeyboardButton("Tog'ay Murod - Yulduzlar mangu yonadi")
        ],
        [
            KeyboardButton("Tohir Malik - Alvido bolalik")
        ],
        [
            KeyboardButton("O'tkir Hoshimov - Dunyoning ishlari")
        ],
        [
            KeyboardButton("GO Back")
        ]
    ],
    resize_keyboard=True
)

rroman_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("O'nta negir bolasi")
        ],
        [
            KeyboardButton("Dengiz sarguzashtlari")
        ],
        [
            KeyboardButton("Graf Monte Kristo")
        ],
        [
            KeyboardButton("O'gay ona")
        ],
        [
            KeyboardButton("GO Back")
        ]
    ],
    resize_keyboard=True
)
rqissa_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Chingiz Aytmatov - "Jamila"')
        ],
        [
            KeyboardButton('Paulo Koelo - "Alkimyogar"')
        ],
        [
            KeyboardButton('Chingiz Aytmatov - "Chingizxonning oq buluti"')
        ],
        [
            KeyboardButton('GO Back')
        ]
    ],
    resize_keyboard=True
)
