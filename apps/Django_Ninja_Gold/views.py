from django.shortcuts import render, HttpResponse, redirect
# import random
from random import randrange
from datetime import datetime
# Create your views here.
def index(request):
    # if not('gold' in request.session):
    #     print "reset"
    #     reset(request)
    # return render(request, 'django_ninja_gold/index.html')
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if not 'greeting' in request.session:
        request.session['greeting'] = {'greeting': 'Welcome to Coding Dojo'}
    if not 'activities' in request.session:
        request.session['activities'] = []
    return render(request, 'django_ninja_gold/index.html')

def process_money(request, my_data):
    print request.POST
    # my_roll = ['farm', 'cave', 'house', 'casino']
    # print "my_roll is ", my_roll
    my_data = request.POST['data']
    print my_data
    if my_data == 'farm':
        num = randrange(10,20)
        msg = "Earned {} golds from the farm".format(num)
        print msg
    elif my_data == 'cave':
        num = randrange(5,10)
        msg = "Earned {} golds from the cave".format(num)
        print msg
    elif my_data == 'house':
        num = randrange(2,5)
        msg = "Earned {} golds from the house".format(num)
        print msg
    elif my_data == 'casino':
        num = randrange(-50,50)
        if num >=0:
            msg = "Earned {} golds from the casino".format(num)
            print msg
        else:
            msg = "Enter a casino and lost {} golds ....Ouch!!".format(num)
            print msg

    print request.session['gold'] 
    request.session['gold'] += num
    request.session['activities'].append(msg)
    return redirect('/')



    # Which form sent the request?
    # if building == "farm":
    #     #Generate the gold earned or lost
    #     gold_earned = random.randint(10,20)
    #
    #     #New activities string
    #     activity_to_register = "Earned " + str(gold_earned) + " golds from the the farm! " + "(" + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ")"
    #
    #     #Save the dictionary element in the activities list: color and string
    #     request.session['activities'].append({'color':'c-green','activity':activity_to_register})
    #
    #     #Update the amount of gold
    #     request.session['gold'] += gold_earned
    #
    # elif building == "cave":
    #     gold_earned = random.randint(5,10)
    #     activity_to_register = "Earned " + str(gold_earned) + " golds from the the cave! " + "(" + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ")"
    #     request.session['activities'].append({'color':'c-green','activity':activity_to_register})
    #     request.session['gold'] += gold_earned



def reset(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return redirect('/')
