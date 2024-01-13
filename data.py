from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("↯︙ انشاء جلسه .", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("↯︙𝑀𝐴𝑅𝑂 .", url="https://t.me/j_s_9"),
        ],

        [InlineKeyboardButton("↯︙𝐴𝐿𝑃𝑂𝑃 .", url="https://t.me/vip_alpop"),
        ],

        [InlineKeyboardButton("↯︙𝑆𝑂𝐔𝑅𝐶𝐸 𝐴𝐿𝑃𝑂𝑃 .", url="https://t.me/source_alpop"),
        ],

        [InlineKeyboardButton("↯︙𝐺𝑅𝑂𝐔𝑃 .", url="https://t.me/bar_alpop"),
        ],
    ]

    START = """
↯︙اهلا بك في بوت انشاء الجلسات .

↯︙ يمكنك انشاء كود بايروجرام بسهولة .

↯︙يتم ارسال الكود في الرسائل المحفوضة .
    """
