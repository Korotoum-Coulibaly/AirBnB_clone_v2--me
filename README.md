# 0x00.AirBnB clone - The console

--
##Ressources

*https://docs.python.org/3.8/library/cmd.html
*http://pymotw.com/2/cmd/
*packages concept page
*https://docs.python.org/3.8/library/uuid.html
*https://docs.python.org/3.8/library/datetime.html
*https://docs.python.org/3.8/library/unittest.html#module-unittest
*https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/
*https://www.pythonsheets.com/notes/python-tests.html
*https://wiki.python.org/moin/CmdModule
*https://realpython.com/python-testing/

--
##Learning Objectives

Explain: 
*How to create a python package
*How to create a command interpreter in Python using the cmd module
*What is Unit testing and how to implement in a large project
*How to serialize and deserialize a class
*How to write and read a Json file
*How to manage datetime
*What is an UUID
*What is *args and how to use it
*What is *kwargs and how to use it
*How to handle named arguments in a function

--
##Description of the project

The AirBnB clone project starts now until...the end of the first year.The goal of the project is to deploy on your server a simple copy of the AirBnB website.
You won't implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.
After 4 months, you will have a complete web application composed by:
*A command interpreter to manipulate data without a visual interface, like in a shell(perfect for development and debugging)
*A website(the front-end that shows the final product to everybody: static and dynamic
*A database or files that store data(data = objects)
*An API that provides a communication interface between the front-end and your date(retrieve, create, delete, update them)

for this first steps i make The console
###The console

This first piece is to manipulate a powerful storage system.This storage engine will give us an abstraction between "My object" and "How they are stored and persisted".This means: from your console code(the command interpreter itself) and from the front-end and RestAPI you will build later, you won't have to pay attention (take care) of how your objects are stored.

This abstration will also allow you to change the type of storage easily without updating all of your codebase.
The console will be tool to validate this storage engine https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230320%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230320T095827Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e8d429c904ce88764053d43597cd3ce2379aa4a8a5d80f2e121795bdb39f5f2a

--
##Important
A class, called "model" in a OOP project is the representation of an object/instance.
A data is model.
##Description of the command interpreter

Do you remember the Shell?It's exactly the same but limited to a specific use-case.
###How to start it

###How to use it

###Examples

--

