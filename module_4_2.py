def test_function():
    text = "Я в области видимости функции test_function"
    def inner_function():
        print(text)
    inner_function()


test_function()
# inner_function()  # При вызове inner_function, вне test_function, будет ошибка: 
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
# Так как функции inner_function локальная для test_function, и не может быть вызвана в глобальном пространстве
