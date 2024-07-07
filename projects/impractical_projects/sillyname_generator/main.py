import random
import sys

print('Welcome to Silly Name Generator!\n\n')

# List of 100 silly first names
silly_first_names = [
    "Wobble", "Fizz", "Snork", "Bibble", "Ziggy", "Gloop", "Bumble", "Quirk", "Doodle", "Wibble",
    "Fluffy", "Mumble", "Tink", "Jabber", "Frodo", "Giggle", "Snuggle", "Noodle", "Blip", "Zoodle",
    "Fuzzle", "Twiddle", "Bloop", "Dizzy", "Blinky", "Sprinkle", "Wiggle", "Nifty", "Bingo", "Pip",
    "Bongo", "Gizmo", "Puff", "Toodle", "Wacky", "Chirpy", "Zappy", "Wizzle", "Wizzle", "Zigzag",
    "Fizzy", "Giddy", "Snazzy", "Nibbles", "Pudding", "Squirt", "Boogie", "Funky", "Tiddly", "Muffin",
    "Tickle", "Scooter", "Zippity", "Twitch", "Bouncy", "Jiffy", "Flicker", "Pookie", "Zippy", "Tango",
    "Snickerdoodle", "Bubbles", "Twinkle", "Snazzy", "Peppy", "Bibbity", "Dizzy", "Squiggle", "Wobbly",
    "Tootsie", "Puddles", "Whiskers", "Snickers", "Wacky", "Zigzag", "Frolic", "Snappy", "Gooey", "Scooby",
    "Fizz", "Zappy", "Giggly", "Waffle", "Snuggle", "Zoodle", "Wiggles", "Jiggly", "Womble", "Snicker",
    "Doodle", "Bing", "Wobble", "Bibble", "Ziggy", "Gloop", "Bumble", "Quirk", "Doodle", "Wibble"
]

# List of 100 silly last names
silly_last_names = [
    "Wobblebottom", "Fizzwhistle", "Snorklefoot", "Bibblepants", "Ziggletoes", "Gloopington", "Bumblefluff", "Quirkmire", "Doodlepuff", "Wibblewink",
    "Fluffernutter", "Mumblecrumb", "Tinkertop", "Jabberquack", "Frodowinkle", "Gigglesnort", "Snuggleton", "Noodlefish", "Blipblop", "Zoodlebum",
    "Fuzzlebop", "Twiddlewink", "Bloopnugget", "Dizzywhirl", "Blinkybop", "Sprinklefish", "Wigglesnort", "Niftypop", "Bingobop", "Pipplesnort",
    "Bongosnuff", "Gizmocrunch", "Puffenstuff", "Toodlepip", "Wackywig", "Chirpyfluff", "Zappyfizz", "Wizzlebop", "Wizzlepop", "Zigzagwig",
    "Fizzyfluff", "Giddywhirl", "Snazzywinkle", "Nibblesnort", "Puddingpop", "Squirtywig", "Booglesnort", "Funkyfluff", "Tiddlywink", "Muffintop",
    "Tickletop", "Scooterwig", "Zippitysnap", "Twitchwig", "Bouncypuff", "Jifflesnort", "Flickersnuff", "Pookiepop", "Zippysnort", "Tangofluff",
    "Snickerdoodlewig", "Bubblesnort", "Twinkletoes", "Snazzywhirl", "Peppypop", "Bibbityboop", "Dizzywig", "Squigglewig", "Wobblesnort",
    "Tootsiewig", "Puddlesnort", "Whiskersnuff", "Snickersnort", "Wackybop", "Zigzagwig", "Frolicwig", "Snappybop", "Gooeywig", "Scoobyfluff",
    "Fizzwig", "Zappysnort", "Gigglywig", "Wafflepop", "Snugglewig", "Zoodlepop", "Wigglesnort", "Jigglywig", "Womblesnort", "Snickerwig",
    "Doodlewig", "Bingwig", "Wobblewig", "Bibblewig", "Ziggywig", "Gloopwig", "Bumblewig", "Quirkwig", "Doodlewig", "Wibblewig"
]

while True:
    print('Generated silly name is...\n\n')
    # print(f'{random.choice(silly_first_names), random.choice(silly_last_names)}')
    print("{} {}\n\n" .format(random.choice(silly_first_names), random.choice(silly_last_names)))
    try_again = input('Press enter to continue or q to exit!\n')
    if try_again == 'q':
        sys.exit(1)