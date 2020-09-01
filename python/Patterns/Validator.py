import re
import datetime


class Validator:
    def validate(self, value: str) -> str:
        return ""


class DateVal(Validator):
    def validate(self, value: str) -> str:
        """
        >>> DateVal().validate(value="bad")
        'MALFORMED: bad'

        >>> DateVal().validate(value="2/2/2")
        'MALFORMED: 2/2/2'

        >>> DateVal().validate(value="02/02/2020")
        ''
        """
        result = ""
        try:
            datetime.datetime.strptime(value, '%m/%d/%Y').date()
        except ValueError:
            result = "MALFORMED: " + str(value)
        return result


if __name__ == "__main__":
    val = DateVal()

    print("Test: " + val.validate("baddate"))

    pass
