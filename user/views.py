from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q

from .models import Experience, Profile, Executivecommittiee, Moderator
from .forms import CustomUserCreationForm, EducationForm, ExperienceForm, ProfileForm, SkillForm
from .utils import paginateItems, searchItems

# Create your views here.

def home(request):
    return render(request, 'main.html')

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')

        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'user/login_register.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('edit-account')

        else:
            messages.error(
                request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'user/login_register.html', context)


# def profiles(request):
#     profiles, search_query = searchProfiles(request)

#     custom_range, profiles = paginateProfiles(request, profiles, 3)
#     context = {'profiles': profiles, 'search_query': search_query,
#                'custom_range': custom_range}
#     return render(request, 'users/profiles.html', context)

def moderators(request):

    ec_all = Moderator.objects.all()
    ec_year = ec_all[0]

    context = {
        'ec_all': ec_all, 'ec_year': ec_year,
    }

    return render(request, 'user/moderator.html', context)

def moderator(request, pk):

    ec_all = Moderator.objects.all()
    ec_year = Moderator.objects.get(id = pk)

    context = {
        'ec_all': ec_all, 'ec_year': ec_year,
    }

    return render(request, 'user/moderator.html', context)


def executiveCommittees(request):

    ec_all = Executivecommittiee.objects.all()
    ec_year = ec_all[0]

    context = {
        'ec_all': ec_all, 'ec_year': ec_year,
    }

    return render(request, 'user/executive-committee.html', context)

def executiveCommittee(request, pk):

    ec_all = Executivecommittiee.objects.all()
    ec_year = Executivecommittiee.objects.get(id = pk)

    context = {
        'ec_all': ec_all, 'ec_year': ec_year,
    }

    return render(request, 'user/executive-committee.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile

    ec_obj = []
    
    p = profile.president.all()
    vp = profile.vice_president.all()
    gs = profile.general_secretary.all()
    js = profile.joint_secretary.all()
    tr = profile.treasurer.all()
    ec = profile.event_coordinator.all()
    hol = profile.head_of_logistics.all()

    mod1 = profile.moderator_one.all()
    mod2 = profile.moderator_two.all()
    mod3 = profile.moderator_three.all()

    container = [p, vp, gs, js, tr, ec, hol, mod1, mod2, mod3]

    for scon in container:
        if len(scon) > 0:
            print(len(scon))
            for s in scon:
                ec = ec_obj.append(s)

    skills = profile.skill_set.all()
    educations = profile.education_set.all()
    experiences = profile.experience_set.all()

    context = {'profile': profile, 'skills': skills, 'educations': educations, 'experiences': experiences, 'ec_container': ec_obj}
    return render(request, 'user/account.html', context)



def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topSkills': topSkills,
               "otherSkills": otherSkills}

    # context = {'profile': profile}
    
    return render(request, 'user/user-profile.html', context)
    # return render(request, 'user/user-profile.html')



@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    form_header = "Edit Account"

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form, 'form_header': form_header}
    return render(request, 'user/dynamic_form.html', context)

#start experience

@login_required(login_url='login')
def createExperience(request):
    profile = request.user.profile
    form = ExperienceForm()

    form_header = "Add Experience"

    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.owner = profile
            experience.save()
            messages.success(request, 'Experience was added successfully!')
            return redirect('account')

    context = {'form': form, 'form_header': form_header}
    return render(request, 'user/dynamic_form.html', context)


@login_required(login_url='login')
def updateExperience(request, pk):
    profile = request.user.profile
    experience = profile.experience_set.get(id=pk)
    form = ExperienceForm(instance=experience)

    form_header = "Edit Experience"

    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            messages.success(request, 'Experience was updated successfully!')
            return redirect('account')

    context = {'form': form, 'form_header': form_header}
    return render(request, 'user/dynamic_form.html', context)


@login_required(login_url='login')
def deleteExperience(request, pk):
    profile = request.user.profile
    experience = profile.experience_set.get(id=pk)
    if request.method == 'POST':
        experience.delete()
        messages.success(request, 'Experience was deleted successfully!')
        return redirect('account')

    context = {'object': experience}
    return render(request, 'delete_template.html', context)



#end experience

@login_required(login_url='login')
def createEducation(request):
    profile = request.user.profile
    form = EducationForm()

    form_header = "Add Education"

    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.owner = profile
            education.save()
            messages.success(request, 'Education was added successfully!')
            return redirect('account')

    context = {'form': form, 'form_header': form_header}
    return render(request, 'user/dynamic_form.html', context)


@login_required(login_url='login')
def updateEducation(request, pk):
    profile = request.user.profile
    education = profile.education_set.get(id=pk)
    form = EducationForm(instance=education)

    form_header = "Edit Education"

    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            messages.success(request, 'Education was updated successfully!')
            return redirect('account')

    context = {'form': form, 'form_header': form_header}
    return render(request, 'user/dynamic_form.html', context)


@login_required(login_url='login')
def deleteEducation(request, pk):
    profile = request.user.profile
    education = profile.education_set.get(id=pk)
    if request.method == 'POST':
        education.delete()
        messages.success(request, 'Education was deleted successfully!')
        return redirect('account')

    context = {'object': education}
    return render(request, 'delete_template.html', context)


## Education

@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()

    form_header = "Add Skill"

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill was added successfully!')
            return redirect('account')

    context = {'form': form, 'form_header': form_header}
    return render(request, 'user/dynamic_form.html', context)


@login_required(login_url='login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    form_header = "Edit skill"

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated successfully!')
            return redirect('account')

    context = {'form': form, 'form_header': form_header}
    return render(request, 'user/dynamic_form.html', context)


@login_required(login_url='login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill was deleted successfully!')
        return redirect('account')

    context = {'object': skill}
    return render(request, 'delete_template.html', context)


def searchMe(request):
    items, search_query, item = searchItems(request)
    custom_range, items = paginateItems(request, items, 10)
    type_pro = ['Student', 'Alumni']

    print(item)

    context = {
        'profiles': items,
        'search_query': search_query,
        'item': item,
        'custom_range': custom_range,
        'type_pro': type_pro
    }

    return render(request, 'user/search-me.html', context)

# @login_required(login_url='login')
# def inbox(request):
#     profile = request.user.profile
#     messageRequests = profile.messages.all()
#     unreadCount = messageRequests.filter(is_read=False).count()
#     context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
#     return render(request, 'users/inbox.html', context)


# @login_required(login_url='login')
# def viewMessage(request, pk):
#     profile = request.user.profile
#     message = profile.messages.get(id=pk)
#     if message.is_read == False:
#         message.is_read = True
#         message.save()
#     context = {'message': message}
#     return render(request, 'users/message.html', context)


# def createMessage(request, pk):
#     recipient = Profile.objects.get(id=pk)
#     form = MessageForm()

#     try:
#         sender = request.user.profile
#     except:
#         sender = None

#     if request.method == 'POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             message = form.save(commit=False)
#             message.sender = sender
#             message.recipient = recipient

#             if sender:
#                 message.name = sender.name
#                 message.email = sender.email
#             message.save()

#             messages.success(request, 'Your message was successfully sent!')
#             return redirect('user-profile', pk=recipient.id)

#     context = {'recipient': recipient, 'form': form}
#     return render(request, 'users/message_form.html', context)