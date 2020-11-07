class FourDigitYearConverter:
    regex = '[0-9]{5}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return value
