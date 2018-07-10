from django.http import HttpResponseRedirect
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


def vote(request,username):
    form = VotingForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print('-------<>-------')
            choiceID = form.cleaned_data['choiceID']
            user = Profile.objects.get(user__username=username)
            choice = Choice.objects.get(pk=choiceID)
            choice.vote += 1
            question = Question.objects.get(pk=choice.question.id)
            choice.save()
            log = AnswerLog(question=question, profile=user, choice=choice)
            log.save()
            return HttpResponseRedirect('/voting/'+ username)






def showQuestion(request,username):
    profile = Profile.objects.get(user__username=username)
    questions = Question.objects.exclude(answerlog__profile=profile)
    print(questions[0].questionText)
    finalQuestions = questions.filter(creator__in=profile.friends.all()).all()
    print('-------------')
    print(finalQuestions)
    choices = Choice.objects.filter(question=finalQuestions[0])
    # form = VotingForm()
    context = { 'question':finalQuestions[0],'choices':choices,'profile':profile}
    return render(request,'vote.html',context)














