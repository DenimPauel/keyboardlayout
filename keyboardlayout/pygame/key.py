from keyboardlayout.key import Key
from keyboardlayout.common import LayoutName

import pygame


__MAPPING_BASE = {
    pygame.K_BACKQUOTE: Key.BACKQUOTE,
    pygame.K_EQUALS: Key.EQUALS,
    pygame.K_BACKSPACE: Key.BACKSPACE,
    pygame.K_TAB: Key.TAB,
    pygame.K_q: Key.Q,
    pygame.K_w: Key.W,
    pygame.K_e: Key.E,
    pygame.K_r: Key.R,
    pygame.K_t: Key.T,
    pygame.K_y: Key.Y,
    pygame.K_u: Key.U,
    pygame.K_i: Key.I,
    pygame.K_o: Key.O,
    pygame.K_p: Key.P,
    pygame.K_LEFTBRACKET: Key.LEFTBRACKET,
    pygame.K_RIGHTBRACKET: Key.RIGHTBRACKET,
    pygame.K_BACKSLASH: Key.BACKSLASH,
    pygame.K_CAPSLOCK: Key.CAPSLOCK,
    pygame.K_a: Key.A,
    pygame.K_s: Key.S,
    pygame.K_d: Key.D,
    pygame.K_f: Key.F,
    pygame.K_g: Key.G,
    pygame.K_h: Key.H,
    pygame.K_j: Key.J,
    pygame.K_k: Key.K,
    pygame.K_l: Key.L,
    pygame.K_SEMICOLON: Key.SEMICOLON,
    pygame.K_QUOTE: Key.SINGLEQUOTE,
    pygame.K_RETURN: Key.RETURN,
    pygame.K_LSHIFT: Key.LEFT_SHIFT,
    pygame.K_z: Key.Z,
    pygame.K_x: Key.X,
    pygame.K_c: Key.C,
    pygame.K_v: Key.V,
    pygame.K_b: Key.B,
    pygame.K_n: Key.N,
    pygame.K_m: Key.M,
    pygame.K_COMMA: Key.COMMA,
    pygame.K_PERIOD: Key.PERIOD,
    pygame.K_SLASH: Key.FORWARDSLASH,
    pygame.K_RSHIFT: Key.RIGHT_SHIFT,
    pygame.K_LCTRL: Key.LEFT_CONTROL,
    pygame.K_LMETA: Key.LEFT_META,
    pygame.K_LALT: Key.LEFT_ALT,
    pygame.K_SPACE: Key.SPACE,
    pygame.K_RALT: Key.RIGHT_ALT,
    pygame.K_RMETA: Key.RIGHT_META,
    1073741925: Key.CONTEXT_MENU,
    pygame.K_RCTRL: Key.RIGHT_CONTROL,
    pygame.K_UP: Key.UP_ARROW,
    pygame.K_DOWN: Key.DOWN_ARROW,
    pygame.K_LEFT: Key.LEFT_ARROW,
    pygame.K_RIGHT: Key.RIGHT_ARROW,
    pygame.K_COLON: Key.COLON,
    pygame.K_EXCLAIM: Key.EXCLAMATION,
    249: Key.U_GRAVE,
    pygame.K_CARET: Key.CARET,
    pygame.K_DOLLAR: Key.DOLLAR,
    pygame.K_ASTERISK: Key.ASTERISK,
    pygame.K_LESS: Key.LESSTHAN,
    pygame.K_RIGHTPAREN: Key.RIGHTPAREN,
    pygame.K_EQUALS: Key.EQUALS,
}

KEY_MAP_BY_LAYOUT = {
    LayoutName.QWERTY: {
        **{
            pygame.K_1: Key.DIGIT_1,
            pygame.K_2: Key.DIGIT_2,
            pygame.K_3: Key.DIGIT_3,
            pygame.K_4: Key.DIGIT_4,
            pygame.K_5: Key.DIGIT_5,
            pygame.K_6: Key.DIGIT_6,
            pygame.K_7: Key.DIGIT_7,
            pygame.K_8: Key.DIGIT_8,
            pygame.K_9: Key.DIGIT_9,
            pygame.K_0: Key.DIGIT_0,
            pygame.K_MINUS: Key.MINUS,
        },
        **__MAPPING_BASE,
    },
    LayoutName.AZERTY_LAPTOP: {
        **{
            pygame.K_1: Key.AMPERSAND,
            pygame.K_2: Key.E_ACUTE,
            pygame.K_3: Key.DOUBLEQUOTE,
            pygame.K_4: Key.SINGLEQUOTE,
            pygame.K_5: Key.LEFTPAREN,
            pygame.K_6: Key.MINUS,
            pygame.K_7: Key.E_GRAVE,
            pygame.K_8: Key.UNDERSCORE,
            pygame.K_9: Key.C_CEDILLE,
            pygame.K_0: Key.A_GRAVE,
            pygame.K_MINUS: Key.RIGHTPAREN,
        },
        **__MAPPING_BASE,
    },
    LayoutName.QWERTYJPN106: {
        **{
            pygame.K_1: Key.DIGIT_1,
            pygame.K_2: Key.DIGIT_2,
            pygame.K_3: Key.DIGIT_3,
            pygame.K_4: Key.DIGIT_4,
            pygame.K_5: Key.DIGIT_5,
            pygame.K_6: Key.DIGIT_6,
            pygame.K_7: Key.DIGIT_7,
            pygame.K_8: Key.DIGIT_8,
            pygame.K_9: Key.DIGIT_9,
            pygame.K_0: Key.DIGIT_0,
            pygame.K_MINUS: Key.MINUS,
            # added --->>>
            pygame.K_AT: Key.AT,                    # @ mark
            # \ : U+005C 逆Solidus 半角￥は、U+00A5 decimalだと 165
            pygame.KSCAN_NONUSBACKSLASH: Key.YEN,   # yen対応  （調査中）
            #pygame.KSCAN_BACKSLASH: Key.YEN,   # yen対応 （調査中）
            #165: Key.XXXX,   #0xA5
            #キーマップ関連の情報
            # http://web.yl.is.s.u-tokyo.ac.jp/~hedkandi/camera/keymap.py
            # PygameのあるボタンのKeyコマンドがわからない。
            # https://teratail.com/questions/319347
            # 半角/全角キー押下時、key値は96 (K_BACKQUOTE)です。英語キーで ` がある位置だからか？
            # 
            #if event.type == pygame.KEYDOWN:
            #    if event.scancode == 121:
            #        print("変換")
            #    elif event.scancode == 41: #0x29
            #        print("半角/全角")
            #
            # added <<<---
        },
        **__MAPPING_BASE,
	},

}
