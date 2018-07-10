from django.shortcuts import render
from polls.forms import VotingForm
# Create your views here.
from django.shortcuts import render
from accounts.models import Profile
from polls.models import Question, Choice, AnswerLog


# Create your views here.
def pollPublish(request):
    if request.method == 'GET':
        questionText = request.GET.get('text')
        username = request.GET.get('author')
        answer1 = request.GET.get('answer1')
        answer2 = request.GET.get('answer2')
        answer3 = request.GET.get('answer3')
        answer4 = request.GET.get('answer4')
        user =  Profile.objects.get(user__username=username)
        question = Question.objects.create(creator=user,questionText=questionText)
        question.save()
        choice1 = Choice(question=question,choiceText=answer1)
        choice2 = Choice(question=question,choiceText=answer2)
        choice3 = Choice(question=question,choiceText=answer3)
        choice4 = Choice(question=question,choiceText=answer4)
        choice1.save()
        choice2.save()
        choice3.save()
        choice4.save()


def vote(request,questionID):
    if request.method == 'GET':
        username = request.GET.get('voter')
        user =  Profile.objects.get(user__username=username)
        question =  Question.objects.get(pk = questionID)
        choiceID = request.GET.get('choiceID')
        choice = Choice.objects.get(pk=choiceID)
        choice.vote +=1
        choice.save()
        log = AnswerLog(question=question,profile=user,choice=choice)
        log.save()


def showQuestion(request,username):
    profile = Profile.objects.get(user__username=username)
    questions = Question.objects.exclude(answerlog__profile=profile)
    finalQuestions = questions.filter(creator__in=profile.friends.all())
    form = VotingForm()
    context = { 'form':form}
    return render(request,'vote.html',context)














