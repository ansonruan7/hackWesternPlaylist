# import cohere
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
# from spotifyGen import addSongs

# global importedSongNames
# importedSongNames = []

# def main():
#     # Prompt user for input
#     userPrompt = input("Enter a prompt:")
#     songType = input("Enter a song type:")

#     while (True):

#             #Cohere API call
#         co = cohere.Client('xYbpMlrGHoL1cHWKh7yw2Q5zAEu7ZNJ67TGKWF7B')
#         response = co.generate(
#             model='command-xlarge-20221108',
#             prompt='List 10' +songType+ 'songs about the keywords of' +userPrompt+':',
#             max_tokens=200,
#             temperature=5, #Control the randomness aspect of which tokens the model picks for output (2 - least random)
#             k=0,
#             p=0.75,
#             frequency_penalty=0.4, #to reduce repetition in output
#             presence_penalty=0,
#             stop_sequences=[],
#             return_likelihoods='NONE')

#         output = '{}'.format(response.generations[0].text)
#         output = output.strip()


#         if (output[0:4] =='1. "'): #Validation check, whether it is a song list or not
#             break


#     #Split the output into a list of songs

#     splited_Output = output.split("\n")

#     songList = []

#     for song in splited_Output:
#         song = song[4:song.rindex('" by ')] #retreive song name
#         # song = song.strip() #remove whitespace
#         songList.append(song)
    
#     searchTracks(songList)


# def searchTracks(queryList):
#     #Uses spotify api
#     auth_manager = SpotifyClientCredentials()
#     sp = spotipy.Spotify(auth_manager=auth_manager)
#     names = []
#     for query in queryList:
#       b = sp.search(query,len(queryList),0,"track",None)
#       addSongs(b['tracks']['items'][0]['uri'])
#       names.append(b['tracks']['items'][0]['name'])
#     importedSongNames = names
  
  
# def getImportedSongs():
#   #returns list of string uris
#   return importedSongNames
  
# def flaskTrans(sentence):
#    # Prompt user for input
#     userPrompt = sentence
#     songType = input("Enter a song type:")

#     while (True):

#             #Cohere API call
#         co = cohere.Client('xYbpMlrGHoL1cHWKh7yw2Q5zAEu7ZNJ67TGKWF7B')
#         response = co.generate(
#             model='command-xlarge-20221108',
#             prompt='List 10' +songType+ 'songs about the keywords of' +userPrompt+':',
#             max_tokens=200,
#             temperature=5, #Control the randomness aspect of which tokens the model picks for output (2 - least random)
#             k=0,
#             p=0.75,
#             frequency_penalty=0.4, #to reduce repetition in output
#             presence_penalty=0,
#             stop_sequences=[],
#             return_likelihoods='NONE')

#         output = '{}'.format(response.generations[0].text)
#         output = output.strip()


#         if (output[0:4] =='1. "'): #Validation check, whether it is a song list or not
#             break


#     #Split the output into a list of songs

#     splited_Output = output.split("\n")

#     songList = []

#     for song in splited_Output:
#         song = song[4:song.rindex('" by ')] #retreive song name
#         # song = song.strip() #remove whitespace
#         songList.append(song)
    
#     searchTracks(songList)





# if __name__ == '__main__':
#     main()