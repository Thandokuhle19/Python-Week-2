def causeError():
    try:
        return 1 + 'a'

    except TypeError:
        print('There was a type error!')

    except ZeroDivisionError:
        print('There was a zero division error')

    except Exception:
        print('There was some sort of error!')

causeError()
