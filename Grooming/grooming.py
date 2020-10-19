

##import time
##import tracemalloc
##
##profile = {'name': 'Steve', 'pay': 9000}
##
##try:
##    profile['age']
##except KeyError:
##    print('Key Not Found')
##
##
##try:
##    ...
##except RuntimeError:
##    ...
##except (KeyError, ValueError):
##    ...
##
##try:
##    profile['pay']
##except KeyError:
##    print('Key not found')
##else:
##    print('Running Else')
##finally:
##    print('Running Finally')
##
##
##def func():
##    try:
##        profile['pay']
##    except KeyError:
##        print('Key not found')
##    else:
##        print('Running Else')
##    finally:
##        print('Running Finally')
##
##func()
##
##
##def func():
##    try:
##        print('Try Block')
##    except:
##        print('Except Block')
##    else:
##        print('Else Block')
##    finally:
##        print('Fianlly Block')
##
##func()
##
##
##def func():
##    try:
##        return 1
##    except:
##        return 2
##    else:
##        return 3
##    finally:
##        return 4
##
##print(func())
##
##class SocketException(Exception):
##    pass
##
##def func():
##    try:
##        return 1/0
##    finally:
##        print('In Finally Block!!!!')
##        return 1
##    
##func()
##
##def func():
##    try:
##        raise KeyboardInterrupt
##    finally:
##        print('Goodbye World!')
##        return 1
##
##def func():
##    try:
##        return 1
##    except:
##        return 2
##    else:
##        return 3
##    finally:
##        print('FINALLY')
##
##print(func())
##
##def greet(name):
##    if not isinstance(name, str):
##        raise TypeError(f'{name} should be string')
##    print('Hello {name}')

##try:
##    1/0
##except ZeroDivisionError:
##    print('Divide By Zero')
##    raise

##class AuthError(Exception):
##    pass
##
##raise AuthError('Invalid Login')


##try:
##    f = open('spam.txt')
##except Exception as e:
##    raise RuntimeError from e	
