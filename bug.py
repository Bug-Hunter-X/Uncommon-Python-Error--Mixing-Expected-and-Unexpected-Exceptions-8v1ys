def function_with_uncommon_error(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input types")
        return None
    return result

#Example
print(function_with_uncommon_error(10, 2))  #Output: 5.0
print(function_with_uncommon_error(10, 0))  #Output: Error: Division by zero
print(function_with_uncommon_error(10, "a")) #Output: Error: Invalid input types