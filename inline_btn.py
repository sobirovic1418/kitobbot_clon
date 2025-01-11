from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

kanal_ibtn=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="guruh",callback_data="mushuk"),
            InlineKeyboardButton(text="guruh1",callback_data="ot")
        ],
        [
            InlineKeyboardButton(text="guruh2",callback_data="kuchuk")
        ],
        [
            InlineKeyboardButton(text="guruh3",callback_data="sigir"),
            InlineKeyboardButton(text="guruh4",callback_data="sigir")
        ]
    ]
)

aloqa_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="contakt",request_contact=True),
            KeyboardButton(text="location",request_location=True)
        ]
    ]
)
