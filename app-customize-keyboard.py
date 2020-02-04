# 

actions = {
  {'New...': 'Choose layout: Blank, US, ISO, 60%, 40%, Ergonomic, Number Pad'}
}

menu_bar = [
  {'App', ['New...', 'Open...', 'Save', 'Save...', 'Export...', 'Exit']},
  {'', []},
  {'', []}
]

app_layout = [
    [menu_bar],
    [main_content],
    [status_bar]
]

choose_key_size_layout = [
    [key_1x1, key_1.5x1, key_2x1, key_3x1, key_1x0.5, key_1x2]
]


def show_app():
    print('show_app()')


def main():
    print('main()')


if __name__ == '__main__':
    main()
