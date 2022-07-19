from shirtificate import generate_shirtificate

def test_generate_shirtificate_invalid_name_raises_valueerror():
    try:
        generate_shirtificate('', '1.pdf')
    except ValueError:
        pass
    else:
        raise AssertionError('ValueError was expected.')

    try:
        generate_shirtificate(None, '1.pdf')
    except ValueError:
        return
    raise AssertionError('ValueError was expected.')

def test_generate_shirtificate_invalid_file_path_raises_valueerror():
    try:
        generate_shirtificate('Olesia', '')
    except ValueError:
        pass
    else:
        raise AssertionError('ValueError was expected.')

    try:
        generate_shirtificate('Olesia', None)
    except ValueError:
        return
    raise AssertionError('ValueError was expected.')

def test_generate_shirtificate_file_path_is_not_pdf_file_raises_valueerror():
    try:
        generate_shirtificate('Olesia', '1')
    except ValueError:
        pass
    else:
        raise AssertionError('ValueError was expected.')

    try:
        generate_shirtificate('Olesia', 'output.pdfa')
    except ValueError:
        return
    raise AssertionError('ValueError was expected.')
