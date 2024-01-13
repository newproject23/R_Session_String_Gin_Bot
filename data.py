from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("↯︙ انشاء كود بايروجرام .", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("↯︙المطور .", url="https://t.me/j_s_9"),
        ],

        [InlineKeyboardButton("↯︙المطور .", url="https://t.me/vip_alpop"),
        ],

        [InlineKeyboardButton("↯︙السورس .", url="https://t.me/source_alpop"),
        ],

        [InlineKeyboardButton("↯︙جروب الدعم .", url="https://t.me/bar_alpop"),
        ],
    ]

    START = """
↯︙اهلا بك في بوت انشاء كود بايروجرام .

↯︙ يمكنك انشاء كود بايروجرام بسهولة .

↯︙يتم ارسال الكود في الرسائل المحفوضة .
    """
