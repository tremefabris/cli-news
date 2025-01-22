
class Color:
    
    @staticmethod
    def color(text, color):
        color = color.lower()

        if color not in ["red", "green", "grn", "blue", "blu", "yellow", "ylw"]:
            raise ValueError(
                "`color` argument must be one of `red`, `green`, `grn`, `blue`, `blu`, `yellow`, `ylw`"
            )


        ESC_CODES = {
            "RED": "\033[91m",
            "GRN": "\033[92m",
            "YLW": "\033[93m",
            "BLU": "\033[94m",
            "RST": "\033[0m"
        }

        if color in ["red"]:
            text = f"{ESC_CODES['RED']}{text}{ESC_CODES['RST']}"
        elif color in ["green", "grn"]:
            text = f"{ESC_CODES['GRN']}{text}{ESC_CODES['RST']}"
        elif color in ["yellow", "ylw"]:
            text = f"{ESC_CODES['YLW']}{text}{ESC_CODES['RST']}"
        elif color in ["blue", "blu"]:
            text = f"{ESC_CODES['BLU']}{text}{ESC_CODES['RST']}"

        return text


    @staticmethod
    def red(text):
        return f"\033[91m{text}\033[0m"
    
    @staticmethod
    def green(text):
        return f"\033[92m{text}\033[0m"
    
    @staticmethod
    def blue(text):
        return f"\033[94m{text}\033[0m"
    
    @staticmethod
    def yellow(text):
        return f"\033[93m{text}\033[0m"
