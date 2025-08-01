from telegram import InlineKeyboardButton
from ptb.callbacks import CallbackData, CallbackName
from enum import Enum, auto


class ButtonName(Enum):
    TOS = auto()
    FAQ = auto()
    ORDER_STORAGE = auto()
    MY_ACCOUNT = auto()
    MY_ORDERS = auto()
    TOS_DOWNLOAD = auto()
    BACK_TO_MENU = auto()
    FORBIDDEN = auto()
    COURIER_DELIVERY = auto()
    COURIER_DELIVERY_YES = auto()
    SELF_DELIVERY = auto()
    PPD_YES = auto()
    PPD_NO = auto()
    PPD_DOWNLOAD = auto()
    HAND_OVER_THINGS = auto()
    SIGNUP = auto()
    CONFIRM_SIGNUP = auto()
    CHANGE_PERSONAL_DATA = auto()
    SHOW_PRICES = auto()
    NO_PROMO = auto()
    CONFIRM_RENT = auto()
    OPEN_QR = auto()
    ADD_THINGS = auto()
    REMOVE_THINGS = auto()


BUTTONS = {
    ButtonName.REMOVE_THINGS: InlineKeyboardButton(
      'Забрать вещи',
      callback_data=CallbackData(CallbackName.REMOVE_ITEMS).to_str()
    ),
    ButtonName.ADD_THINGS: InlineKeyboardButton(
      'Положить вещи',
      callback_data=CallbackData(CallbackName.PUT_NEW_ITEMS).to_str()
    ),
    ButtonName.OPEN_QR: InlineKeyboardButton(
        'Получить QR для открытия',
        callback_data=CallbackData(CallbackName.OPEN_QR).to_str()
    ),
    ButtonName.CONFIRM_RENT: InlineKeyboardButton(
        'Подтвердить аренду',
        callback_data=CallbackData(CallbackName.CONFIRM_BOX_RENT).to_str()
    ),
    ButtonName.NO_PROMO: InlineKeyboardButton(
        'Нет промокода',
        callback_data=CallbackData(CallbackName.NO_PROMO).to_str()
    ),
    ButtonName.COURIER_DELIVERY_YES: InlineKeyboardButton(
        'Подтвердить',
        callback_data=CallbackData(CallbackName.CREATE_COURIER_DELIVERY_REQUEST).to_str()
    ),
    ButtonName.MY_ACCOUNT: InlineKeyboardButton(
        'Личный кабинет',
        callback_data=CallbackData(CallbackName.MY_ACCOUNT).to_str()
    ),
    ButtonName.SHOW_PRICES: InlineKeyboardButton(
        'Показать расценки',
        callback_data=CallbackData(CallbackName.SHOW_PRICES).to_str()
    ),
    ButtonName.TOS: InlineKeyboardButton(
        'Условия хранения/FAQ',
        callback_data=CallbackData(CallbackName.TERMS_OF_SERVICE).to_str()
    ),
    ButtonName.FAQ: InlineKeyboardButton(
        'Частые вопросы',
        callback_data=CallbackData(CallbackName.FAQ).to_str()
    ),
    ButtonName.ORDER_STORAGE: InlineKeyboardButton(
        'Заказать ячейку',
        callback_data=CallbackData(CallbackName.ORDER_STORAGE).to_str()
    ),
    ButtonName.MY_ORDERS: InlineKeyboardButton(
        'Мои заказы',
        callback_data=CallbackData(CallbackName.MY_ORDERS).to_str()
    ),
    ButtonName.TOS_DOWNLOAD: InlineKeyboardButton(
        'Скачать условия',
        callback_data=CallbackData(CallbackName.DOWNLOAD_TOS).to_str()
    ),
    ButtonName.BACK_TO_MENU: InlineKeyboardButton(
        'В главное меню',
        callback_data=CallbackData(CallbackName.MAIN_MENU).to_str()
    ),
    ButtonName.FORBIDDEN: InlineKeyboardButton(
        'Запрещенные к хранению вещества',
        callback_data=CallbackData(CallbackName.FORBIDDEN_TO_STORE).to_str()
    ),
    ButtonName.COURIER_DELIVERY: InlineKeyboardButton(
        'Вывоз курьером',
        callback_data=CallbackData(CallbackName.COURIER_DELIVERY).to_str()
    ),
    ButtonName.SELF_DELIVERY: InlineKeyboardButton(
        'Привезу сам',
        callback_data=CallbackData(CallbackName.SELECT_WAREHOUSE).to_str()
        ),
    ButtonName.PPD_YES: InlineKeyboardButton(
        'Да',
        callback_data=CallbackData(CallbackName.INPUT_FULL_NAME).to_str()
    ),
    ButtonName.PPD_NO: InlineKeyboardButton(
        'Нет',
        callback_data=CallbackData(CallbackName.MAIN_MENU).to_str()
    ),
    ButtonName.PPD_DOWNLOAD: InlineKeyboardButton(
        'Скачать полную версию',
        callback_data=CallbackData(CallbackName.DOWNLOAD_PPD).to_str()
    ),
    ButtonName.HAND_OVER_THINGS: InlineKeyboardButton('Сдать вещи', callback_data='hand_over_things'),
    ButtonName.SIGNUP: InlineKeyboardButton(
        'Зарегистрироваться',
        callback_data=CallbackData(CallbackName.PERSONAL_DATA_AGREEMENT).to_str()
    ),
    ButtonName.CONFIRM_SIGNUP: InlineKeyboardButton(
        'Подтвердить регистрацию',
        callback_data=CallbackData(CallbackName.SIGN_UP).to_str()
    ),
    ButtonName.CHANGE_PERSONAL_DATA: InlineKeyboardButton(
        'Ввести данные заново',
        callback_data=CallbackData(CallbackName.PERSONAL_DATA_AGREEMENT).to_str()
    )
}
