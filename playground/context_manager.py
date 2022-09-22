import contextlib


@contextlib.contextmanager
def manage_context():
    print("Entering the context manager")
    yield 1
    print("Exiting the context manager")


with manage_context() as one:
    print(one)


