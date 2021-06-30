
![airbnb-logo-FB](https://user-images.githubusercontent.com/70924466/124042441-78e9a300-d9ce-11eb-9eac-4b600f571267.png)
# Airbnb

this is the first part of a big project in which we create a copy of Airbnb, which can create objects and interact with them

# How to start it

git clone https://github.com/ManuBedoya/AirBnB_clone.git

# How to use

now we will see the different commands that we can use in our interpreter

# Create

this command creates a new instance of the 'class-name' and returns the id of that same instance saving it in a file.json

    (hbnb) create User
    eddce1c0-72a1-4b13-b4c0-3cd523554895


# Show 

return the string representation of an instance based on its name and id


    (hbnb) show eddce1c0-72a1-4b13-b4c0-3cd523554895
    ** class doesn't exist **
    (hbnb) show User eddce1c0-72a1-4b13-b4c0-3cd523554895
    [User] (eddce1c0-72a1-4b13-b4c0-3cd523554895) {'id': 'eddce1c0-72a1-4b13-b4c0-3cd523554895', 'created_at': datetime.datetime(2021, 6, 30, 18, 14, 45, 150811), 'updated_at':     datetime.datetime(2021, 6, 30, 18, 14, 45, 150863)}
    (hbnb)

# Destroy 

delete the string representation of an instance based on its name and id

    (hbnb) destroy User eddce1c0-72a1-4b13-b4c0-3cd523554895
    (hbnb) show User eddce1c0-72a1-4b13-b4c0-3cd523554895
    ** no instance found **
    (hbnb)

# All

it return all the instances created based on the name and if this is not there, it will print all the instances that have valid names 

    (hbnb) create User
    b4e589cc-d006-48cb-9671-7a311443ba4f
    (hbnb) all User
    ["[User] (b4e589cc-d006-48cb-9671-7a311443ba4f) {'id': 'b4e589cc-d006-48cb-9671-7a311443ba4f', 'created_at': datetime.datetime(2021, 6, 30, 18, 17, 53, 91952), 'updated_at':     datetime.datetime(2021, 6, 30, 18, 17, 53, 91971)}"]
    (hbnb) create BaseModel
    50bc434a-9eba-4c21-8f76-d7c55425ee81
    (hbnb) all
    ["[User] (b4e589cc-d006-48cb-9671-7a311443ba4f) {'id': 'b4e589cc-d006-48cb-9671-7a311443ba4f', 'created_at': datetime.datetime(2021, 6, 30, 18, 17, 53, 91952), 'updated_at':     datetime.datetime(2021, 6, 30, 18, 17, 53, 91971)}", "[BaseModel] (50bc434a-9eba-4c21-8f76-d7c55425ee81) {'id': '50bc434a-9eba-4c21-8f76-d7c55425ee81', 'created_at':          datetime.datetime(2021, 6, 30, 18, 18, 1, 348232), 'updated_at': datetime.datetime(2021, 6, 30, 18, 18, 1, 348247)}"]
    (hbnb)

# Update

update an instance of the 'class-name' with an id, an attribute and a value, if none of these are not found the program will get an error

    (hbnb) create User
    514f059e-b033-448d-831b-b18fc7c0f5f3
    (hbnb) update User 514f059e-b033-448d-831b-b18fc7c0f5f3 first_name "Betty"
    (hbnb) show User 514f059e-b033-448d-831b-b18fc7c0f5f3
    [User] (514f059e-b033-448d-831b-b18fc7c0f5f3) {'id': '514f059e-b033-448d-831b-b18fc7c0f5f3', 'created_at': datetime.datetime(2021, 6, 30, 18, 19, 36, 83099), 'updated_at':    datetime.datetime(2021, 6, 30, 18, 19, 36, 83112), 'first_name': 'Betty'}
    (hbnb)

# Help

use this command to see information about the commands of the interface

    (hbnb) help
    
    Documented commands (type help <topic>):
    ========================================
    EOF  all  create  destroy  help  quit  show  update

    (hbnb)
    
# Authors

Daniel Escobar < fdnate@gmail.com >
Manuel Bedoya < manuelfernandobedoya@gmail.com >
