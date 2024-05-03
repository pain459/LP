from flask import Flask, jsonify, request
from itertools import permutations
from main import load_wordnet, validate_word

app = Flask(__name__)
wordnet_dict = load_wordnet()

# Points per card dictionary
points_per_card = {
    'A': 10, 'B': 2, 'C': 8, 'D': 6, 'E': 10, 'F': 2, 'G': 4, 'H': 8, 'I': 10, 'J': 6,
    'K': 8, 'L': 8, 'M': 8, 'N': 8, 'O': 8, 'P': 8, 'Q': 4, 'R': 8, 'S': 8, 'T': 8,
    'U': 8, 'V': 6, 'W': 8, 'X': 2, 'Y': 4, 'Z': 2
}

def calculate_word_points(word):
    # Calculate total points for a given word based on points per card
    return sum(points_per_card.get(letter, 0) for letter in word)
def generate_possible_words(cards):
    # Find all possible permutations of the cards
    card_permutations = [''.join(permutation) for r in range(3, len(cards) + 1) for permutation in permutations(cards, r)]

    # Validate each combination of cards and find valid words with points
    valid_words_with_points = {}
    for card_combination in card_permutations:
        is_valid, _ = validate_word(card_combination, wordnet_dict)
        if is_valid:
            word_points = calculate_word_points(card_combination)
            valid_words_with_points[card_combination] = word_points

    # Sort possible words by points (highest to lowest) and return top 10
    sorted_words_with_points = sorted(valid_words_with_points.items(), key=lambda x: x[1], reverse=True)
    top_10_words_with_points = sorted_words_with_points[:10]

    return dict(top_10_words_with_points)



@app.route('/api/validate-cards', methods=['POST'])
def validate_cards():
    # Get list of players and their cards from the request
    players = request.json.get('players', {})

    # Ensure at least one player is provided
    if not players:
        return jsonify({'error': 'Please provide at least one player'}), 400

    # Generate possible words for each player's hand
    player_hands = {}
    for player, cards in players.items():
        # Ensure each player receives 10 cards per turn
        if len(cards) != 10:
            return jsonify({'error': f'Player {player} does not have 10 cards in hand'}), 400

        # Generate possible words from the player's hand with points
        possible_words_with_points = generate_possible_words(cards)

        # Sort possible words by points (highest to lowest)
        sorted_words_with_points = sorted(possible_words_with_points.items(), key=lambda x: x[1], reverse=True)

        player_hands[player] = {'cards': cards, 'possible_words': sorted_words_with_points}

    return jsonify({'player_hands': player_hands})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
