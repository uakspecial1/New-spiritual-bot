#!/usr/bin/env python
# coding: utf-8

# In[20]:


##Fixed size character chunking


# In[3]:

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
import re

# Sample text
text = """ Today, the spiritual Father is looking at the spirituality of all the spiritual children everywhere to see to what extent there is the sparkle of spirituality in each child. Spirituality is revealed through the eyes. Souls who have the power of spirituality constantly give others spiritual power through their eyes. A spiritual smile also gives others the experience of happiness. Their behaviour and faces appear to be double light like angels. The basis of such spirituality is purity. To the extent that there is purity in your thoughts, words and deeds, so that much spirituality will be visible. Purity is the decoration of Brahmin life. Purity is the code of conduct of Brahmin life. So BapDada is seeing the spirituality of every child on the basis of his or her purity. Whilst living in this world, spiritual souls would be seen as subtle angels.

Therefore, examine and check yourself: Is there spirituality in my thoughts and words? Spiritual thoughts fill you with power and also give power to others. You refer to this in other words as: “Spiritual thoughts are the instrument with which to serve with your mind.” Spiritual words enable you and others to experience happiness. They enable you to experience peace. One spiritual word becomes the basis for many souls to move forward in their lives. One who speaks spiritual words becomes a bestower of blessings. Spiritual actions enable you to experience the karma-yogi stage easily and you become a sample for others to become karma yogis. Whoever comes into contact with such souls easily experience the easy yogi and karma yogi life themselves. However, you were told that the seed of spirituality is purity. Purity should not be broken even in your dreams, for only then would spirituality be visible. Purity does not just mean celibacy, but let every word be “Brahmachari” (one who follows in the footsteps of Brahma), let every thought be Brahma-chari, and every action be Brahma-chari. In worldly life, when a child’s features are like his father’s, it is said that his father is visible in him. In the same way, on the basis of spirituality, let the faces of you Brahmachari Brahmin souls be experienced to be like that of Father Brahma, so that souls who come into contact with you experience your being equal to the Father. OK, you may not be 100%, but, according to the present time, what percentage should you have? What percentage have you reached? 75%? 80%? 90%? Where have you reached? This line sitting at the front, speak! Look, you have been given a number to sit at the front. So, you would also claim a number ahead in becoming Brahmachari, would you not? Are you ahead in this or not?

BapDada wishes to see the spirituality of every child on the basis of their purity. BapDada has everyone’s chart. He doesn’t say anything, but He has a chart of what each one does, and how they do it. BapDada has all the charts. Even in purity the percentage of some children is very small. According to the time, souls of the world want to see you souls as samples of spirituality. The easy way for you to show this is simply to pay attention to one term. Repeatedly underline for yourself this one term. This one term is “May you be committed to One!” (Ek-vrata). Where there is One, there is automatically stability. You automatically become unshakeable and immovable. By being committed to One, it becomes very easy to follow one direction. Since you are committed to One then, by following the directions of the One Supreme, there will easily be salvation. Your stage automatically becomes constant and stable. Therefore, check yourself: Am I committed to One? Throughout the day, do my mind and intellect remain committed to One? In accounting, an account first begins with a “1”. A zero, a number. Add one number, add one zero and see how much it continues to increase. So, even if you don’t remember anything else, you can at least remember the word “One”. Time and souls are calling out to you souls who are committed to One. O deity souls, can you not hear the call of time and the call of souls? Even the elements are seeing you masters of the elements and are calling out to you: O souls, masters of the elements, now bring about transformation! These are minor jolts in-between every now and then. Don’t make the poor, helpless souls experience jolts of sorrow and fear again and again. When will you souls, who enable others to receive liberation, you master bestowers of liberation, give liberation to those souls? Do you not feel mercy for them in your minds? Or, do you just become quiet, having heard the news? That’s it! It’s all happened. You have heard about it. This is why BapDada now wishes to see the merciful form of every child. Now renounce all your limited matters. Become merciful! Become busy serving with your minds. Give a powerful current (sakaash)! Give peace! Give support! If you become merciful and remain busy giving support to others, you will automatically become distant from all limited attractions and matters. You will become free from labouring. You have given a lot of time to serving with words. You used that time in a worthwhile way and also gave a message. You brought souls into a relationship or a connection with you. Whatever you have done so far according to the drama, you have done very well. However, now, as well as serving with words, there is a greater need for serving with your minds. Everyone, new, old, maharathis (elephant-riders), cavalry and infantry, can all do this. You don’t need any supports for this: “The older ones will do this! I am still young. I am ill! I don’t have the physical means.” Even the little children can do this. Children, you can do this, can you not? (Yes). You can serve with your minds. Therefore, now keep a balance of serving with words and your minds. All of you who serve with your minds can benefit a great deal. Why? The souls to whom you give power and a powerful current (sakaash) by serving them with your minds, that is, with your thoughts, will give you blessings. In your accounts, there is already the accumulation of effort of yourselves, and you will also accumulate in your accounts of blessings. Therefore, your saving accounts will increase in two ways. So, whether you are new or old – this time, many new ones have come. The new ones who have come for the first time, raise your hands! BapDada is asking the souls who have come here for the first time: Are you souls able to serve with your mind? (BapDada asked the Pandavas, the mothers, and all the groups individually whether they were able to serve with their minds.) All of you raised your hands very well. Now, whether you are watching and listening on the TV or whether you are listening to Baba face-to-face, BapDada is giving all of you children the responsibility: Every day, for how many hours did you serve with your minds accurately? Don’t just say: Yes, you did it. For how many hours did you serve with your minds in an accurate way? Let each one of you keep this chart with you. One day, BapDada will suddenly ask for this chart. You will not be given a date. He will ask for it suddenly. He will see whether you have worn the crown of responsibility or whether it has been shaking. You want to wear the crown of responsibility, do you not? Teachers, you have already put on the crown of responsibility, have you not? Now add this to it. Is this OK? Double-foreigners, raise your hands! Do you like this crown of responsibility? Then raise your hands! Teachers, too, raise your hands! Seeing you, everyone will receive inspiration. So, will you keep a chart? Achcha, BapDada will one day suddenly ask you: Each one write and send your own chart. Then, we shall see! Because, at the present time, there is a great need for this. Can you bear to see the sorrow and distress of your family? Are you able to see this? At least give a drop to the unhappy souls! You have a song: We are thirsty for just one drop of love. At present, souls are thirsty for one drop of peace and happiness. By receiving one drop of the nectar of peace and happiness, they will become happy. BapDada repeatedly tells you that time is waiting for you. Father Brahma is waiting to open the gates of his home. The elements are waiting to cleanse everything at a fast speed. Therefore, o angels, now, with your double light, let their waiting come to an end. All of you say the words “ever-ready”. However, have you become ever-ready in becoming complete and perfect? Don’t be ever-ready just to leave your body, but be ever-ready in becoming equal to the Father and returning home.

All of these from Madhuban are sitting at the front; it is good. They are also doing service. Those of you from Madhuban, are you ever-ready? You are laughing. Achcha, maharathis in the front line, are you ever-ready? Are you ever-ready in becoming equal to the Father? If you go just like that, you will go into the advance party. The advance party is growing without anyone’s conscious wish. If you now become busy keeping a balance between serving with words and with your minds, you will receive a lot of blessings. You will accumulate in two accounts: in your account of efforts and also of blessings. So, give and receive good wishes with your thoughts, words, deeds, relationships and connections. Just do one thing: You just have to have good wishes. Even if someone has bad wishes, you just give them good wishes because you are the children of the Ocean of Good Wishes. Even if someone is upset, don’t you become upset. You remain happy. Is that possible? Is it possible that even if 100 people upset you, you still remain happy? Is that possible? Those sitting in the second line, is that possible? Now, just wait and see: others will upset you even more! Test papers will also come? Maya is also listening to you, is she not? Just make this commitment. Have the determined thought: I have to give good wishes and receive good wishes. Is that possible? Let Maya upset you! You are those who make everyone happy, are you not? So, just do one thing, that’s all: “I mustn’t become upset or upset anyone. Even if others upset anyone, let them do it, but I mustn’t become upset. I mustn’t upset anyone or get upset.” Each one of you has to take responsibility for yourself. Don’t look at others: “Is this one doing it? Is that one doing it?” Each of you is just a detached observer watching the game. Will you see the game of just being happy? Every now and then, you also have to see the game of becoming upset, do you not? However, each one of you should keep yourself happy.

Mothers, is this possible? Pandavas, is this possible? BapDada will watch the picture. BapDada has a very big TV. It is very big. He can see each and every one. BapDada is seeing what each one is doing at every moment, but He doesn’t say anything. He doesn’t tell you about this, but He does see many colours. He also sees what you do secretly. Some children have a great deal of this trickery in them. They are very clever. If BapDada were to tell you about your trickery, then when you heard it, you would begin to have thoughts about it and this is why He doesn’t tell you. Why should He make you have thoughts? However, everything is done very cleverly. If you want to see the cleverest of all, see them amongst Brahmins. However, in what will you now become clever? In serving with your minds. Take a number ahead in this. Don’t take the last number. There are no excuses for this: “I don’t have time. I am not given a chance. My health is not OK. I wasn’t asked about it.” None of this will do. Everyone can do this. Children played a game of racing. Now race in this. Race in serving with your minds. Achcha.

This time it was Karnataka who served. Those from Karnataka who have come to serve, stand up. So many of you have come to serve. It is good. This is also a golden chance that you receive to accumulate easily in your accounts of elevated charity. On the path of devotion, it is said that it is a great act of charity to serve even one brahmin, whereas how many true Brahmins do you serve here? So you receive a very good chance. Did you like it or did you become tired? You are not tired, are you? You enjoyed yourselves, did you not? If you serve with an honest heart considering it to be charity, then the practical, visible fruit of that is that you won’t feel tired, but will be happy. This practical fruit is experienced to be the accumulation of charity. If you feel a little tired due to any reason, if you even feel this a little, then understand that it is not serving with an honest heart. Service means instant fruit, nourishing fruit. You are not just serving, but eating nourishing fruit. So all the servers of Karnataka played their part of service very well and also ate the fruit of that service.

Achcha, are all of you teachers all right? Teachers receive so many chances during the season. To receive this chance is also a sign of fortune. Now you teachers have to race in serving with your minds, but don’t just sit down for the whole day and say: “I am serving with mind.” If someone comes to take a course, you then say: “No, I am serving with my mind!” Or when it is time to do karma yoga, you say that you are serving with your mind. No. There has to be a balance. Some become too intoxicated. Therefore, don’t have that type of intoxication. Blessings will be received by keeping a balance. If there is no balance, there are no blessings. Achcha.

Now, all of you will experience serving with your minds in a second. Give souls a drop of peace and power. Achcha. To all the spiritual souls everywhere who give others the experience of the most elevated spirituality, to the Brahmachari children who use the lesson of purity in all their thoughts and dreams, to all those with determination and to all the intense effort-making souls who serve with their minds, to the charitable souls who constantly give good wishes and receive good wishes, lots of love from the depths of BapDada’s heart, the Comforter of Hearts, love, remembrance and namaste.

BapDada meeting Dadiji and Dadi Janki personally (BapDada had shown Dadi Gulzar at the inauguration of the Delhi complex at Manesar a vision of the Trimurti of Brahma Baba, Dadi Kumarka and Dadi Janki.)

BapDada showed the scene of Trimurti Brahma. Did all of you see that? It is because both of you are equal to the Father and are His companions in His every task, are you not? This is why this scene was shown. BapDada has willed special powers to both of you. He has given you will power and also willed you all powers. This is why those powers are doing their own work. Karavanhar (One who enables everything to be done) is enabling everything to be done and you are doing it all as instruments. You are enjoying it, are you not? The Father, Karankaravanhar (the One working directly and also through others) is enabling you to do it. This is why the One who is enabling you to do something is having it done. You are doing it whilst remaining carefree. You don’t have any worries, do you? You are carefree emperors. Achcha. Be knowledge-full about your health. It creates a little mischief sometimes. You definitely have to become knowledge-full in this too because you have to do a lot of service. So, health also co-operates with you. Therefore, be double knowledge-full. Achcha. """

# 1. Fixed Size Character Chunking (using CharacterTextSplitter)
def fixed_size_chunking(text, chunk_size):
    splitter = CharacterTextSplitter(separator="",chunk_size=chunk_size, chunk_overlap=10)
    return splitter.split_text(text)



# Applying the chunking strategies
fixed_size_chunks = fixed_size_chunking(text, 1000)  # Fixed-size chunks of 100 characters

# Output the results
print(f"Total number of Fixed Size Character Chunks: {len(fixed_size_chunks)}\n")
print("Fixed Size Character Chunks:")
for i, chunk in enumerate(fixed_size_chunks, 1):
    print(f"Chunk {i}:\n{chunk}\n")





# In[2]:


##Sentence Wise Chunking


# In[5]:


from langchain.text_splitter import RecursiveCharacterTextSplitter

# Define the RecursiveCharacterTextSplitter with sentence-based separators
sentence_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # Maximum number of characters per chunk
    chunk_overlap=0,  # Number of overlapping characters
    separators=[". ", "? ", "! "]  # Sentence boundary separators
)

# Get sentence-wise chunks using the RecursiveCharacterTextSplitter
sentence_chunks = sentence_splitter.split_text(text)

# Output the results
print(f"Total number of Sentence-wise Chunks: {len(sentence_chunks)}\n")
print("Sentence-wise Chunks:")
for i, chunk in enumerate(sentence_chunks, 1):
    print(f"Chunk {i}:\n{chunk}\n")


# In[5]:


##Paragraph wise Chunking


# In[74]:


from langchain.text_splitter import RecursiveCharacterTextSplitter

# RecursiveCharacterTextSplitter can split by paragraphs based on the separator used
paragraph_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000, # Number of characters per chunk
    chunk_overlap=0,  # Number of overlapping characters
    separators=["\n\n", "\n"],  # Prioritize paragraph-based splitting
)

# Get paragraph chunks using RecursiveCharacterTextSplitter
paragraph_chunks = paragraph_splitter.split_text(text)

# Output the results
print(f"Total number of Paragraph-wise Chunks: {len(paragraph_chunks)}\n")
print("Paragraph-wise Chunks:")
for i, chunk in enumerate(paragraph_chunks, 1):
    print(f"Chunk {i}:\n{chunk}\n")


# In[26]:


## Semantic Chunking


# In[55]:


import re
def split_para_to_sentence(text):
    sentences = re.split(r'(?<=[.])\s+', text)
    return sentences


# In[56]:


split_para_to_sentence(text)


# In[17]:


from langchain.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings (model_name="BAAI/bge-large-en-v1.5")


# In[57]:


len(embeddings.embed_query("vaibhavi"))


# In[58]:


import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def create_semantic_chunks(sentences):
    # Generate embeddings for each sentence
    sen_embeddings = [np.array(embeddings.embed_query(sentence)).reshape(1, -1) for sentence in sentences]
    semantic_chunks = []

    for i in range(len(sentences)):
        if i == 0:
            # Start with the first sentence
            semantic_chunks.append([sentences[i]])
        else:
            # Calculate similarity between the current sentence and the previous chunk
            similarity = cosine_similarity(sen_embeddings[i-1], sen_embeddings[i])
            if similarity[0][0] > 0.5:
                # Append to the last chunk if similarity is above the threshold
                semantic_chunks[-1].append(sentences[i])
            else:
                # Start a new chunk
                semantic_chunks.append([sentences[i]])
                
    return semantic_chunks


# In[59]:


sentences = split_para_to_sentence(text)


# In[60]:


sentences


# In[38]:


create_semantic_chunks(sentences)


# In[39]:


chunks = create_semantic_chunks(sentences)


# In[40]:


len(chunks)


# In[75]:


chunks[0]


# In[77]:


chunks[1]


# In[50]:


## Topic based semantic chunking and Contextual semantic chunking


# In[67]:


import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from langchain.embeddings import HuggingFaceEmbeddings

# Function to perform topic-based chunking
def create_topic_based_chunks(sentences, embeddings, n_topics=3):
    # Generate embeddings for each sentence
    sen_embeddings = np.array([embeddings.embed_query(sentence) for sentence in sentences])
    
    # Perform KMeans clustering to group sentences into topic chunks
    kmeans = KMeans(n_clusters=n_topics, random_state=42)
    sentence_clusters = kmeans.fit_predict(sen_embeddings)

    # Organize sentences into topic chunks based on clusters
    topic_chunks = [[] for _ in range(n_topics)]
    for i, cluster in enumerate(sentence_clusters):
        topic_chunks[cluster].append(sentences[i])

    return topic_chunks

# Function to perform contextual chunking
def create_contextual_chunks(sentences, embeddings, similarity_threshold=0.5):
    # Generate embeddings for each sentence
    sen_embeddings = [np.array(embeddings.embed_query(sentence)).reshape(1, -1) for sentence in sentences]
    
    contextual_chunks = []

    for i in range(len(sentences)):
        if i == 0:
            # Start with the first sentence
            contextual_chunks.append([sentences[i]])
        else:
            # Calculate similarity between the current sentence and the previous chunk
            similarity = cosine_similarity(sen_embeddings[i-1], sen_embeddings[i])
            if similarity[0][0] > similarity_threshold:
                # Append to the last chunk if similarity is above the threshold
                contextual_chunks[-1].append(sentences[i])
            else:
                # Start a new chunk if context shifts
                contextual_chunks.append([sentences[i]])
    
    return contextual_chunks

# Example usage
sentences = [
    "The sky is clear and blue.",  # Topic 1: Weather
    "It's a sunny day.",           # Topic 1: Weather
    "I love eating pizza.",        # Topic 2: Food
    "Pasta is a great Italian dish.",  # Topic 2: Food
    "Rain is expected tomorrow.",  # Topic 1: Weather
    "The stock market is unpredictable.",  # Topic 3: Finance
    "Investing can be risky."      # Topic 3: Finance
]
  # Replace with actual sentences

embeddings = HuggingFaceEmbeddings (model_name="BAAI/bge-large-en-v1.5")  # Example model


# For topic-based chunking
topic_chunks = create_topic_based_chunks(sentences, embeddings, n_topics=3)
print("Topic-Based Chunks:")
for i, chunk in enumerate(topic_chunks):
    print(f"Chunk {i+1}: {chunk}")

# For contextual chunking
contextual_chunks = create_contextual_chunks(sentences, embeddings, similarity_threshold=0.5)
print("\nContextual Chunks:")
for i, chunk in enumerate(contextual_chunks):
    print(f"Chunk {i+1}: {chunk}")



# In[ ]:





# In[69]:


import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from langchain.embeddings import HuggingFaceEmbeddings

# Function to perform topic-based chunking
def create_topic_based_chunks(sentences, embeddings, n_topics=3):
    # Generate embeddings for each sentence
    sen_embeddings = np.array([embeddings.embed_query(sentence) for sentence in sentences])
    
    # Perform KMeans clustering to group sentences into topic chunks
    kmeans = KMeans(n_clusters=n_topics, random_state=42)
    sentence_clusters = kmeans.fit_predict(sen_embeddings)

    # Organize sentences into topic chunks based on clusters
    topic_chunks = [[] for _ in range(n_topics)]
    for i, cluster in enumerate(sentence_clusters):
        topic_chunks[cluster].append(sentences[i])

    return topic_chunks

# Function to perform contextual chunking
def create_contextual_chunks(sentences, embeddings, similarity_threshold=0.5):
    # Generate embeddings for each sentence
    sen_embeddings = [np.array(embeddings.embed_query(sentence)).reshape(1, -1) for sentence in sentences]
    
    contextual_chunks = []

    for i in range(len(sentences)):
        if i == 0:
            # Start with the first sentence
            contextual_chunks.append([sentences[i]])
        else:
            # Calculate similarity between the current sentence and the previous chunk
            similarity = cosine_similarity(sen_embeddings[i-1], sen_embeddings[i])
            if similarity[0][0] > similarity_threshold:
                # Append to the last chunk if similarity is above the threshold
                contextual_chunks[-1].append(sentences[i])
            else:
                # Start a new chunk if context shifts
                contextual_chunks.append([sentences[i]])
    
    return contextual_chunks

# Example usage
sentences = [' Today, the spiritual Father is looking at the spirituality of all the spiritual children everywhere to see to what extent there is the sparkle of spirituality in each child.',
 'Spirituality is revealed through the eyes.',
 'Souls who have the power of spirituality constantly give others spiritual power through their eyes.',
 'A spiritual smile also gives others the experience of happiness.',
 'Their behaviour and faces appear to be double light like angels.',
 'The basis of such spirituality is purity.',
 'To the extent that there is purity in your thoughts, words and deeds, so that much spirituality will be visible.',
 'Purity is the decoration of Brahmin life.',
 'Purity is the code of conduct of Brahmin life.',
 'So BapDada is seeing the spirituality of every child on the basis of his or her purity.',
 'Whilst living in this world, spiritual souls would be seen as subtle angels.',
 'Therefore, examine and check yourself: Is there spirituality in my thoughts and words? Spiritual thoughts fill you with power and also give power to others.',
 'You refer to this in other words as: “Spiritual thoughts are the instrument with which to serve with your mind.” Spiritual words enable you and others to experience happiness.',
 'They enable you to experience peace.',
 'One spiritual word becomes the basis for many souls to move forward in their lives.',
 'One who speaks spiritual words becomes a bestower of blessings.',
 'Spiritual actions enable you to experience the karma-yogi stage easily and you become a sample for others to become karma yogis.',
 'Whoever comes into contact with such souls easily experience the easy yogi and karma yogi life themselves.',
 'However, you were told that the seed of spirituality is purity.',
 'Purity should not be broken even in your dreams, for only then would spirituality be visible.',
 'Purity does not just mean celibacy, but let every word be “Brahmachari” (one who follows in the footsteps of Brahma), let every thought be Brahma-chari, and every action be Brahma-chari.',
 'In worldly life, when a child’s features are like his father’s, it is said that his father is visible in him.',
 'In the same way, on the basis of spirituality, let the faces of you Brahmachari Brahmin souls be experienced to be like that of Father Brahma, so that souls who come into contact with you experience your being equal to the Father.',
 'OK, you may not be 100%, but, according to the present time, what percentage should you have? What percentage have you reached? 75%? 80%? 90%? Where have you reached? This line sitting at the front, speak! Look, you have been given a number to sit at the front.',
 'So, you would also claim a number ahead in becoming Brahmachari, would you not? Are you ahead in this or not?\n\nBapDada wishes to see the spirituality of every child on the basis of their purity.',
 'BapDada has everyone’s chart.',
 'He doesn’t say anything, but He has a chart of what each one does, and how they do it.',
 'BapDada has all the charts.',
 'Even in purity the percentage of some children is very small.',
 'According to the time, souls of the world want to see you souls as samples of spirituality.',
 'The easy way for you to show this is simply to pay attention to one term.',
 'Repeatedly underline for yourself this one term.',
 'This one term is “May you be committed to One!” (Ek-vrata).',
 'Where there is One, there is automatically stability.',
 'You automatically become unshakeable and immovable.',
 'By being committed to One, it becomes very easy to follow one direction.',
 'Since you are committed to One then, by following the directions of the One Supreme, there will easily be salvation.',
 'Your stage automatically becomes constant and stable.',
 'Therefore, check yourself: Am I committed to One? Throughout the day, do my mind and intellect remain committed to One? In accounting, an account first begins with a “1”.',
 'A zero, a number.',
 'Add one number, add one zero and see how much it continues to increase.',
 'So, even if you don’t remember anything else, you can at least remember the word “One”.',
 'Time and souls are calling out to you souls who are committed to One.',
 'O deity souls, can you not hear the call of time and the call of souls? Even the elements are seeing you masters of the elements and are calling out to you: O souls, masters of the elements, now bring about transformation! These are minor jolts in-between every now and then.',
 'Don’t make the poor, helpless souls experience jolts of sorrow and fear again and again.',
 'When will you souls, who enable others to receive liberation, you master bestowers of liberation, give liberation to those souls? Do you not feel mercy for them in your minds? Or, do you just become quiet, having heard the news? That’s it! It’s all happened.',
 'You have heard about it.',
 'This is why BapDada now wishes to see the merciful form of every child.',
 'Now renounce all your limited matters.',
 'Become merciful! Become busy serving with your minds.',
 'Give a powerful current (sakaash)! Give peace! Give support! If you become merciful and remain busy giving support to others, you will automatically become distant from all limited attractions and matters.',
 'You will become free from labouring.',
 'You have given a lot of time to serving with words.',
 'You used that time in a worthwhile way and also gave a message.',
 'You brought souls into a relationship or a connection with you.',
 'Whatever you have done so far according to the drama, you have done very well.',
 'However, now, as well as serving with words, there is a greater need for serving with your minds.',
 'Everyone, new, old, maharathis (elephant-riders), cavalry and infantry, can all do this.',
 'You don’t need any supports for this: “The older ones will do this! I am still young.',
 'I am ill! I don’t have the physical means.” Even the little children can do this.',
 'Children, you can do this, can you not? (Yes).',
 'You can serve with your minds.',
 'Therefore, now keep a balance of serving with words and your minds.',
 'All of you who serve with your minds can benefit a great deal.',
 'Why? The souls to whom you give power and a powerful current (sakaash) by serving them with your minds, that is, with your thoughts, will give you blessings.',
 'In your accounts, there is already the accumulation of effort of yourselves, and you will also accumulate in your accounts of blessings.',
 'Therefore, your saving accounts will increase in two ways.',
 'So, whether you are new or old – this time, many new ones have come.',
 'The new ones who have come for the first time, raise your hands! BapDada is asking the souls who have come here for the first time: Are you souls able to serve with your mind? (BapDada asked the Pandavas, the mothers, and all the groups individually whether they were able to serve with their minds.) All of you raised your hands very well.',
 'Now, whether you are watching and listening on the TV or whether you are listening to Baba face-to-face, BapDada is giving all of you children the responsibility: Every day, for how many hours did you serve with your minds accurately? Don’t just say: Yes, you did it.',
 'For how many hours did you serve with your minds in an accurate way? Let each one of you keep this chart with you.',
 'One day, BapDada will suddenly ask for this chart.',
 'You will not be given a date.',
 'He will ask for it suddenly.',
 'He will see whether you have worn the crown of responsibility or whether it has been shaking.',
 'You want to wear the crown of responsibility, do you not? Teachers, you have already put on the crown of responsibility, have you not? Now add this to it.',
 'Is this OK? Double-foreigners, raise your hands! Do you like this crown of responsibility? Then raise your hands! Teachers, too, raise your hands! Seeing you, everyone will receive inspiration.',
 'So, will you keep a chart? Achcha, BapDada will one day suddenly ask you: Each one write and send your own chart.',
 'Then, we shall see! Because, at the present time, there is a great need for this.',
 'Can you bear to see the sorrow and distress of your family? Are you able to see this? At least give a drop to the unhappy souls! You have a song: We are thirsty for just one drop of love.',
 'At present, souls are thirsty for one drop of peace and happiness.',
 'By receiving one drop of the nectar of peace and happiness, they will become happy.',
 'BapDada repeatedly tells you that time is waiting for you.',
 'Father Brahma is waiting to open the gates of his home.',
 'The elements are waiting to cleanse everything at a fast speed.',
 'Therefore, o angels, now, with your double light, let their waiting come to an end.',
 'All of you say the words “ever-ready”.',
 'However, have you become ever-ready in becoming complete and perfect? Don’t be ever-ready just to leave your body, but be ever-ready in becoming equal to the Father and returning home.',
 'All of these from Madhuban are sitting at the front; it is good.',
 'They are also doing service.',
 'Those of you from Madhuban, are you ever-ready? You are laughing.',
 'Achcha, maharathis in the front line, are you ever-ready? Are you ever-ready in becoming equal to the Father? If you go just like that, you will go into the advance party.',
 'The advance party is growing without anyone’s conscious wish.',
 'If you now become busy keeping a balance between serving with words and with your minds, you will receive a lot of blessings.',
 'You will accumulate in two accounts: in your account of efforts and also of blessings.',
 'So, give and receive good wishes with your thoughts, words, deeds, relationships and connections.',
 'Just do one thing: You just have to have good wishes.',
 'Even if someone has bad wishes, you just give them good wishes because you are the children of the Ocean of Good Wishes.',
 'Even if someone is upset, don’t you become upset.',
 'You remain happy.',
 'Is that possible? Is it possible that even if 100 people upset you, you still remain happy? Is that possible? Those sitting in the second line, is that possible? Now, just wait and see: others will upset you even more! Test papers will also come? Maya is also listening to you, is she not? Just make this commitment.',
 'Have the determined thought: I have to give good wishes and receive good wishes.',
 'Is that possible? Let Maya upset you! You are those who make everyone happy, are you not? So, just do one thing, that’s all: “I mustn’t become upset or upset anyone.',
 'Even if others upset anyone, let them do it, but I mustn’t become upset.',
 'I mustn’t upset anyone or get upset.” Each one of you has to take responsibility for yourself.',
 'Don’t look at others: “Is this one doing it? Is that one doing it?” Each of you is just a detached observer watching the game.',
 'Will you see the game of just being happy? Every now and then, you also have to see the game of becoming upset, do you not? However, each one of you should keep yourself happy.',
 'Mothers, is this possible? Pandavas, is this possible? BapDada will watch the picture.',
 'BapDada has a very big TV.',
 'It is very big.',
 'He can see each and every one.',
 'BapDada is seeing what each one is doing at every moment, but He doesn’t say anything.',
 'He doesn’t tell you about this, but He does see many colours.',
 'He also sees what you do secretly.',
 'Some children have a great deal of this trickery in them.',
 'They are very clever.',
 'If BapDada were to tell you about your trickery, then when you heard it, you would begin to have thoughts about it and this is why He doesn’t tell you.',
 'Why should He make you have thoughts? However, everything is done very cleverly.',
 'If you want to see the cleverest of all, see them amongst Brahmins.',
 'However, in what will you now become clever? In serving with your minds.',
 'Take a number ahead in this.',
 'Don’t take the last number.',
 'There are no excuses for this: “I don’t have time.',
 'I am not given a chance.',
 'My health is not OK.',
 'I wasn’t asked about it.” None of this will do.',
 'Everyone can do this.',
 'Children played a game of racing.',
 'Now race in this.',
 'Race in serving with your minds.',
 'Achcha.',
 'This time it was Karnataka who served.',
 'Those from Karnataka who have come to serve, stand up.',
 'So many of you have come to serve.',
 'It is good.',
 'This is also a golden chance that you receive to accumulate easily in your accounts of elevated charity.',
 'On the path of devotion, it is said that it is a great act of charity to serve even one brahmin, whereas how many true Brahmins do you serve here? So you receive a very good chance.',
 'Did you like it or did you become tired? You are not tired, are you? You enjoyed yourselves, did you not? If you serve with an honest heart considering it to be charity, then the practical, visible fruit of that is that you won’t feel tired, but will be happy.',
 'This practical fruit is experienced to be the accumulation of charity.',
 'If you feel a little tired due to any reason, if you even feel this a little, then understand that it is not serving with an honest heart.',
 'Service means instant fruit, nourishing fruit.',
 'You are not just serving, but eating nourishing fruit.',
 'So all the servers of Karnataka played their part of service very well and also ate the fruit of that service.',
 'Achcha, are all of you teachers all right? Teachers receive so many chances during the season.',
 'To receive this chance is also a sign of fortune.',
 'Now you teachers have to race in serving with your minds, but don’t just sit down for the whole day and say: “I am serving with mind.” If someone comes to take a course, you then say: “No, I am serving with my mind!” Or when it is time to do karma yoga, you say that you are serving with your mind.',
 'No.',
 'There has to be a balance.',
 'Some become too intoxicated.',
 'Therefore, don’t have that type of intoxication.',
 'Blessings will be received by keeping a balance.',
 'If there is no balance, there are no blessings.',
 'Achcha.',
 'Now, all of you will experience serving with your minds in a second.',
 'Give souls a drop of peace and power.',
 'Achcha.',
 'To all the spiritual souls everywhere who give others the experience of the most elevated spirituality, to the Brahmachari children who use the lesson of purity in all their thoughts and dreams, to all those with determination and to all the intense effort-making souls who serve with their minds, to the charitable souls who constantly give good wishes and receive good wishes, lots of love from the depths of BapDada’s heart, the Comforter of Hearts, love, remembrance and namaste.',
 'BapDada meeting Dadiji and Dadi Janki personally (BapDada had shown Dadi Gulzar at the inauguration of the Delhi complex at Manesar a vision of the Trimurti of Brahma Baba, Dadi Kumarka and Dadi Janki.)\n\nBapDada showed the scene of Trimurti Brahma.',
 'Did all of you see that? It is because both of you are equal to the Father and are His companions in His every task, are you not? This is why this scene was shown.',
 'BapDada has willed special powers to both of you.',
 'He has given you will power and also willed you all powers.',
 'This is why those powers are doing their own work.',
 'Karavanhar (One who enables everything to be done) is enabling everything to be done and you are doing it all as instruments.',
 'You are enjoying it, are you not? The Father, Karankaravanhar (the One working directly and also through others) is enabling you to do it.',
 'This is why the One who is enabling you to do something is having it done.',
 'You are doing it whilst remaining carefree.',
 'You don’t have any worries, do you? You are carefree emperors.',
 'Achcha.',
 'Be knowledge-full about your health.',
 'It creates a little mischief sometimes.',
 'You definitely have to become knowledge-full in this too because you have to do a lot of service.',
 'So, health also co-operates with you.',
 'Therefore, be double knowledge-full.',
 'Achcha.',
 '']
  # Replace with actual sentences

embeddings = HuggingFaceEmbeddings (model_name="BAAI/bge-large-en-v1.5")  # Example model


# For topic-based chunking
topic_chunks = create_topic_based_chunks(sentences, embeddings, n_topics=3)
print("Topic-Based Chunks:")
for i, chunk in enumerate(topic_chunks):
    print(f"Chunk {i+1}: {chunk}")

# For contextual chunking
contextual_chunks = create_contextual_chunks(sentences, embeddings, similarity_threshold=0.5)
print("\nContextual Chunks:")
for i, chunk in enumerate(contextual_chunks):
    print(f"Chunk {i+1}: {chunk}")



# In[70]:


len(topic_chunks)


# In[71]:


len(contextual_chunks)


# In[ ]:




