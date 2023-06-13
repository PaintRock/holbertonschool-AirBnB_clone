![image](https://github.com/PaintRock/holbertonschool-AirBnB_clone/assets/122139376/6ec97612-3f56-43e6-9b1b-62120dd08b2d)





# AirBnB Clone - The Console
The command interpreter module to Manage AirBnB objects.

## Project Notes
### Environment
Files interpreted/run on Ubuntu 14.04 LTS with Python 3
### Style
All code is written in accordance with Pep8 https://www.python.org/dev/peps/pep-0008/

<details><summary> Description of the Project </summary>

<p>

<h2>Description</h2>

This is the first part of the project Holberotnn AirBNB clone web application by developing a command interpreter using Python. The command interpreter serves as a management system for AirBnB objects, allowing users to create, update, delete, and retrieve data related to various entities such as users, states, cities, places, and more. The project encompasses several tasks, including implementing a parent class for initialization and serialization, creating a serialization flow, defining classes for AirBnB entities, building a file storage engine, and validating classes and storage engine with unittests.

</p>

</details>

<details><summary> How to Use the Console? </summary>

<p>

To start:

<h3>Interactive Mode</h3>

`User$ ./console.py`
  
  which returns a 
  '(hbnb)'
  prompt
  

<h3>Non-interactive Mode</h3>

` User$ echo "help" | ./console.py`
  
 </p>

</details>

</p>

</details>

<details><summary> Description of the Command Interpreter </summary>

<p>

<h2>The Command Interpreter</h2>

The command interpreter is a command-line interface that provides interaction with the AirBnB clone and enables users to manage the objects within the application. Here are the details on how to start and use the command interpreter: How to Start the Command Interpreter.

The first thing is to manipulate the storage system. This will give us an abstraction of our objects, how they are stored and how they are persisted, via JSON files, which means we don't have to look at how our objects are stored. This abstraction will also allow us to change the storage type easily without updating our entire database.

The console will be used to validate that this storage engine is working properly.

</p>

<p>

To start using the interpreter, write one of these lines of code:

<h3>Interactive Mode</h3>

`User$ ./console.py`

<h3>Non-interactive Mode</h3>

` User$ "user command" | ./console.py`

</p>

</details>

<details><summary> Commands Inside the Interpreter </summary>

<p>

<h2>All the Commands You Can Use</h2>


- quit - Use it to exit the console, only in interactive mode
- create - Creates an instance - Needs: Class - Usage: create Class
- show - Prints the string representation of an instance - Needs: Class and id - Usage: show specific Class with ID
- destroy - Deletes an intance - Use: Class and id - Usage: destroy specific Class with ID
- all - Prints all string representation of all instance - Needs: Optional (Class) - Usage: show all or all of a specific class
- update - Updates an instance - Use: Class, id, attribute and value for the attribute - Usage: update value attribute of specific Class with ID

</p>

</details>

<details><summary> Usage Examples </summary>

<p>

<h2>Examples</h2>

<details><summary> "Create" Examples </summary>

<p>

```
(hbnb) create BaseModel
60d4e689-a246-405b-9d42-88428f99a105
(hbnb) create BaseModel
09de3adc-993d-44c0-8a7a-f62c62e8e870
(hbnb) create User
9dc47629-ad61-442d-8865-c82aedfa0ee5
(hbnb) create Place
d7820d61-423c-44e3-aa7b-0018ca8c66a8
(hbnb) create alligatorMeat
** class doesn't exist **
(hbnb) create
** class name missing **
```

</p>

</details>

<details><summary> "Show" Examples </summary>

<p>

```
(hbnb) show BaseModel 09de3adc-993d-44c0-8a7a-f62c62e8e870
[BaseModel] (09de3adc-993d-44c0-8a7a-f62c62e8e870) {'id': '09de3adc-993d-44c0-8a7a-f62c62e8e870', 'created_at': datetime.datetime(2022, 10, 28, 17, 14, 40, 440464), 'updated_at': datetime.datetime(2022, 10, 28, 17, 14, 40, 440474)}
(hbnb) show BaseModel 60d4e689-a246-405b-9d42-88428f99a105
[BaseModel] (60d4e689-a246-405b-9d42-88428f99a105) {'id': '60d4e689-a246-405b-9d42-88428f99a105', 'created_at': datetime.datetime(2022, 10, 28, 17, 13, 57, 826499), 'updated_at': datetime.datetime(2022, 10, 28, 17, 13, 57, 826512)}
(hbnb) show BaseModel FrodoVillage
** no instance found **
(hbnb) show BaseModel 
** instance id missing **
(hbnb) show AlligatorMeat
** class doesn't exist **
(hbnb) show 
** class name missing **
```

</p>

</details>

<details><summary> "Destroy" Examples </summary>

<p>

```
(hbnb) destroy BaseModel 09de3adc-993d-44c0-8a7a-f62c62e8e870
(hbnb) show BaseModel 09de3adc-993d-44c0-8a7a-f62c62e8e870
** no instance found **
(hbnb) destroy BaseModel NinjaDoom
** no instance found **
(hbnb) destroy BaseModel 
** instance id missing **
(hbnb) destroy AlligatorMeat
** class doesn't exist **
(hbnb) destroy 
** class name missing **
```

</p>

</details>

<details><summary> "All" Examples </summary>

<p>

```
(hbnb) all BaseModel
["[BaseModel] (60d4e689-a246-405b-9d42-88428f99a105) {'id': '60d4e689-a246-405b-9d42-88428f99a105', 'created_at': datetime.datetime(2022, 10, 28, 17, 13, 57, 826499), 'updated_at': datetime.datetime(2022, 10, 28, 17, 13, 57, 826512)}"]
(hbnb) all User
["[User] (9dc47629-ad61-442d-8865-c82aedfa0ee5) {'id': '9dc47629-ad61-442d-8865-c82aedfa0ee5', 'created_at': datetime.datetime(2022, 10, 28, 17, 14, 52, 306321), 'updated_at': datetime.datetime(2022, 10, 28, 17, 14, 52, 306330)}"]
(hbnb) all Place
["[Place] (d7820d61-423c-44e3-aa7b-0018ca8c66a8) {'id': 'd7820d61-423c-44e3-aa7b-0018ca8c66a8', 'created_at': datetime.datetime(2022, 10, 28, 17, 14, 59, 257449), 'updated_at': datetime.datetime(2022, 10, 28, 17, 14, 59, 257458)}"]
(hbnb) all aleatory
** class doesn't exist **
(hbnb) all
["[BaseModel] (60d4e689-a246-405b-9d42-88428f99a105) {'id': '60d4e689-a246-405b-9d42-88428f99a105', 'created_at': datetime.datetime(2022, 10, 28, 17, 13, 57, 826499), 'updated_at': datetime.datetime(2022, 10, 28, 17, 13, 57, 826512)}", "[User] (9dc47629-ad61-442d-8865-c82aedfa0ee5) {'id': '9dc47629-ad61-442d-8865-c82aedfa0ee5', 'created_at': datetime.datetime(2022, 10, 28, 17, 14, 52, 306321), 'updated_at': datetime.datetime(2022, 10, 28, 17, 14, 52, 306330)}", "[Place] (d7820d61-423c-44e3-aa7b-0018ca8c66a8) {'id': 'd7820d61-423c-44e3-aa7b-0018ca8c66a8', 'created_at': datetime.datetime(2022, 10, 28, 17, 14, 59, 257449), 'updated_at': datetime.datetime(2022, 10, 28, 17, 14, 59, 257458)}"]
```

</p>

</details>

<details><summary> "Update" Examples </summary>

<p>

```
(hbnb) show Place d7820d61-423c-44e3-aa7b-0018ca8c66a8
[Place] (d7820d61-423c-44e3-aa7b-0018ca8c66a8) {'id': 'd7820d61-423c-44e3-aa7b-0018ca8c66a8', 'created_at': datetime.datetime(2022, 10, 28, 17, 14, 59, 257449), 'updated_at': datetime.datetime(2022, 10, 28, 17, 14, 59, 257458)}
(hbnb) update Place d7820d61-423c-44e3-aa7b-0018ca8c66a8 number_rooms 3
(hbnb) show Place d7820d61-423c-44e3-aa7b-0018ca8c66a8
[Place] (d7820d61-423c-44e3-aa7b-0018ca8c66a8) {'id': 'd7820d61-423c-44e3-aa7b-0018ca8c66a8', 'created_at': datetime.datetime(2022, 10, 28, 17, 14, 59, 257449), 'updated_at': datetime.datetime(2022, 10, 28, 17, 14, 59, 257458), 'number_rooms': '3'}
(hbnb) update Place d7820d61-423c-44e3-aa7b-0018ca8c66a8 number_rooms 
** value missing **
(hbnb) update Place d7820d61-423c-44e3-aa7b-0018ca8c66a8
** attribute name missing **
(hbnb) update Place FrodoVillage
** no instance found **
(hbnb) update Place 
** instance id missing **
(hbnb) update alligatorMeat
** class doesn't exist **
(hbnb) update 
** class name missing **
```

</p>

</details>

<details><summary> "Quit" Examples </summary>

<p>

```
(hbnb) quit
User$ 
```

</p>

</details>

</p>

</details>

</p> 

</details>

<details><summary> Authors </summary>
  
  ## Authors
* Alton Andrews, <a href='https://github.com/AAndrews-1982'>Github</a>
* Adel Knode, <a href='https://github.com/PaintRock'>Github</a>
