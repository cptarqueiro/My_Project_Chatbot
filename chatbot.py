from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer

# Criar uma nova instancia ChatBot
# usar o read_only=True) quando o bot já estiver treinado, assim ele para de treinar e carrega mais rápido.
chatbot = ChatBot('Ordis',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  logic_adapters=[
                      'chatterbot.logic.MathematicalEvaluation',
                      'chatterbot.logic.BestMatch',
                      {
                          'import_path': 'chatterbot.logic.BestMatch',
                          'default_response': 'Sinto muito, mas não entendo. Ainda estou aprendendo.',
                          'maximum_similarity_threshold': 0.90
                      }
                  ],
                  database_uri='sqlite:///database.sqlite3')

# Treinamento informativo sobre o corona
training_data_informativo = open('training_data/corona.txt', encoding='utf-8').read().splitlines()
# treinamento sobre questões de duvidas sobre o chatbot.
training_data_personal = open('training_data/personal_ques.txt', encoding='utf-8').read().splitlines()

training_data_info = training_data_informativo
training_data_pesssoal = training_data_personal

trainer = ListTrainer(chatbot)
trainer.train(training_data_info)
trainer.train(training_data_pesssoal)

# treinamento com portuguese corpus data.
# trainer_corpus = ChatterBotCorpusTrainer(chatbot)
# trainer_corpus.train('chatterbot.corpus.portuguese')
