from captcha.image import ImageGen
from io import BytesIO


def main():
    text = 'HELLO!'

    captcha = ImageCaptcha(width=400,
                           height=220,
                           fonts=['SF-Pro',
                                  'SF-Compact-Rounded-Black',
                                  'SF-Pro-Display-UltralightItalic',
                                  'Neoneon'],
                            font_sizes=(40, 70, 100))  # NOQA: Type hint was wrong
    
    captcha.write(text, 'fake_captcha.png')


if __name__ == '__main__':
    main()
