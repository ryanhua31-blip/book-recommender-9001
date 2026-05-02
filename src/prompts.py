def get_prompt(liked_books, liked_genres, unliked_books, unliked_genres):
    return f"""
    Make a list of 6 books that the user would probably like to read 
    based on the books they like and the genres they like. 
    Make sure to exclude books from the kinds of books they don't like 
    and genres they don't like.
    Do not recommend books in the same series as the ones the user likes.
    Respond with JSON format
    """ + """
    {
        "Recommendations": [
            { 
                "name": "{book name}", 
                "author": "{name of author}", 
                "description": "{description of book}"
            },
            { 
                "name": "{book name}", 
                "author": "{name of author}", 
                "description": "{description of book}"
            }
        ]
    }
    """ + f"""
    Books they like:
    {liked_books}

    Genres they like:
    {liked_genres}

    Books they Don't like:
    {unliked_books}

    Genres they Don't like:
    {unliked_genres}
    """

def get_prompt_image():
    return """
    Get the ISBN numbers for each of the books I will give you.
    Return in this JSON format:
    {
        "{name}" : {isbn}
    }

    """