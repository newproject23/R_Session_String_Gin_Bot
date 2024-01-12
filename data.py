from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("↯︙ انشاء كود بايروجرام .", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("↯︙المطور .", url="https://t.me/j_s_9"),
        ],

        [InlineKeyboardButton("↯︙المطور .", url="https://t.me/j_s_9"),
        ],
    ]

    START = """
↯︙اهلا بك في بوت انشاء كود بايروجرام .

↯︙ يمكنك انشاء كود بايروجرام بسهولة .

↯︙يتم ارسال الكود في الرسائل المحفوضة .
    """
