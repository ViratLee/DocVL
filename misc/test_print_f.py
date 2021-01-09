def headline(text, border="♦", *, width=50):
    return f" {text} ".center(width, border)
if __name__ == '__main__':
    print(headline('Positional-only Arguments'))