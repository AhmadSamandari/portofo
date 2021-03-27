from flask import Flask , render_template , url_for , request , redirect
import csv

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_name(page_name):
    return render_template(page_name)


def save_data_txt(data):
	with open ('database.txt' , mode = 'a') as my_file:
		email = data['email']
		subject = data['subject']
		message = data['message']
		text = my_file.write(f'\n\nemail:{email}\nsubject:{subject}\ntext:{message}')

def save_data_csv(data):
	with open ('database.csv' , mode = 'a', newline = '') as my_file2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_txt = csv.writer(my_file2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csv_txt.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		# save_data_txt(data)
		save_data_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'something is wrong. please try again'


