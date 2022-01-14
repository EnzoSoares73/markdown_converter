import pytest

from main import markdown_converter

def test_if_signals_are_not_converted_inside_code_signals():
    text = "`" \
           "###--Código qualquer--###" \
           "flkajsdçlfkjaklçsdf" \
           "`"

    converted_text: str = markdown_converter(text)
    assert converted_text.find("###--")
    assert converted_text.find("--###")

def test_if_empty_keys_raise_errors():
    with pytest.raises(ValueError) as excinfo:
        text = "`" \
               "###--Código qualquer--###" \
               "flkajsdçlfkjaklçsdf" \
               "`"

        signals = {
            'test_signal': {
                '': {
                    'test': ''
                }
            }
        }

        markdown_converter(text, signals)
        assert "Signal has empty key" in str(excinfo.value)

def test_if_num_keys_different_from_1():
    with pytest.raises(ValueError, match='1 expected'):
        signals = {
            'test_signal': {
            }
        }
        markdown_converter("", signals)