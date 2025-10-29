# FAST API PROJECT

This is a basic project using fastAPI, you use the following opperations:

POST (http://localhost:8000/items)


creates an item.

example of body:



    {
        "nombre": "item1",
        "precio": "10"
    }


GET (http://localhost:8000/items)

gets all Items.

example of response:


    [
        {
            "nombre": "item1",
            "precio": "10",
            "id": 1
        },
        {
            "nombre": "item2",
            "precio": "20",
            "id": 2
        }
    ]



GET (http://localhost:8000/items/{ID})

gets one Item.

example of response:



    
    {
        "nombre": "item1",
        "precio": "10",
        "id": 1
    }



TO RUN: 

Execute the following command:


    uvicorn app.main:app --reload

