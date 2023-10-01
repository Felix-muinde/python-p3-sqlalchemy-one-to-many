#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///one_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()

    # Inside the interactive debugging session, you can perform CRUD operations:
    # For example, let's create a new game and its associated reviews:
    
    # Create a new Game
    new_game = Game(name="Sample Game", platform="PC")

    # Add reviews to the game
    review1 = Review(title="Great Game!", content="I loved it.", game=new_game)
    review2 = Review(title="Not so good", content="Could be better.", game=new_game)

    # Add the game and reviews to the session
    session.add(new_game)
    session.add(review1)
    session.add(review2)

    # Commit the changes to the database
    session.commit()

    # Retrieve and print the game with its reviews
    game_with_reviews = session.query(Game).filter_by(name="Sample Game").first()
    if game_with_reviews:
        print(f"Game: {game_with_reviews.name}, Platform: {game_with_reviews.platform}")
        print("Reviews:")
        for review in game_with_reviews.reviews:
            print(f"  Title: {review.title}, Content: {review.content}")

    # You can also update and delete records as needed within the session.
