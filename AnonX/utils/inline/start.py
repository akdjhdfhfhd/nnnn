from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"",
            ),
            InlineKeyboardButton(
                text=_["S_B_S"], callback_data="amm"
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], callback_data="settings_helper"
            ),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                ),
                InlineKeyboardButton(

                    text=_["S_B_9"], url=f"https://t.me/so_alfaa"

                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                    )
                ]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_8"], callback_data="settings_back_helper"
            )
        ]
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                    )
                ]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )
    if GITHUB_REPO and OWNER:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_7"], user_id=OWNER),
                InlineKeyboardButton(
                    text=_["S_B_6"], url=f"{GITHUB_REPO}"
                ),
            ]
        )
    else:
        if GITHUB_REPO:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_6"], url=f"{GITHUB_REPO}"
                    ),
                ]
            )
        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_11"], url=f"https://t.me/NvvvC"
                    ),
                    InlineKeyboardButton(

                        text=_["S_B_12"], url=f"https://t.me/NvvvM"

                    ),
                ]
            )
        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_7"], user_id=OWNER
                    ),
                    InlineKeyboardButton(

                        text=_["S_B_10"], url=f"https://t.me/so_alfaa"

                    ),
                ]
            )
    buttons.append(
        [InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG")]
    )
    return buttons





  
  
REPLY_MESSAGE = "- اهلين ياعيني عندك الازرار تحت استمتع"

REPLY_MESSAGE_BUTTONS = [
         [
             ("طريقة تشغيل ميرا"),                   
             ("اوامر ميرا")

          ],
          [
             ("المطور"),
             ("السورس")
          ],
          [
             ("اخفاء الازرار")
          ]
]

