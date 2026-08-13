def banner_builder(word):
    lenght = len(word) +8
    print("="*(lenght))
    print(word.center(lenght))
    print("="*(lenght))
banner_builder("Hello Folks")