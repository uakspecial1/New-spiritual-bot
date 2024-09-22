


# #**Step 2: Import All the Required Libraries**

# In[3]:


from langchain.document_loaders import PyPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from sentence_transformers import SentenceTransformer
from langchain.chains.question_answering import load_qa_chain
import pinecone
import os


# #**Load the Data**

# In[ ]:





# In[ ]:





# In[35]:


data = """ Today, Father Shiva, the Creator of the Trimurti, has come to meet His worthy­of­worship saligrams. Today, it is a meeting as well as a celebration. All of you have arrived here from all over the world with a lot of zeal and enthusiasm in order to celebrate BapDada's birthday. Children say that they have come to celebrate the Father's birthday and the Father says that He has come to celebrate the children's birthday. All of you have also come to celebrate your alokik birthday. At no other time throughout the whole cycle can there be such another lovely and unique birthday. Throughout the whole cycle, did you see or celebrate such a birthday that is the same for the Father as well as the children? This is because, for the task of world transformation, together with Father Shiva and Brahma Dada, Brahmins are also needed. A sacrificial fire cannot be successful without Brahmins. This is why the birthday, the jayantis, of the Father and children are together. Children are congratulating the Father from their heart and the Father is giving each Brahmin child more than multi­multi­million times congratulations as well as blessings from the heart for the alokik birthday. Congratulations! Congratulations! Congratulations! Very good! You enjoy clapping with one hand, not two hands. There is a lot of happiness and so you can't stop your hands; they just move automatically.

In the world also, devotees celebrate Shiv Jayanti with a lot of splendour. However, their celebration is one night without sleep (jagran) or a fast for one day. You children have not had the thought of having jagran of the sleep of ignorance for only one day ­ they too have jagran ­ but you have stayed awake for the whole of this one life of the confluence age that is like a diamond. You have awakened, have you not? You will not now go back to sleep, will you? Or will you fall asleep a little? Achcha, you may not have fallen asleep, but perhaps you nod off! This staying awake throughout the night is such that you yourself are awake, and you also awaken others. In this life of knowledge, to remain awake means to come out of the darkness and into the light. All of you like this spiritual wakefulness, do you not? From the moment you took birth and celebrated your birthday, what vows have you kept from that time? Do you remember them? Children say: Let alone remembering them, our life has become that of a natural vow. Our life has become one of pure diet, pure interaction and pure thoughts. It isn't for just one or two months, but it has become such that we have imbibed this vow in our life. It has become natural and it has become our nature. You have made your nature that of purity, have you not? Has your nature become that or do you have to make it that? It has become that, has it not? Simply nod in agreement, that's all! Has it become that? Has impurity finished in your nature and has purity merged in your life? You have now celebrated Shiv Jayanti and saligram jayanti that are as valuable as a diamond. The children from everywhere abroad and in this land are also celebrating it at the same time. BapDada is seeing that together with you and the Father, they too are all so happy!

Today, as your memorial, devotees especially offer a sacrifice. All of you surrender yourself to the Father in your thoughts, words and deeds. In memory of that, devotees don't offer themselves as a sacrifice, but sacrifice a goat instead. Could they not find anything else? Could they only find a goat? You know the significance of this. It is because the greatest cause of body consciousness is the consciousness of "I" (mai ­ in Hindi is "I"). When you surrender the consciousness of "I", it is then that you become Brahmins. So what does a goat do? "Maiii, maiii!" So this is a sign of the body consciousness of "I". The consciousness of the "I" of body consciousness is also very subtle and has a variety of forms. The first consciousness of "I" is "I am a body!" "I am so­and­so!" Then, as you move further, there are the different forms of "I" as you become trapped in relationships. Then, as you move further, there are the different forms of "I" of position. Even more subtle than that is the "I" of your own speciality which brings you down from up above. Each of you has a speciality. Whether it is in a gross or a subtle form, there isn't a single human soul who doesn't have a speciality. In this life of knowledge too, each Brahmin definitely has at least one speciality. However, in the life of knowledge, a speciality is a gift bestowed by God. It is God's gift. When you put the consciousness of "I" into the gift that God has given you, this is royal ego and the biggest consciousness of "I". And so you are already surrendered yourself, but what do you still have to consider further?

What do all of you teachers call yourselves? You are surrendered, are you not? Are all teachers surrendered? Achcha, are those who are living at home with their family surrendered? Yes or no? You are surrendered! Are the Pandavas surrendered? Very good! Congratulations! What are you going to do now? You have surrendered yourselves and that is very good. Now, in future, you have to check that… Should Baba tell you? You would say: We are surrendered, so what else do we have to do now? One is to surrender, but after that there is total surrender. Especially underlined in total surrender is the surrender of your mind, intellect and sanskars. Because in order to move forward, you have to take fast steps in your efforts. You are doing that, even now, according to the present atmosphere in your Brahmin life, because the majority of you sitting here are Brahmins. There is just an influence of waste on the mind, nothing bad, because all bad things have finished. However, according to the present atmosphere, wasteful and negative things influence the intellect a great deal, and because of this, the power of realisation to make an accurate and true decision decreases. There is realisation through the understanding that, "Yes, this is wrong!" "This is not right!" However, one is realisation with common sense and the other is realisation with your heart. When you realise something with your heart, then, even if the world changes, you yourself would not change. So you have been told about the mind and intellect. Now the sanskars. Because your sanskars are 63 births old, they have become natural. In other words, you say, “This is not a mistake, but it is my nature.” Therefore, some of the old sanskars are erased and others are suppressed, but then emerge again. However, total surrender means that the motives and feelings in your mind for every soul should be transformed. BapDada refers to this as: No matter what souls are like, there will always be a variety. This is the kalpa tree, and if there were no variety in that, then there wouldn't be any beauty. However, there should be good wishes and pure feelings for every soul. You even have to transform bad wishes and have good wishes and pure feelings. Have good wishes for every soul that they will definitely transform themselves. Don't think: This one is never going to change. Don't become their judge and make a judgement that they are never going to change. Since you have issued a challenge that you will transform the elements and make them satoguni, then you have to do it. There is no question of whether or not they will become that, but it is you who have to make them that. You have underlined the words "have to do it". So is it that the elements can change but the soul cannot change? The soul is the master of matter. Matter changes and the master doesn't. Why? So at the present time the only service to do is transformation of the self ­ the mind, intellect and sanskars; the transformation of everything.

Everyone is asking: What are we going to do this year? You have to do double service. First, totally surrender the self! Surrender the self to such an extent that your vibrations, atmosphere, company, co­operation of the heart, and blessings of the heart help others to bring about easy transformation. You have to transform the self to this extent. You have to totally surrender everything. This is one type of service and the other is serving other people. As a result, it has been seen that everywhere in this land and abroad, whatever service you Brahmin children have done, even in the villages, you have done it with love for the Father. BapDada is giving many, many congratulations for that. What will you do in the future?

BapDada has seen that there is growth of Brahmins and there will be even faster growth. However, together with this, the service you have done that people like, the service that is taking place through the different projects, is very good. Now very good co­operative souls have become good instruments at many different places. They are very good co­operative souls. They have taken one step of co­operation; they have put one foot forward. However, the other foot is to become an easy yogi and a karma yogi. A few have become karma yogis and easy yogis to some extent; this is the second stage. Now, such souls have to play a practical part on the stage. A mike is always on the stage. Therefore they should become mikes and definitely come on to the stage of service in a visible way. You are the might and they are the mikes. Just as Brahma Baba in the subtle form is the might who has made you children mikes, in the same way, now become the might and prepare such mikes. They are very good, there is hope for them, and they can go fast. However, now it is necessary to increase the connection with such souls. They want to know what to do and how to do it. Become the might and show them that whilst maintaining a balance of their worldly occupation and their spiritual service, they, who have come last, can go fast and come into the line of those who come first. There are such souls; they just have to be revealed! Simply maintain a connection with them and give them a current! The current of spirituality, the current of vibrations and atmosphere and also show them the way to become instruments to reveal that a balanced life is very good and easy. Is this all right? You have now heard what you have to do, have you not?

Prepare small bouquets. OK, not a big bouquet, but at least bring a bouquet of 5 or 10 flowers. They exist everywhere in BapDada's eyes. Did you hear that? Did the Pandavas hear that? Very good!

Double foreigners are not jumping, but are flying. So, who will bring the first bouquet, those from abroad or those from Bharat? Who will bring it? Or will both bring them at the same time? The bouquet from abroad on one side and the bouquet from Bharat on the other. Both bouquets will come on to the stage. Just as you celebrate this ceremony, so we shall then also celebrate that ceremony with both bouquets, one from Bharat and one from abroad. Is this all right? What do those from abroad think? Will you bring them in the next season? Will you bring them? Will those from Bharat bring them? Bring those who have a balance of their worldly and spiritual occupation, not just those who have a Brahmin life like you, but both worldly and spiritual. Their impact will be greater. People will come to you for drishti.

Achcha, what are you thinking, Jayanti? Are you thinking about names? Nirmala, Mohini, you are thinking about names, are you not? Look at the Pandavas here! There are fewer Pandavas in Bharat. They are equal to Allah! Look, some are even sitting here. This is Brian sitting just in front, is it not? (Speaking to Brian of Australia). A bouquet has to be prepared, does it not? There are very good souls. What is the name you use? NCO. Achcha. Those from the NCOs abroad, raise your hands! It is not easy to become an NCO! You will have to perform wonders! You can do it; it is not a big thing because the land is now ready. The seed is also sown; it just needs to be watered with sustenance. Now the seed needs the water of sustenance. Achcha. BapDada is pleased to see all the children. In every meeting, half the numbers are new ones who have come for the first time. Therefore, this is a sign of growth. Those who have come now for the first time, raise your hands! Simply raise your hands! TV crew, show the hands of those at the back! There are many of them. To all you special souls who have come for the first time, congratulations for celebrating your new birthday. It is only today that you are celebrating your birthday in Madhuban, this time. It is good!

Many teachers have also come. Congratulations to the teachers also! All of you have done service, have you not? So, congratulations for the service! Achcha. What is the condition of Gujarat? The upheaval has started in Gujarat. There is a lot of upheaval in Gujarat and even a little abroad. You are not afraid, are you? The earth is shaking, but your heart isn't shaking, is it? The earth shook a little, and damage was caused. Those who have come from there, stand up! Those from Ahmedabad, stand up! Achcha. Did your heart shake or did the earth shake? What happened? Did it shake your heart a little? It didn’t! You are courageous! BapDada saw that children kept their record good by maintaining courage and by keeping the Father's canopy of protection over them. None of you failed. All of you passed: some less and some more. It is numberwise everywhere, but you passed! Congratulations! Who has come from the most sensitive place? (There was one person from Bhuj and another town nearby) Achcha, you were with the One with a thousand arms in Bhuj (bhuja – arms). Achcha, you passed this paper! You did very well! In future too, don’t fluctuate! This will continue to happen. Don’t be afraid. (It happens every day.) Let it happen! Transformation has to take place. Nature will also do its work. Since human souls have made nature tamoguni, she will do her own work. However, in every game of the drama, this too is a game. Whilst watching the game, don’t allow your stage to fluctuate. External situations should not influence the original stage of master almighty souls. Instead, become instruments to liberate souls from the distress in their mind because it is only with meditation that you can finish the distress of the mind. Doctors will do their work, scientists will do their work, and the Government will do its work. Your duty is to finish the distress and tension of the mind. Give the donation of a tension­free life! Give co­ operation! At present, this land and lands abroad are all co­operating and giving their co­ operation, are they not? They are doing very good work. This shows that whatever land it is or whoever it is, they all have love for the land of Bharat. They are all doing what they have to do, and you are continuing with your work. When there is a fire, firemen are not afraid, but they put out the fire. All of you are those who put out the fire of the distress of the mind. Achcha.

Gujarat is strong, is it not? You are under the canopy of protection of the One with a Thousand Arms. Having seen this in Gujarat, wherever it now happens, you have now become experienced. Look, no one can command nature. You can't say: Come in Gujarat! Don’t come in Abu! Don’t come in Bombay! No! It is independent. However, all of you have to make your own stage unshakeable and immovable and keep the line of your mind and intellect clear. When your line is clear you will receive touchings. BapDada had told you earlier too that theirs is a wireless and yours is a viceless intellect. Then you will very quickly and clearly be able to decide what you have to do and what is going to happen. You won't need to think: Let's get out! Let's sit inside! Let's sit by the door! Let's sit on the roof! No! Your feet will only go where there is safety. And if you become too afraid ­ and, in fact, you shouldn’t be afraid ­ but if you are very afraid and have a lot of fear, then Madhuban, the asylum, the home is yours. Don’t be afraid! This is nothing. Now, everything is yet to happen! Don’t be afraid! It is just a game! Transformation has to take place. Not destruction, but transformation. The attitude of disinterest has to be created in everyone. Become merciful and with all powers, have mercy and give a powerful current. Do you understand?

This time it was Eastern Zone, Nepal & Tamil Nadu who were responsible for service:

Those from Tamil Nadu, stand up! All of you are standing wearing your sashes. Achcha, your duty is security. You did good service and you also receive the fruit of service in the form of happiness as well as power for the present and the future too. So, you received the power of service and also the fruit of service. Is this right? You did very good service. Congratulations! Those from Nepal, stand up! What service did those from Nepal do? (Cut the vegetables, clean the grain etc.) You did hard work! Look, if they hadn’t cut the vegetables, what would you all have eaten? This is why you did very good service and you also received blessings from so many Brahmin souls for the service you did. Your blessings have accumulated. All of you served from your heart. This record of everyone is good. Achcha. Congratulations.

Eastern Zone: Bengal, Bihar, Orissa, Assam:
Those from Bihar, stand up! There are many at the back. What duty did those from Bihar perform? (Security.) You also did your own security, did you not? You provided security of your own stage and also that of Shantivan. You did very well! Look, everyone’s face is so happy! The sparkle of service has now come on to the face. Very good! Those from Orissa, stand up! The majority are from Orissa. What did those from Orissa do? (Accommodation, rolling chapattis, providing tea, water, food and serving.) Look, those from Orissa performed the greatest wonders! You did very well! There are many of you and this is why you performed great wonders! You were happy, were you not? How much happiness did you receive from service? A lot! Assam: There are more Shaktis in Assam. The Shakti Army is larger. What duty did you perform? (Transport and serving VIPs) Achcha, did you enable everyone reach their destination well? You brought them from the train stations and will take them back there; you will take them there in comfort. You did well. Of Assam, BapDada says: They are those with a special personality (assami). Not Assam, but assami! Very good! Congratulations! Bengal: What duty did those from Bengal perform? (Cleaning, meetings with Dadiji and laundry). Cleaning on one side and meetings with Dadi on the other side. The two match one another so well! Cleanliness is essential and meetings too are essential! Look, you performed your duty considering this to be your home and therefore, there was success, success and success. Success is the birthright of you children. Therefore, you achieved success, did you not? Very good!

Achcha, now the group of kumars from abroad:
You had a very good bhatti. You enjoyed it very much. Kumars will perform wonders. Kumars can do whatever they want. You are doing it and will continue to do it in the future. You are going to do it, are you not? All of you are clever. BapDada is seeing from your faces that all of you are courageous. Congratulations for your courage. Very good! BapDada has seen you. Now you won’t complain that no one has seen you, will you? BapDada has seen each one of you. You have worked well.

Achcha, BapDada has seen, not heard, but seen that this time the double foreigners have had very good experiences of silence. It is not possible to hear everyone's experience, but He has heard everyone. You made the programmes with great zeal and enthusiasm. In future also, when you go back, every now and again, continue to have these experiences of silence in your own countries. Make whatever time you are able to for this, because silence also influences the service you do. You have had very good programmes. BapDada is pleased. Continue to increase them in the future. Continue to fly and make others fly. Achcha.

Are you now able to concentrate your mind and intellect in one second? Are you able to do this? Stop, and it should stop. Now, completely concentrate your mind and intellect in the form of a point in just one second! Merge into the Point. Achcha.

To all the most elevated Brahmins everywhere; to the stable souls everywhere who constantly have the determination to keep their vow; to the great serviceable souls everywhere who have total courage and enthusiasm for self­service and the service of benefiting people; congratulations for today's Shiv Jayanti, the jayanti as valuable as a diamond, the jayanti that is lovely and unique and, together with this, blessings, love, remembrance and namaste.

Achcha, many very good cards and letters have come from everyone. BapDada is seeing that they have been placed here. The letters of the effort made from the heart written by the double foreigners have all reached BapDada. BapDada has received all their cards and letters with a variety of decoration on them, Baba has received their cards of very beautiful thoughts filled with the zeal and enthusiasm from the heart. This is why BapDada is giving love and remembrance to those who are sitting far away whilst seeing them to be the closest and in front of Him.

BapDada meeting the Chief Minister of Andhra Pradesh and his wife, Mr and Mrs Chandra Babu Naidu:

You did very well to reach your Godly family. This is a Godly family, is it not? You are a family member, are you not? Or, have you come from outside? Who are you? Are you a family member? You are not a guest! Are you a guest? You are the host. You are not a guest. This is your home because this is God's home and so it is everyone's home. BapDada is happy that the child has one speciality. That speciality is courage. Whenever you carry out any task, you do that with courage and, because of your courage, you automatically receive help. You should never lose courage. Courage makes you worthy of receiving help from God. (To Mrs Naidu) This one is also courageous; you are no less! This is why, although there is some conflict, you are still successful. Why? Because you have the key of determination with you. Where there is determination there is definitely success. There is no question as to whether or not there will be success. There is success! However, according to the atmosphere, a few situations will come, but maintain courage and consider those things to be side scenes and continue to move forward. You have played a good part. You have very good love for your State. And this one is your companion. She is your companion, is she not? She co­operates with you, does she not? And who are these? (secretary and security.) Very good!

You showed many devotees the path of devotion and so you receive the fruit of that because that is a good task. It is not a bad task, and the fruit of a good task is happiness and lightness. This is the fruit. It is good. It is a wonder! Your secretary is very faithful. Look, if the secretary does not co­operate, then the task cannot be accomplished. This is why thanks are given to the secretary because he is giving you co­operation.

Achcha, are you a BK? Achcha, who is the creator of the world? The creator of the world is Brahma. Do you believe that? Brahma carries out establishment, Vishnu sustains it and it is Shankar who destroys the old world. You know about all three, do you not? Therefore, are you not the creation of Brahma? So all of you are Brahma Kumars. The creator is Brahma and so all are Brahma Kumars. It is just that you now have to recognise Father Brahma a little. You did very well! Look, you understand what a mike is. A mike is someone who comes on to the stage of service. Therefore, you have played a good part in becoming a mike. You have fulfilled your duty very well in giving a message to all of those in your assembly. Whether they accepted it or not or followed it or not, you still fulfilled your duty. This is your first example. This is why BapDada is happy and He is also happy with your companions. (He has given everyone inspiration to do meditation.) BapDada has heard about it. You have maintained courage. (His vision is to create a beautiful Andhra.) Yes, why should you not create that? Everything has to be made beautiful.

BapDada meeting guests that came for The Call of the Time Programme:

Do all of you feel that this is your home? Is this your home? Have you ever seen such a big Godly family? Have you ever seen it? You have never seen it. You are so fortunate that you have reached such a big Godly family. All of you had a very good experience. In future too, continue to increase this experience by keeping your connection. The connection is necessary, isn't it? The more you continue to keep in connection, the more your experiences will continue to grow. Now you are becoming messengers. You are messengers, are you not? Are you messengers? Give others the message that you have received and make them tension­free. There is so much tension in the world today. So you experience being tension­free and then give others this experience. You will give this experience, will you not? It is good! All of you who have come are special. You have speciality in you. Now use that speciality and it will continue to increase even more, just as a seed is filled with everything, but it won't bear fruit until it is sown in the ground. So all of you have the seed of speciality. Now put that into practice and you will continue to move ahead. Is this all right? Achcha. They have done service. You have done good service. You have prepared a group and also made good plans. Achcha. You are all very happy, are you not? Achcha.

BapDada personally hoisted the flag for the 65th Trimurti Shiva Jayanti and gave congratulations to all the children, lit the candles and cut the cake.

All of you hoisted the flag. The hands were of just a few, but the hands of all of you were with the Father's hand. Those who are sitting at the back also hoisted the flag with everyone. The Father's flag is hoisted on everyone's face and in everyone's heart. This is visible in your faces. So you have hoisted the flag in your heart and you have also hoisted the material flag in many different places. Now hoist the flag of revelation as quickly as possible. Take this vow, take a vow of a firm promise that you will very quickly hoist the flag of the glorification of the Father's name. Now make the unhappy world go to the land of liberation and liberation­in­life. They are all very unhappy. Therefore, have mercy! Now liberate them from sorrow! Give everyone the Father's inheritance of liberation because they are very distressed. You are in your pure pride (shaan) and they are distressed (par­e­ shaan). Never move away from serving through the mind. Constantly continue to do service. Continue to spread this atmosphere. You are the children of the Bestower of Happiness. Therefore, continue to spread an atmosphere of happiness. This is what it means to celebrate. Have you celebrated Shiv Ratri? Did all of you celebrate it? Did all of you here celebrate it? Did those sitting on the chairs celebrate it? Did those sitting at the back celebrate it? Did those sitting on this side celebrate it? Did those sitting in the gallery celebrate it? All of you celebrated it together? Congratulations to everyone! Congratulations! Congratulations! Congratulations! """


# #**Split the Text into Chunks**

# In[36]:


data


# In[37]:


#data1 = [{"page_content": data}]
from langchain.schema import Document

data1 = [Document(page_content=data)]
print(data1)


# In[55]:


text_splitter=RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0, separators=["\n\n", "\n"],)


# In[50]:


docs= text_splitter.split_documents(data1)


# In[51]:


len(docs)


# In[57]:


docs[1]


# #**Setup the Environment**

# In[58]:


PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY', '5dbf1d73-7ca2-4c88-b952-dc315eb86f98')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV', 'us-east-1')


# #**Downlaod the Embeddings**

# In[44]:


embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')


# #**Initializing the Pinecone**

# In[65]:


from pinecone import Pinecone, ServerlessSpec

# Replace with your actual Pinecone API key and environment
PINECONE_API_KEY = '5dbf1d73-7ca2-4c88-b952-dc315eb86f98'
PINECONE_API_ENV = 'us-east-1'

# Initialize Pinecone
pc = Pinecone(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_API_ENV
)

# Define the index name
index_name = "pinecone"

# Example of checking and creating an index
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,  # Adjust to the dimension of your embeddings
        metric='euclidean',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-west-2'
        )
    )


# #**Create Embeddings for Each of the Text Chunk**

# In[66]:


# get_ipython().system('pip install pinecone')


# In[67]:


#docsearch=Pinecone.from_documents([t.page_content for t in docs], embeddings, index_name=index_name)
from langchain.vectorstores import Pinecone
import pinecone

os.environ["PINECONE_API_KEY"] ='5dbf1d73-7ca2-4c88-b952-dc315eb86f98'


# Assuming you already have embeddings and docs
docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)


# #**Similarity Search**

# In[71]:


query="which are eastern zones"


# In[72]:


docs=docsearch.similarity_search(query)


# In[73]:


# Perform similarity search with the query
docs = docsearch.similarity_search(query)

# Display the top 1 chunk
if docs:
    print(f"Top 1 Chunk:\n{docs[0].page_content}\n")
else:
    print("No results found.")


# In[ ]:




