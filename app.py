{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "618a24ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask,render_template,request \n",
    "import pickle\n",
    "\n",
    "###Loading model and cv\n",
    "cv = pickle.load(open('cv.pkl','rb')) ##loading cv\n",
    "model = pickle.load(open('spam.pkl','rb')) ##loading model\n",
    "\n",
    "app = Flask(__name__) ## defining flask name\n",
    "\n",
    "@app.route('/') ## home route\n",
    "def home():\n",
    "    return render_template('index.html') ##at home route returning index.html to show\n",
    "\n",
    "@app.route('/predict',methods=['POST']) ## on post request /predict \n",
    "def predict():\n",
    "    if request.method=='POST':     \n",
    "        mail = request.form['email']  ## requesting the content of the text field\n",
    "        data = [mail] ## converting text into a list\n",
    "        vect = cv.transform(data).toarray() ## transforming the list of sentence into vecotor form\n",
    "        pred = model.predict(vect) ## predicting the class(1=spam,0=ham)\n",
    "        return render_template('result.html',prediction=pred) ## returning result.html with prediction var value as class value(0,1)\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)     ## running the flask app as debug==True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4bf98935",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
