from flask import Flask, render_template, request
from signup import create_user
from login import check_user
from tree import *
import csv
from selfsortingarray import *

val=SelfSortingArray()
lst=val.array
print(lst)

def insert_value(filename, value):
    with open(filename, "a") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(value)

global USER 
USER=None
ADMIN=None

app = Flask(__name__)

@app.route('/')
def signup_form():
    return render_template('user_choice.html')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    print(create_user(name,email,password))
    return render_template('sign_up_successful.html')

@app.route('/login')
def prender():
    return render_template('user_login.html')

@app.route('/sign_up')
def render():
    return render_template('sign_up_page.html')

@app.route('/userlogin')
def login_form():
    return render_template('user_login.html')

@app.route('/admin_login')
def admin_form():
    return display_tables()

@app.route('/add_table',methods=['POST'])
def display_tables():
    table_data = []
    with open("table_data.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            table_data.append(row)

    return render_template("display_tables.html", table_data=table_data)

@app.route('/add_tables',methods=['POST'])
def display_table():

    print('in')
    seats=request.form['block_name']
    x=SelfSortingArray()
    x.insert(int(seats))
    table_data = []
    with open("table_data.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            table_data.append(row)

    return render_template("display_tables.html", table_data=table_data)


@app.route('/admin_add_table')
def admin_add_table():
    # Function to handle the admin_add_table.html page
    # Add the necessary logic for the admin_add_table page here
    return render_template("admin_add_table.html")

@app.route('/user_res',methods=['POST'])
def login():
    # Access the form data
    username = request.form['username']
    password = request.form['password']

    if check_user(username,password):
        return render_template('add_reservation.html')
    

@app.route('/reservation',methods=['POST'])
def reserve():
    val=SelfSortingArray()
    lst=val.array
    seat = request.form['seat']
    date = request.form['date']
    hour = request.form['hour']
    minute = request.form['minute']
    booking_time=str(hour)+':'+str(minute)

    next_element = find_immediate_next_element(lst, int(seat))
    print('ejcieji',next_element)
    if next_element is None:
        print("No immediate next element found in the list")
        return render_template('reservation_unsuccessful.html')
    else:
        duration=1
        table_num = book_table(next_element, booking_time, duration)
        insert_value('table_data.csv',['Table '+str(table_num),seat,booking_time])
        return render_template('reservation_successful.html')


if __name__ == '__main__':

    app.run(debug=True)

