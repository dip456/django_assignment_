"""What is a QuerySet ? Write program to create a new Post object in database:"""

"""
    QuerySet is a collection of database query results. It represents a set of database rows that match
    a specific query. QuerySets allow you to interact with the database using Python, enabling you to 
    retrieve, filter, update, and delete data from the database.


1. import model :
   from myapp.models import PostModel

2. data = {
    'title': 'Assignment',
    'content': 'This is assignment.'
}

3. creates a new Post object : 
   new_post = Post(**data)

4. new_post.save()

5. prints a confirmation message:

   print("New post created with title:", new_post.title)


   

    
"""