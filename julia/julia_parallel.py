if 'line_profiler' not in dir() and 'profile' not in dir():
    def profile(func):
        return func

