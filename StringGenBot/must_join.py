from env import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(photo="https://telegra.ph/file/f698f60484b7aef0d6f29.jpg", caption=f"↯︙ عـݪـيك اެݪاެشـتراެك فـي قـنـاެة اެݪـبـوت 📻 .\n↯︙يوزر القناة ( {link} ) .",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("اضغط هنا للاشتراك💤", url=f"{link}")]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"ارفعني ادمن يعم في قناه او جروب الاشتراك الاجباري : {MUST_JOIN} !")
