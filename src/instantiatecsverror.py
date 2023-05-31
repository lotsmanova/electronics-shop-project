class InstantiateCSVError(Exception):
    """
    Класс для обработки исключения
    при поврежденном файле
    """
    def __init__(self, *args, **kwargs):
        if 'name' in args or 'price' in args or 'quantity' in args:
            self.message = args[0]
        else:
            self.message = 'InstantiateCSVError: Файл item.csv поврежден'
