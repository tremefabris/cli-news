from .color import Color as C


class Log():

    OK = 0
    WARNING = 1
    ERROR = 2

    def __init__(self, *messages, level=None):
        if level not in [Log.OK, Log.WARNING, Log.ERROR]:
            raise ValueError("`level` should be one of `Log.OK`, `Log.WARNING`, `Log.ERROR`")
        
        level_color = {
            Log.OK: C.green("OK"),
            Log.WARNING: C.yellow("WARNING"),
            Log.ERROR: C.red("ERROR"),
        }

        for message in messages:
            print(f" :: {level_color[level]} :: {message}...")

        if level == Log.ERROR:
            raise RuntimeError("please, check messages above")
