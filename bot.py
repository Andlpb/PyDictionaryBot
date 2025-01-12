from python_reference import python_help_dict
NOT_FOUND_MASSAGE = 'Ничего не найдено по запросу!'
class PythonHelperBot:
    def __init__(self,referrence):
        self.referrence = referrence
    def get_help(self, user_query):
        try:
            result = self.referrence[user_query]
        except KeyError:
            result = NOT_FOUND_MASSAGE
        return result
if __name__ == '__main__':
    bot = PythonHelperBot(python_help_dict)
    while True:
        user_query = input('Запрос: ')
        if user_query == 'quit':
            break
        print(bot.get_help(user_query))
    print('Программа завершила работу.')

