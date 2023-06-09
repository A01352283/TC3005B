import nltk
from nltk.corpus import stopwords
import pandas as pd

def count_stopwords(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)

    # Get the set of Spanish stopwords
    spanish_stopwords = set(stopwords.words('spanish'))

    # Initialize counters
    stopwords_count = 0
    non_stopwords_count = 0

    # Count stopwords and non-stopwords
    for word in words:
        if word.lower() in spanish_stopwords:
            stopwords_count += 1
        else:
            non_stopwords_count += 1

    return stopwords_count, non_stopwords_count


def getStopWordsProportion():
    # Read the CSV file
    df = pd.read_csv('./GenerateDummyData/finalScrapedExpandedDescription_20230531201457.csv')

    # Initialize the stopwords proportion column
    df['stopwords_proportion'] = 0

    # For each row in the dataframe
    for index, row in df.iterrows():
        # Get the description
        description = row['descripcion']

        # Count the stopwords and non-stopwords
        stopwords_count, non_stopwords_count = count_stopwords(description)

        # Calculate the proportion of stopwords
        stopwords_proportion = stopwords_count / (stopwords_count + non_stopwords_count)

        # Add the proportion to the dataframe
        df.loc[index, 'stopwords_proportion'] = stopwords_proportion

    # Get the average proportion of stopwords
    average_stopwords_proportion = df['stopwords_proportion'].mean()

    # Print the average proportion of stopwords
    print(f"Average proportion of stopwords: {average_stopwords_proportion}")

    # Save the dataframe to a CSV file
    df.to_csv('./GenerateDummyData/stopWordProportions.csv', index=False)

def getDescriptionWordCount():
    # Read the CSV file
    df = pd.read_csv('./GenerateDummyData/finalScrapedExpandedDescription_20230531201457.csv')

    # Initialize the word count column
    df['description_word_count'] = 0

    # For each row in the dataframe
    for index, row in df.iterrows():
        # Get the description
        description = row['descripcion']

        # Count the words in the description
        word_count = len(description.split())

        # Add the word count to the dataframe
        df.loc[index, 'description_word_count'] = word_count

    # Get the average word count
    average_word_count = df['description_word_count'].mean()

    # Print the average word count
    print(f"Average word count: {average_word_count}")

    # Save the dataframe to a CSV file
    df.to_csv('./GenerateDummyData/descriptionWordCount.csv', index=False)

getDescriptionWordCount()
