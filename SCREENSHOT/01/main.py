import pyscreenshot as ImageGrab

def main():
    imagem = ImageGrab.grab()
    imagem.save('screenShot1.png', 'PNG')

if __name__ == "__main__":
    main()