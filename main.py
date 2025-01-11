from aiogram import types, executor

from head_fun import dp
from key_btn import start_btn, english_btn, ozb_adb, jahon_adb, bola_adb, mun_adb, aud_btn, baho_btn, kit_btn, \
    taklif_btn, uzb_btn, rom_btn, fan_btn, rus_btn, sinf_btn, ozb_btn, fanl_btn, roman_btn, rroman_btn, rqissa_btn, \
    qissa_btn
from key_btn import sher_btn, mak_btn, lug_btn, din_btn
from inline_btn import kanal_ibtn

@dp.message_handler(commands=["start"])
async def start_fun(message: types.Message):
    await message.answer(f"Assalomu alaykum{message.from_user.full_name}\n"
                         f"botimizga xush kelibsiz!!!", reply_markup=start_btn)


@dp.message_handler(text=["☎️ Murojat uchun tel raqam"])
async def sal(message: types.Message):
    await message.answer("""Savol va takliflaringiz bo'lsa, ushbu @Bizga_murojaatbot ga 
    yozib qoldirishingiz mumkin (Biz uni albatta ko'rib chiqamiz)""")


@dp.message_handler(text=["✅Foydali kanallar va ulardan foydalanish"])
async def qan(message: types.Message):
    await message.answer("""@English_books_new - Ingliz tilidan barcha turdagi (Grammatika, IELTS, vocabulary, test va badiiy) kitoblarini topishingiz mumkin!

@Tarix - Ushbu kanal orqali tarixni oson o'rganing!


Yuqoridagi kanallarga reklama berish shartlari bilan batafsi bu yerda tanishing 👇

https://t.me/joinchat/RoDr_1utiTbt9T7C

@Elektron_kutubxona_kitoblarbot botidan kelganingizni aytsangiz 10% chegirma bor""", reply_markup=kanal_ibtn)


@dp.message_handler(text=["🇬🇧 English"])
async def english(message: types.Message):
    await message.answer("Sizga ingliz tilidan grammatik kitoblar kerakmi yoki"
                         " IELTS kitoblarimi? Tanlang! 👇", reply_markup=english_btn)


@dp.message_handler(text=["📚 O'zbek adabiyoti"])
async def uzb(message: types.Message):
    await message.answer("Sizga qaysi yozuvchining asarlari kerak? Tanlang! 👇",
                         reply_markup=ozb_adb)


@dp.message_handler(text=["📚 Jahon adabiyoti"])
async def jah(message: types.Message):
    await message.answer("Yozuvchini tanlang", reply_markup=jahon_adb)


@dp.message_handler(text=["📚 Bolalar adabiyoti"])
async def bol(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=bola_adb)


@dp.message_handler(text=["📚 Muntoz adabiyot"])
async def mun(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=mun_adb)


@dp.message_handler(text=["🎧 Audio kitoblar"])
async def aud(message: types.Message):
    await message.answer("Sizga o'zbek adabiyotidan audio kitoblar kerakmi yoki jahon adabiyotidanmi? Tanlang! 👇",
                         reply_markup=aud_btn)


@dp.message_handler(text=["💯 Top 100 kitoblar"])
async def top(message: types.Message):
    await message.answer("Marhamat")


@dp.message_handler(text=["📚 Maktab darsliklari"])
async def mak(message: types.Message):
    await message.answer("Sizga o'zbekcha darsliklar kerakmi yoki ruscha darsliklarmi? Tanlang! 👇",
                         reply_markup=mak_btn)


@dp.message_handler(text=["📚 Islomiy kitoblar"])
async def din(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=din_btn)


@dp.message_handler(text=["🔍 Lug'atlar"])
async def lul(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=lug_btn)


@dp.message_handler(text=["📝 She'riyat"])
async def she(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=sher_btn)


@dp.message_handler(text=["📜 Alisher Navoiy asarlari"])
async def ali(message: types.Message):
    await message.answer("Keyingi sahifa: /alishernavoiy__page2")


@dp.message_handler(text=["📜O'zbekiston Milliy Ensiklopediyasi"])
async def uzb(message: types.Message):
    await message.answer("Keyingi sahifa: /ensiklopediya__page2")


@dp.message_handler(text=["📋 O'zbek tilining izohli lug'atlari"])
async def mil(message: types.Message):
    await message.answer("Keyingi sahifa: /ozbektiliningizohlilugatlari__page2")


@dp.message_handler(text=["Islom Karimov asarlari"])
async def ism(message: types.Message):
    await message.answer("Keyingi sahifa: /islomkarimovasarlari__page2")


@dp.message_handler(text=["📥 Kitob o'qish uchun dasturlar"])
async def kit(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=kit_btn)


@dp.message_handler(text=["🤖 Botni guruhga qo'shish"])
async def bo(message: types.Message):
    await message.answer("""Botni guruhga qo'shish:

Botni guruhga qo'shish uchun quyidagi link ustiga bosing va botni qo'shmoqchi bo'lgan guruhingizni tanlang. Guruhga qo'shganingizdan so'ng bot ishlashi uchun admin qiling.

LINK: http://t.me/Elektron_kutubxona_kitoblarbot?startgroup=ru""")


@dp.message_handler(text=["↗️ Botni do'stlarga ulashish"])
async def ulash(message: types.Message):
    await message.answer("""Botni do'stlarga ulashish:

Botni ulashish uchun quyidagi link ustiga bosing va ulashmoqchi bo'lgan odamingizni tanlang:

LINK: http://telegram.me/share/url?url=https://telegram.me/Elektron_kutubxona_kitoblarbot""")


@dp.message_handler(text=["♻️ Takliflar"])
async def tak(message: types.Message):
    await message.answer("""Botni rivojlantirish uchun qanday takliflaringiz bor? Yozib qoldiring, takliflaringiz albatta ko'rib chiqiladi!

P/s: Taklifingizni yozib "Done" tugmasini bosishni unutmang aks holda taklifingiz bizga kelib tushmaydi.""",
                         reply_markup=taklif_btn)


@dp.message_handler(text=["⭐ Botni baholash"])
async def mal(message: types.Message):
    await message.answer("Bot faoliyatiga baho bering! 👇", reply_markup=baho_btn)


@dp.message_handler(text=["Bekor qilish"])
async def bek(message: types.Message):
    await message.answer("Bekor qilindi", reply_markup=start_btn)


@dp.message_handler(text=["📚 Grammatika"])
async def gram(message: types.Message):
    await message.answer("https://telegra.ph/Grammar-Books-11-04")


@dp.message_handler(text=["📚 IELTS"])
async def its(message: types.Message):
    await message.answer("https://telegra.ph/IELTS-Books-11-04")


@dp.message_handler(text=["📚 Vocabulary"])
async def voc(message: types.Message):
    await message.answer("https://telegra.ph/Vocabulary-Books-11-04")


@dp.message_handler(text=["📚 Testlar"])
async def tes(message: types.Message):
    await message.answer("https://telegra.ph/Test-Books-11-04")


@dp.message_handler(text=["📚 Fiction Books"])
async def fic(message: types.Message):
    await message.answer("https://telegra.ph/Fiction-Books-12-24")


@dp.message_handler(text=["🇬🇧 Ingliz tilidan foydali kanallar"])
async def ing(message: types.Message):
    await message.answer("""@English_books_new - Ushbu kanaldan ko'proq ingliz tili kitoblarini yuklab olishingiz mumkin. ✅

@shaxzodtorayev - IELTS 7.0, Reading 8.5 sohibining blogi! 🔥""")


@dp.message_handler(text=["🇺🇿 O'zbek adabiyoti"])
async def uzb(message: types.Message):
    await message.answer("Sizga qaysi janrdagi audio kitoblar kerak? Tanlang! 👇", reply_markup=uzb_btn)


@dp.message_handler(text=["🌐 Jahon adabiyoti"])
async def jah(message: types.Message):
    await message.answer("Sizga qaysi janrdagi audio kitoblar kerak? Tanlang! 👇", reply_markup=rom_btn)


@dp.message_handler(text=["Back"])
async def bak(message: types.Message):
    await message.answer("""Sizga o'zbek adabiyotidan audio kitoblar kerakmi yoki jahon adabiyotidanmi? Tanlang! 👇""",
                         reply_markup=aud_btn)


@dp.message_handler(text=["🇺🇿 O'zbekcha"])
async def uzb(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=fan_btn)


@dp.message_handler(text=["🇷🇺 Ruscha"])
async def uzb(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=sinf_btn)


@dp.message_handler(text=["⬅️"])
async def star(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=mak_btn)


@dp.message_handler(text=["🔢 Sinflar bo'yicha 🇷🇺"])
async def sin(message: types.Message):
    await message.answer("Sizga qaysi sinf darsliklari kerak? Tanlang! 👇", reply_markup=sinf_btn)


@dp.message_handler(text=["🔢 Sinflar bo'yicha"])
async def sin(message: types.Message):
    await message.answer("Sizga qaysi sinf darsliklari kerak? Tanlang! 👇", reply_markup=ozb_btn)


@dp.message_handler(text=["📔 Fanlar bo'yicha"])
async def rus(message: types.Message):
    await message.answer("Sizga qaysi fan darsliklari kerak? Tanlang! 👇!", reply_markup=fanl_btn)


@dp.message_handler(text=["👤 Abdulla Qodiriy"])
async def abd(message: types.Message):
    kitoblar = ["static/dokuments/O'tkan Kunlar (Abdulla Qodiriy).pdf",
                "static/dokuments/Abdulla Qodiriy. Ijod mashaqqati.pdf",
                "static/dokuments/Abdulla Qodiriy. Mehrobdan chayon (roman).pdf",
                "static/dokuments/Abdulla Qodiriy. Jinlar bazmi (hikoyalar).pdf",
                "static/dokuments/[@Elektron_kutubxona_kitoblarbot] Baxtsiz kuyov.pdf"]
    for i in kitoblar:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Cho'lpon"])
async def chol(message: types.Message):
    kitoblar1 = ["static/dokuments/kitoblar/[@Elektron_kutubxona_kitoblarbot] Cho lpon. Hikoyalar, tarji.pdf",
                 "static/dokuments/kitoblar/Abdulhamid Cho'lpon. Buloqlar quchog'ida.pdf",
                 "static/dokuments/kitoblar/Cho'lpon. Kecha va kunduz (roman).pdf"]
    for i in kitoblar1:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Oybek"])
async def sal(message: types.Message):
    kitoblar2 = ["static/dokuments/Oybek. Quyosh qoraymas (roman).pdf",
                 "static/dokuments/Oybek. Bolalik (xotira-qissa).pdf",
                 "static/dokuments/Oybek. Bola Alisher (qissa).pdf"]
    for i in kitoblar2:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 G'afur G'ulom"])
async def sta(message: types.Message):
    kitoblar3 = ["static/dokuments/G'afur G'ulom.pptx",
                 "static/dokuments/G'afur G'ulom. Qayda baxt (komediya).pdf",
                 "static/dokuments/G'afur G'ulom. Muxbir sudi (pyesa).pdf",
                 "static/dokuments/G'afur G'ulom. Yodgor (qissa).pdf"]
    for i in kitoblar3:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Abdulla Qahhor"])
async def sal(message: types.Message):
    kitoblar4 = ["static/dokuments/Abdulla Qahhor. O'tmishdan ertaklar (qissa).pdf",
                 "static/dokuments/Abdulla Qahhor. Oltin yulduz (qissa).pdf",
                 "static/dokuments/Abdulla Qahhor - Sarob (roman).pdf"]
    for i in kitoblar4:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /abdullaqahhor__page2")


@dp.message_handler(text=["👤 Said Ahmad"])
async def sar(message: types.Message):
    kitoblar5 = ["static/dokuments/Said Ahmad. Cho'l burguti (hikoyalar).pdf",
                 "static/dokuments/Said Ahmad. Sobiq o'g'ri (hikoyalar).pdf",
                 "static/dokuments/Said Ahmad. Ta'zim (hikoyalar).pdf"]
    for i in kitoblar5:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /saidahmad__page2")


@dp.message_handler(text=["👤 O'tkir Hoshimov"])
async def sar(message: types.Message):
    kitoblar6 = ["static/dokuments/O'tkir Hoshimov .Ikki eshik orasi.pdf",
                 "static/dokuments/O'tkir Hoshimov. Sevgi qissalari.pdf"
                 "static/dokuments/O'tkir Hoshimov. Sevgi qissalari.pdf"]
    for i in kitoblar6:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Pirimqul Qodirov"])
async def sar(message: types.Message):
    kitoblar7 = ["static/dokuments/Pirimqul Qodirov. Avlodlar dovoni (roman).pdf",
                 "static/dokuments/Pirimqul Qodirov. Yulduzli tunlar (roman).pdf",
                 "static/dokuments/Pirimqul Qodirov. Erk (qissa).pdf"]
    for i in kitoblar7:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Asqad Muxtor"])
async def sar(message: types.Message):
    kitoblar8 = ["static/dokuments/Asqad Muxtor. Ildizlar (qissa).pdf",
                 "static/dokuments/Asqad Muxtor. Jar yoqasidagi chaqmoq (qissa).pdf",
                 "static/dokuments/(@KITOB) Asqad Muxtor - Chinor (Roman) 1-qisim.pdf)"]
    for i in kitoblar8:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Odil Yoqubov"])
async def sar(message: types.Message):
    kitoblar9 = ["static/dokuments/Odil Yoqubov. Dastlabki qadam (hikoyalar).pdf",
                 "static/dokuments/Odil Yoqubov. Billur qandillar (qissa).pdf",
                 "static/dokuments/Odil Yoqubov. Muqaddas (qissa).pdf"]
    for i in kitoblar9:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Tog'ay Murod"])
async def sar(message: types.Message):
    kitoblar0 = ["static/dokuments/Tog'ay Murod. Ot kishnagan oqshom (qissa).pdf",
                 "static/dokuments/Tog'ay Murod. Otamdan qolgan dalalar (roman).pdf",
                 "static/dokuments/Tog'ay Murod. Tanlangan asarlar. 1-jild.pdf"]
    for i in kitoblar0:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /togaymurod__page2")


@dp.message_handler(text=["👤 Tohir Malik"])
async def sak(message: types.Message):
    kitob = ["static/dokuments/Shaytanat 1- kitob.pdf",
             "static/dokuments/Shaytanat 2- kitob.pdf",
             "static/dokuments/Shaytanat 3- kitob.pdf"]
    for i in kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /tohirmalik__page2")


@dp.message_handler(text=["👤 O'lmas Umarbekov"])
async def sal(message: types.Message):
    kitob1 = ["static/dokuments/O'lmas Umarbekov. Qiyomat qarz (drama).pdf",
              "static/dokuments/O'lmas Umarbekov hayoti va ijodi.pdf",
              "static/dokuments/O'lmas Umarbekov. Yoz yomg'iri (qissa).pdf"]
    for i in kitob1:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /olmasumarbekov__page2")


@dp.message_handler(text=["👤 Lev Tolstoy"])
async def salas(message: types.Message):
    kitob2 = ["static/dokuments/Lev Tolstoy. Urush va tinchlik (1-kitob).pdf",
              "static/dokuments/Lev Tolstoy. Urush va tinchlik (2-kitob).pdf",
              "static/dokuments/Lev Nikolayevic Tolstoy - Anna Karenina.pdf"]
    for i in kitob2:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /levtolstoy__page2")


@dp.message_handler(text=["👤 Aleksandr Pushkin"])
async def sala(message: types.Message):
    kitob3 = ["static/dokuments/Aleksandr Pushkin. Marhum Ivan Petrovich Belkin qissalari.pdf",
              "static/dokuments/Aleksandr Pushkin. Poema va ertaklar.pdf",
              "static/dokuments/Aleksandr Pushkin. Suv parisi.pdf"]
    for i in kitob3:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Fyodor Dostoyevskiy"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Fedor Dostoyevskiy. Qimorboz (roman).pdf",
                 "static/dokuments/Fedor Dostoyevskiy. Qimorboz (roman) (2).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Mixail Bulgakov"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Mixail Bulgakov. Usta va Margarita (roman).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Chingiz Aytmatov"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Chingiz Aytmatov. Oqkema (qissa).pdf",
                 "static/dokuments/Chingiz Aytmatov. Bo'tako'z (qissa).pdf",
                 "static/dokuments/Kassandra tamg‘asi (oxirzamon) - Chingiz Aytmatov.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /chingizaytmatov__page2")


@dp.message_handler(text=["👤 Nodar Dumbadze"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Kukaracha.pdf",
                 "static/dokuments/Hislarimni qozgama.Nodar Dumbadze..pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Jek London"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Hayotga muhabbat (Jek London).pdf",
                 "static/dokuments/Jek London. Martin Iden (roman).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Gabriel Garsia Markes"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Ulug  onaning jazosi [@Elektron_kutubxona_kitoblarbot].pdf",
                 "static/dokuments/Gabriel Garsia Markes. Oshkora qotillik qissasi (qissa).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Alber Kamyu"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Alber Kamyu. Vabo (roman).pdf",
                 "static/dokuments/Alber Kamyu. Kaligula (pyesa).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Kobo Abe"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Qumdagi xotin.pdf",
                 "static/dokuments/Yashik odam (roman).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Lao She"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/@Elektron_Kutubxona-Mushuklar shahri.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Artur Konan Doyl"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/sh_xolms_hikoya.pdf",
                 "static/dokuments/Artur Konan Doyl. Baskervillar iti (qissa).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Agata Kristi"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/O`g`irlangan million dollar (Agata Kristi).pdf",
                 "static/dokuments/Ustasi faranglar (Agata Kristi).pdf",
                 "static/dokuments/Izquvar Puaro (Agata Kristi).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Gi De Mopassan"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Gi de Mopassan. Novellalar.pdf",
                 "static/dokuments/Gi de Mopassan. Azizim (roman).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Ernest Xeminguey"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Ernest Xeminguey. Dahshatli kutish (hikoya).docx",
                 "static/dokuments/Ernest Xeminguey. Ko‘prikdagi chol (hikoya).docx",
                 "static/dokuments/Ernest Xeminguey. Maestro bilan muloqot.docx"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Onor De Balzak"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/ONORE DE BALZAK- chin sevgi.pdf",
                 "static/dokuments/@Kutubxona_Olami-Gobsek.pdf",
                 "static/dokuments/@Kutubxona_Elektron-Dahriyning ibodati.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Jeyms Joys"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Jeyms_Joys_Musavvirning_yoshlikdagi.pdf",
                 "static/dokuments/Jeyms Joys. Uliss sarguzashtlari (roman).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Jonatan Svift"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Jonatan Svift. Gulliverning sayohatlari (roman).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Jyul Vern"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Jyul Vern - O'n besh yoshli kapitan (roman) .pdf",
                 "static/dokuments/Kapitan Grant bolalari.pdf",
                 "static/dokuments/Robinzonlar maktabi [@kitoblar1].pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Somerset Moem"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Somerset Moem-Oy va sariq chaqa (roman)[@Zokki_bot].pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Robindranat Tagor"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Robindranat Tagor_Halokat_.pdf",
                 "static/dokuments/Nur va soyalar (Robindranat Tagor).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["📚 Ertaklar"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/[@Elektron_kutubxona_kitoblarbot] Oltin beshik.pdf",
                 "static/dokuments/[@Elektron_kutubxona_kitoblarbot] O zbek xalq ertaklari.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["🤓 Qiziqarli kitoblar | Bolalar ensiklopediyasi"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/[@Elektron_kutubxona_kitoblarbot] Geografik kashfiyotlar.pdf",
                 "static/dokuments/[@Elektron_kutubxona_kitoblarbot] Dinozavrlar.pdf",
                 "static/dokuments/[@Elektron_kutubxona_kitoblarbot] Aviatsiya.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["📓 Boburnoma"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Boburnoma.pdf",
                 "static/dokuments/Boburnoma uchun qisqacha izohli lug'at (F.Ishoqov, 2008).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["📓 Shohnoma"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Abulqosim Firdavsiy. Shohnoma.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["📓 Zarbulmasal"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Gulxaniy. Zarbulmasal.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["📓 To'rt ulus tarixi"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/mirzo_ulugbek_4_ulus_tarixi_ziyouz_com.zip",
                 "static/dokuments/To'rt ulus tarixi - Mirzo Ulug'bek.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["📓 Devoni lug'otut turk"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Devoni lug'otut turk. 2-jild (Mahmud Koshg'ariy).pdf",
                 "static/dokuments/Devoni lug'otut turk. 3-jild (Mahmud Koshg'ariy).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["📓 Qutadg'u bilig"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Yusuf Xos Hojib. Qutadg'u bilig (nasriy bayoni).pdf",
                 "static/dokuments/Yusuf Xos Hojib. Qutadg'u bilig.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["💯 Top 100 kitoblar"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/100 kitob.txt"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["🗂 Pdf lug'atlar"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Koreyscha-o zbekcha(pdf).pdf",
                 "static/dokuments/Fransuzcha-o zbekcha(pdf).pdf",
                 "static/dokuments/Nemischa-o zbekcha(pdf).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["📲 Apk lug'atlar"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Ispancha-Ozbekcha.apk",
                 "static/dokuments/Inglizcha-o_zbekcha.apk",
                 "static/dokuments/Xitoycha-o zbekcha lug at(apk).apk"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["🌐 Google tarjimon"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Google Translator.apk"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Erkin Vohidov"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Erkin Vohidov. Qumursqalar jangi.pdf",
                 "static/dokuments/Erkin Vohidov. O'rtada begona yo'q.pdf",
                 "static/dokuments/Erkin Vohidov. Hozirgi yoshlar.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /erkinvohidov__page2")


@dp.message_handler(text=["👤 Abdulla Oripov"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Jannatga yo`l.pdf",
                 "static/dokuments/Abdulla Oripov-She'rlar.pdf"]
    kit = open("static/dokuments/")
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Rauf Parfi"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Rauf Parfi.pdf",
                 "static/dokuments/Rauf Parfi. Qaytish.pdf",
                 "static/dokuments/Rauf Parfi. Ona Turkiston.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Shavkat Rahmon"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Shavkat Rahmon. Saylanma.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["👤 Muhammad Yusuf"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Muhammad Yusuf. Ŏzingdan qŏymasin [@kitoblar1].pdf",
                 "static/dokuments/Muhammad Yusuf. Tanish teraklar [@kitoblar1].pdf",
                 "static/dokuments/Hayotga muhabbat (Jek London).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /muhammadyusuf__page2")


@dp.message_handler(text=["📜 Alisher Navoiy asarlari"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Alisher Navoiy. Mukammal asarlar to'plami. 1-jild.pdf",
                 "static/dokuments/Alisher Navoiy. Mukammal asarlar to'plami. 2-jild.pdf",
                 "static/dokuments/Alisher Navoiy. Lison ut-tayr.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /alishernavoiy__page2")


@dp.message_handler(text=["📜O'zbekiston Milliy Ensiklopediyasi"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/O'zbekiston Milliy Ensiklopediyasi - Ye harfi.pdf",
                 "static/dokuments/O'zbekiston Milliy Ensiklopediyasi - Yo harfi.pdf",
                 "static/dokuments/O'zbekiston Milliy Ensiklopediyasi - Z harfi.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /ensiklopediya__page2")


@dp.message_handler(text=["🔍 O'zbek tilining imlo lug'ati"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/X mi H (qisqacha imlo lug'ati).pdf",
                 "static/dokuments/Imlo qoidalari.pdf",
                 "static/dokuments/O'zbek tilining imlo lug'ati.apk"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Shavkat Mirziyoyev asarlari"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Ш.Мирзиёев  Танқидий таҳлил.apk",
                 "static/dokuments/Ш.Мирзиёев  Эркин ва Фаровон.apk",
                 "static/dokuments/Biografiya (Shavkat Mirziyoyev).txt"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Islom Karimov asarlari"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Islom_Karimov_Asarlar_2_jild_Bizdan.pdf",
                 "static/dokuments/Islom_Karimov_Asarlar_3_jild_Vatan.pdf",
                 "static/dokuments/Islom_Karimov_Asarlar_1_jild_O'zbekiston.pdf.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /islomkarimovasarlari__page2")


@dp.message_handler(text=["📒 Pdf kitoblar uchun"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/EBookDroid.apk",
                 "static/dokuments/pdf.reader.apk",
                 "static/dokuments/Adobe Reader.apk"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["📒 Djvu kitoblar uchun"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/EBookDroid.apk"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["📒 Epub kitoblar uchun"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/'Alreader.apk",
                 "static/dokuments/'FBReader.apk"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["📒 Zip kitoblar uchun"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Zip file reader.apk",
                 "static/dokuments/[@Elektron_kutubxona_kitoblarbot] Androzip.apk"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Tafsiri Hilol"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Tafsiri Hilol 1 juz.pdf",
                 "static/dokuments/Tafsiri Hilol 5 juz.pdf"]
    kit = open("static/dokuments/Tafsiri Hilol 6 juz.pdf")
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Jannat vasfi"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Jannat vasfi.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Keng rizq va baraka omillari"])
async def rus(message: types.Message):
    rus_kitob = []
    kit = open("static/dokuments/Keng rizq va baraka omillari.pdf")
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Istig'forning 40 xosiyati | Salovotlar"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Istig forning 40 xosiyati. Salovotlar.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Qur'on - qalblar shifosi"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Ziyovuddin Rahim. Qur'on - qalblar shifosi.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Baxtli hayot sari"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Baxtli hayot sari.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Payg'ambar uyida bir kun"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Payg'ambar uyida bir kun.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Shamoili Muhammadiy"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Imom Termiziy. Shamoili Muhammadiy.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Abu Bakr Siddiq"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Ahmad Lutfiy Qozonchi. Abu Bakr Siddiq.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Sunani Termiziy"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Sunani Termiziy.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Hazrati Umar ibn Xattob"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Ahmad Lutfiy Qozonchi. Hazrati Umar ibn Hattob (r.a.).pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Musnad"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Musnad. Imom A’zam Abu Hanifa.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Mukoshafat-ul qulub"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Mukoshafat-ul qulub.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Ramazon va taqvo"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Ramazon va taqvo.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["📗 1-sinf"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/Alifbe.apk",
                 "static/dokuments/matematika_1_uzb.pdf",
                 "static/dokuments/ona_tili_1_uzb.pdf",
                 "static/dokuments/yozuv_daftari_1_uzb.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /1sinf__page2")


@dp.message_handler(text=["📗 2-sinf"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/jismoniy_tarbiya_2_uzb.pdf",
                 "static/dokuments/rus_tili_2_uzb.pdf",
                 "static/dokuments/oqish_kitobi_2_uzb.pdf",
                 "static/dokuments/ona_tili_2_uzb.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /2sinf__page2")


@dp.message_handler(text=["📗 3-sinf"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/oqish_3_metodika.pdf",
                 "static/dokuments/texnologiya_3_uzb.pdf",
                 "static/dokuments/jismoniy_tarbiya_3_uzb.pdf",
                 "static/dokuments/tabiatshunoslik_3_rus.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /3sinf__page2")


@dp.message_handler(text=["📗 4-sinf"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/oqish_4_uzb.pdf",
                 "static/dokuments/rus_tili_4_uzb.pdf",
                 "static/dokuments/jismoniy_tarbiya_4_uzb.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /4sinf__page2")


@dp.message_handler(text=["📗 5-sinf"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/fransuz_tili_metodika_5_uzb.pdf",
                 "static/dokuments/botanika_5_uzb.pdf",
                 "static/dokuments/adabiyot_1qism_5_uzb.pdf",
                 "static/dokuments/adabiyot_2qism_5_uzb.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /5sinf__page2")


@dp.message_handler(text=["📗 7-sinf"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/fransuz_tili_metodika_7_uzb.pdf",
                 "static/dokuments/ingliz_tili_metodika_7_uzb.pdf",
                 "static/dokuments/algebra_7_uzb.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /7sinf__page2")


@dp.message_handler(text=["📗 6-sinf"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/fizika_6_uzb.pdf",
                 "static/dokuments/adabiyot_1qism_6_uzb.pdf",
                 "static/dokuments/adabiyot_2qism_6_uzb.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /6sinf__page2")


@dp.message_handler(text=["📗 8-sinf"])
async def rus(message: types.Message):
    rus_kitob = []
    kit = open("static/dokuments/")
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=[""])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/informatika_8_uzb.pdf",
                 "static/dokuments/ingliz_tili_8_metodika.pdf",
                 "static/dokuments/geometriya_8_uzb.pdf",
                 "static/dokuments/fransuz_tili_8_metodika.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /8sinf__page2")


@dp.message_handler(text=["📗 9-sinf"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/chizmachilik_9_uzb.pdf",
                 "static/dokuments/biologiya_9_uzb.pdf",
                 "static/dokuments/fransuz_tili_9_darslik.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /9sinf__page2")


@dp.message_handler(text=["📗 10-sinf"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/davlat_va_huquq_asoslari_10_uzb.pdf",
                 "static/dokuments/rus_tili_10_uzbqardosh.pdf",
                 "static/dokuments/adabiyot_10_uzb.pdf",
                 "static/dokuments/ingliz_tili_10_uzb.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /10sinf__page2")


@dp.message_handler(text=["📗 11-sinf"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/ona_tili_11_uzb.pdf",
                 "static/dokuments/jahon_tarixi_11_uzb.pdf",
                 "static/dokuments/ozbekiston_tarixi_11_uzb.pdf",
                 "static/dokuments/biologiya_11_uzb.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /11sinf__page2")


@dp.message_handler(text=["🇺🇿 Ona tili"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/ona_tili_11_uzb.pdf",
                 "static/dokuments/ona_tili_2_uzb.pdf",
                 "static/dokuments/ona_tili_1_uzb.pdf",
                 "static/dokuments/ona_tili_7_uzb.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /onatili__page2")


@dp.message_handler(text=["📚 Adabiyot"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/adabiyot_2qism_6_uzb.pdf",
                 "static/dokuments/adabiyot_1qism_6_uzb.pdf",
                 "static/dokuments/adabiyot_1qism_5_uzb.pdf",
                 "static/dokuments/adabiyot_7_uzb.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /adabiyot__page2")


@dp.message_handler(text=["🇬🇧 Ingliz tili"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/ingliz_tili_daftar_4_uzb.pdf",
                 "static/dokuments/ingliz_tili_daftar_4_uzb.pdf",
                 "static/dokuments/ingliz_tili_metodika_5_uzb.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /ingliztili__page2")


@dp.message_handler(text=["🇩🇪 Nemis tili"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/nemis_tili_metodika_5_uzb.pdf",
                 "static/dokuments/nemis_tili_3_uzb.pdf",
                 "static/dokuments/nemis_tili_daftar_2_uzb.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /nemistili__page2")


@dp.message_handler(text=["🇫🇷 Fransuz tili"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/fransuz_tili_metodika_5_uzb.pdf",
                 "static/dokuments/fransuz_tili_daftar_3_uzb.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /fransuztili__page2")


@dp.message_handler(text=["🇷🇺 Rus tili"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/rus_tili_10_uzbqardosh.pdf",
                 "static/dokuments/rus_tili_2_uzb.pdf",
                 "static/dokuments/rus_tili_4_uzb.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /rustili__page2")


@dp.message_handler(text=["🗺 Geografiya"])
async def rus(message: types.Message):
    rus_kitob = ["static/dokuments/geografiya_5_uzb.pdf",
                 "static/dokuments/geografiya_10_uzb.pdf",
                 "static/dokuments/geografiya_6_uzb.pdf"]
    for i in rus_kitob:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["🔬 Fizika"])
async def saj(message: types.Message):
    qand = ["static/dokuments/fizika_6_uzb.pdf",
            "static/dokuments/fizika_7_uzb.pdf",
            "static/dokuments/fizika_10_uzb.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["🔍 Tarix"])
async def saj(message: types.Message):
    qand = ["static/dokuments/jahon_tarixi_11_uzb.pdf",
            "static/dokuments/jahon_tarixi_10_uzb.pdf",
            "static/dokuments/Jahon_tarixi_8-sinf.apk"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /tarix__page2")


@dp.message_handler(text=["🔢 Matematika"])
async def saj(message: types.Message):
    qand = ["static/dokuments/matematika_1_uzb.pdf",
            "static/dokuments/algebra_7_uzb.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /matematika__page2")


@dp.message_handler(text=["🩺 Biologiya"])
async def saj(message: types.Message):
    qand = ["static/dokuments/botanika_5_uzb.pdf",
            "static/dokuments/biologiya_11_uzb.pdf",
            "static/dokuments/biologiya_9_uzb.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["🌡 Kimyo"])
async def saj(message: types.Message):
    qand = ["static/dokuments/kimyo_7_uzb.pdf",
            "static/dokuments/kimyo_8_uzb.pdf",
            "static/dokuments/kimyo_9_uzb.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["🏃‍♂ Jismoniy tarbiya"])
async def saj(message: types.Message):
    qand = ["static/dokuments/jismoniy_tarbiya_3_uzb.pdf",
            "static/dokuments/jismoniy_tarbiya_4_uzb.pdf",
            "static/dokuments/jismoniy_tarbiya_2_uzb.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["📙 1-sinf"])
async def saj(message: types.Message):
    qand = ["static/dokuments/Alifbe.apk",
            "static/dokuments/odobnoma_1_rus.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /1sinfru__page2")


@dp.message_handler(text=["📙 2-sinf"])
async def saj(message: types.Message):
    qand = ["static/dokuments/odobnoma_2_rus.pdf",
            "static/dokuments/matematika_2_rus.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /2sinfru__page2")


@dp.message_handler(text=["📙 3-sinf"])
async def saj(message: types.Message):
    qand = ["static/dokuments/tabiatshunoslik_3_rus.pdf",
            "static/dokuments/rus_tili_3_rus.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /3sinfru__page2")


@dp.message_handler(text=["📙 4-sinf"])
async def saj(message: types.Message):
    qand = ["static/dokuments/rus_tili_4_rus.pdf",
            "static/dokuments/oqish_kitobi_4_rus.pdf",
            "static/dokuments/oqish_metodika_4_rus.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /4sinfru__page2")


@dp.message_handler(text=["📙 5-sinf"])
async def saj(message: types.Message):
    qand = ["static/dokuments/musiqa_5_rus.pdf",
            "static/dokuments/mehnat_5_rus.pdf",
            "static/dokuments/adabiyot_5_rus.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /5sinfru__page2")


@dp.message_handler(text=["📙 6-sinf"])
async def saj(message: types.Message):
    qand = ["static/dokuments/matematika_6_rus.pdf",
            "static/dokuments/ingliz_tili_metodika_6_rus.pdf",
            "static/dokuments/geografiya_6_rus.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /6sinfru__page2")


@dp.message_handler(text=["📙 7-sinf"])
async def saj(message: types.Message):
    qand = ["static/dokuments/adabiyot_7_rus.pdf",
            "static/dokuments/fizika_7_rus.pdf",
            "static/dokuments/algebra_7_rus.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /7sinfru__page2")


@dp.message_handler(text=["📙 8-sinf"])
async def saj(message: types.Message):
    qand = ["static/dokuments/informatika_8_rus.pdf",
            "static/dokuments/milliy_goya_8_rus.pdf",
            "static/dokuments/geometriya_8_rus.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /8sinfru__page2")


@dp.message_handler(text=["📙 9-sinf"])
async def saj(message: types.Message):
    qand = ["static/dokuments/milliy_goya_9_rus.pdf",
            "static/dokuments/ozbek_tili_9_rus.pdf",
            "static/dokuments/rus_tili_9_rus.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /9sinfru__page2")


@dp.message_handler(text=["📙 10-sinf"])
async def saj(message: types.Message):
    qand = ["static/dokuments/dunyo_dinlari_tarixi_10_rus.pdf",
            "static/dokuments/geografiya_10_rus.pdf",
            "static/dokuments/davlat_va_huquq_asoslari_10_rus.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /10sinfru__page2")


@dp.message_handler(text=["📙 11-sinf"])
async def saj(message: types.Message):
    qand = ["static/dokuments/[@ABTbooks] dunyo_dinlari_tarixi_11_rus.pdf",
            "static/dokuments/[@ABTbooks] adabiyot_1qism_11_rus.pdf",
            "static/dokuments/[@ABTbooks] adabiyot_2qism_11_rus.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /11sinfru__page2")


@dp.message_handler(text=["Abdulla Qodiriy - Otkan kunlar"])
async def saj(message: types.Message):
    qand = ["static/dokuments/05. Oʻtkan kunlar @audiokitob_ulashamiz.mp3",
            "static/dokuments/06. Oʻtkan kunlar @audiokitob_ulashamiz.mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /otkankunlar__page2")


@dp.message_handler(text=["Abdulla Qodiriy - Mehrobdan chayon"])
async def saj(message: types.Message):
    qand = ["static/dokuments/03. Mehrobdan chayon.mp3",
            "static/dokuments/04. Mehrobdan chayon.mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /mehrobdanchayon__page2")


@dp.message_handler(text=["Oybek - Navoiy"])
async def saj(message: types.Message):
    qand = ["static/dokuments/10. Navoiy @audiokitob_ulashamiz.mp3",
            "static/dokuments/07. Navoiy @audiokitob_ulashamiz.mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /navoiyromani__page2")


@dp.message_handler(text=["Pirimqul Qodirov - Yulduzli tunlar"])
async def saj(message: types.Message):
    qand = ["static/dokuments/08. Yulduzli tunlar @audiokitob_ulashamiz.mp3",
            "static/dokuments/09. Yulduzli tunlar @audiokitob_ulashamiz.mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /yulduzlitunlar__page2")


@dp.message_handler(text=["Said Ahmad - Ufq"])
async def saj(message: types.Message):
    qand = ["static/dokuments/06. Ufq (trilogiya).mp3",
            "static/dokuments/09. Ufq (trilogiya).mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /ufq__page2")


@dp.message_handler(text=["Tohir Malik - Shaytanat"])
async def saj(message: types.Message):
    qand = ["static/dokuments/02. Shaytanat @audibleuzb.mp3,"
            "static/dokuments/03. Shaytanat @audibleuzb.mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /shaytanat__page2")


@dp.message_handler(text=["Cho'lpon - Kecha va kunduz"])
async def saj(message: types.Message):
    qand = ["static/dokuments/06. Kecha va kunduz.mp3",
            "static/dokuments/08. Kecha va kunduz.mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /kechavakunduz__page2")


@dp.message_handler(text=["G'afur G'ulom - Shum bola"])
async def saj(message: types.Message):
    qand = ["static/dokuments/04. Shum bola @audibleuzb.mp3",
            "static/dokuments/Shum bola @audibleuzb.pdf"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Tog'ay Murod - Yulduzlar mangu yonadi"])
async def saj(message: types.Message):
    qand = ["static/dokuments/09. Yulduzli tunlar @audiokitob_ulashamiz.mp3",
            "static/dokuments/08. Yulduzli tunlar @audiokitob_ulashamiz.mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["Tohir Malik - Alvido bolalik"])
async def saj(message: types.Message):
    qand = ["static/dokuments/09. Alvido, bolalik @audiokitob_ulashamiz.mp3",
            "static/dokuments/10. Alvido, bolalik @audiokitob_ulashamiz.mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["O'tkir Hoshimov - Dunyoning ishlari"])
async def saj(message: types.Message):
    qand = ["static/dokuments/09. Dunyoning ishlari @audiokitob_ulashamiz.mp3",
            "static/dokuments/10. Dunyoning ishlari @audiokitob_ulashamiz.mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /dunyoningishlari__page2")


@dp.message_handler(text=["Hikoyalar"])
async def saj(message: types.Message):
    qand = ["static/dokuments/Abdulla Qahhor - Ming bir jon (hikoya).mp3",
            "static/dokuments/Abdulla Qahhor - O g ri (hikoya).mp3",
            "static/dokuments/O tkir Hoshimov - Urushning so nggi qurboni (hikoya).mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /hikoyalar__page2")


@dp.message_handler(text=["🌐 Hikoyalar"])
async def saj(message: types.Message):
    qand = ["static/dokuments/qopqon-j.london asari.mp3",
            "static/dokuments/Chaqaloq @audiokitob_ulashamiz.mp3",
            "static/dokuments/Buqalamun.mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
    await message.answer("Keyingi sahifa: /hikoyalarjahon__page2")


@dp.message_handler(text=['Chingiz Aytmatov - "Jamila"'])
async def saj(message: types.Message):
    qand = ["static/dokuments/05. Jamila @audiokitob_ulashamiz.mp3",
            "static/dokuments/08. Jamila @audiokitob_ulashamiz.mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=['Chingiz Aytmatov - "Chingizxonning oq buluti"'])
async def saj(message: types.Message):
    qand = ["static/dokuments/10. Alkimyogar @audiokitob_ulashamiz.mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=["O'nta negir bolasi"])
async def saj(message: types.Message):
    qand = ["static/dokuments/06. Oʻnta negr bolasi @audiokitob_ulashamiz.mp3",
            "static/dokuments/10. Oʻnta negr bolasi @audiokitob_ulashamiz.mp3",
            "static/dokuments/07. Oʻnta negr bolasi @audiokitob_ulashamiz.mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
        await message.answer("Keyingi sahifa: /ontanegirbolasi__page2")


@dp.message_handler(text=['Dengiz sarguzashtlari'])
async def saj(message: types.Message):
    qand = ["static/dokuments/08. Dengiz sarguzashtlari @audiokitob_ulashamiz.mp3",
            "static/dokuments/09. Dengiz sarguzashtlari @audiokitob_ulashamiz.mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))


@dp.message_handler(text=['Graf Monte Kristo'])
async def saj(message: types.Message):
    qand = ["static/dokuments/001. Graf Monte Kristo @audiokitob_ulashamiz.mp3",
            "static/dokuments/002. Graf Monte Kristo @audiokitob_ulashamiz.mp3"]
    for i in qand:
        await message.answer_document(open(i, 'rb'))
        await message.answer("Keyingi sahifa: /grafmontekristo__page2")


@dp.message_handler(text=["Romanlar"])
async def ans(message: types.Message):
    await message.answer("Tanlang 👇!", reply_markup=roman_btn)


@dp.message_handler(text=["Hikoyala"])
async def ans(message: types.Message):
    await message.answer("Tanlang 👇!", reply_markup=qissa_btn)


@dp.message_handler(text=["🌐 Romanlar"])
async def ans(message: types.Message):
    await message.answer("Tanlang 👇!", reply_markup=rroman_btn)


@dp.message_handler(text=["🌐 Qissalar"])
async def ans(message: types.Message):
    await message.answer("Tanlang 👇!", reply_markup=rqissa_btn)


@dp.message_handler(text=["ortga"])
async def ans(message: types.Message):
    await message.answer("Tanlang! 👇",reply_markup=rus_btn)


@dp.message_handler(text=["GO Back"])
async def ans(message: types.Message):
    await message.answer("Sizga qaysi janrdagi audio kitoblar kerak? Tanlang! 👇",reply_markup=uzb_btn)


@dp.message_handler(text=["🇷🇺 Ruscha"])
async def rus(message: types.Message):
    await message.answer("Sizga qaysi janrdagi audio kitoblar kerak? Tanlang! 👇",reply_markup=uzb_btn)


@dp.message_handler(text=["orqaga"])
async def orq(message: types.Message):
    await message.answer("Tanlang! 👇", reply_markup=mak_btn)


@dp.message_handler(text=["Go Back"])
async def ans(message: types.Message):
    await message.answer("Asosiy menyu!", reply_markup=start_btn)


# @dp.message_handler(text=["English"])
# async def sa(message: types.Message):
#     await message.answer("rus")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)