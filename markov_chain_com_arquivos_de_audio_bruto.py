from Neuraline.ArtificialIntelligence.MachineLearning.AutonomousLearning.markov_chain import MarkovChain
markov_chain = MarkovChain()

markov_chain.addFit(url_path='./songs/music01.wav', progress=True)
markov_chain.addFit(url_path='./songs/music02.wav', progress=True)
markov_chain.saveModel('markov_chain_modelo_musical')

result = markov_chain.predict(progress=True)
print(result)
