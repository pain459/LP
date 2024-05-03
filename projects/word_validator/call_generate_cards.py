import requests

def test_api(cards):
    # Define the URL of the API endpoint
    url = 'http://localhost:5000/api/validate-cards'

    # Make a POST request with the player's cards
    response = requests.post(url, json={'players': {'Player1': cards}})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the player hand with possible words and points returned by the API
        player_hand = response.json()['player_hands']['Player1']
        print("Cards in hand:", player_hand['cards'])
        print("Possible words with points:")
        for word, points in player_hand['possible_words']:
            print(f"    {word}: {points} points")
    else:
        # Print the error message if the request was not successful
        print("Error:", response.json()['error'])

if __name__ == '__main__':
    # Sample cards for one player
    cards = ['D', 'I', 'C', 'T', 'I', 'O', 'N', 'A', 'R', 'Y']

    # Call the test function with the sample cards
    test_api(cards)
