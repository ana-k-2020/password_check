import urwid


def is_very_long(password):
    return len(password) > 12


def has_digits(password):
    return any(n.isdigit() for n in str(password))


def has_letters(password):
    return any(i.isalpha() for i in str(password))


def has_upper_letters(password):
    return any(l.isupper() for l in str(password))


def has_lower_letters(password):
    return any(l.islower() for l in str(password))


def has_symbols(password):
    return any(not l.isdigit() and not l.isalpha() for l in str(password))


def on_ask_change(edit, password):
    score = 0
    to_check = [
        is_very_long(password),
        has_letters(password),
        has_upper_letters(password),
        has_digits(password),
        has_lower_letters(password),
        has_symbols(password),
    ]
    for item in to_check:
        if item:
            score += 2
    check.set_text('Рейтинг пароля: %s' % score)


if __name__ == '__main__':
    password = urwid.Edit('Введите пароль: ')
    check = urwid.Text('')
    menu = urwid.Pile([password, check])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(password, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
