from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Solution, Answer, SolutionLike, Plan, Student
from jdatetime import datetime
from django.utils import timezone as Tz
from pytz import timezone
from .decorators import virtualExamNotEnded
from django.core.paginator import Paginator
from exam.models import Question, virtualExam
from django.db.models import Q
import random


def Home(request):
    return render(request, 'home/home.html',context={'title':'Home','HT':'صفحه اصلی'})


    
@login_required
def Announcement(request):
    return render(request, 'home/announcment.html',context={'title':'Announcment','HT':'اطلاعیه'})

@login_required
def Solution_view(request):
    context={'title':'Solution','HT':'رفع اشکال'}
    if request.method =='POST':
        data = request.POST
        files = request.FILES
        action = data['action']
        if action == 'add-Q':
            if 'image' in files.keys():
                s= Solution.objects.create(sender = request.user,
                                        moredata = files['image'],
                                        content = data['content'],
                                        title =data['title'],
                                        grade = data['grade'],
                                        unit=data['unit']
                                        )
            else:
                s= Solution.objects.create(sender = request.user,
                                        content = data['content'],
                                        title =data['title'],
                                        grade = data['grade'],
                                        unit=data['unit']
                                        )
            context['Q-pk'] = s.pk
            messages.success(request,f'شماره شما با ایدی {s.pk} با موفقیت ثبت شد')
        elif action == 'like-Q':
            Q = Solution.objects.get(pk = data['item'])
            try:
                like = SolutionLike.objects.get(s = Q)
                like.delete()
            except:
                like = SolutionLike.objects.create(s = Q, lover = request.user)
        return JsonResponse(context)
    else:
        your_S = Solution.objects.filter(sender = request.user)
        
        myquestions = []
        for q in your_S:
            dc = q.create_time
            ltz = timezone('Asia/Tehran')
            dc = dc.astimezone(ltz)
            pdt = datetime.fromgregorian(datetime = dc)
            time = pdt.strftime('%Y/%m/%d - %H:%M')
            data =  {
                    'title': q.title,
                    'content':q.content,
                    'time':time,
                    'pos':q.position,
                    'pk':q.pk
                }
            if q.moredata:
                data['MD'] = q.moredata.url
            myquestions.append(data)
        
        
        publishedQuestions = Solution.objects.filter(publish = True)
        publishedQs = []
        for q in publishedQuestions:
            dc = q.create_time
            ltz = timezone('Asia/Tehran')
            dc = dc.astimezone(ltz)
            pdt = datetime.fromgregorian(datetime = dc)
            time = pdt.strftime('%Y/%m/%d')
            
            if q.sender.full_name != '':
                username = q.sender.full_name
            else:
                username = q.sender.username
            liked = False
            try:
                SolutionLike.objects.get(s = q, lover = request.user)
                liked = True
            except:
                pass
            
            
            data =  {
                    'title': q.title,
                    'username':username,
                    'content':q.content,
                    'time':time,
                    'pos':q.position,
                    'grade':q.grade,
                    'unit':q.unit,
                    'liked':liked,
                    'likes':SolutionLike.objects.filter(s=q).count(),
                    'pk':q.pk,
                }
            try:
                answer = q.answer
                data['subject'] = answer.subject
            except:
                pass
            publishedQs.append(data)
        if publishedQuestions.count()> 0:
            print(publishedQuestions)
            context['otherQs'] = publishedQs
        if your_S.count() > 0:
            context['myQs'] = myquestions
        return render(request, 'home/solution.html',context=context)
@login_required
def Solution_Question_view(request, pk):
    context = {'title': f'Q - {pk}', 'HT':f'سوال - {pk}',}
    question = Solution.objects.get(pk= pk)
    if request.method =='POST':
        files = request.FILES
        data = request.POST
        action = data['action']
        if action == 'add-answer':
            try: 
                answer = Answer.objects.get(problom = question)
                if 'file' in files.keys():
                    answer.content = data['content']
                    answer.file = files['file']
                    answer.subject = data['subject']
                else: 
                    answer.content = data['content']
                    answer.subject = data['subject']
                    answer.file = None
                answer.save()
            except:
                if 'file' in files.keys():
                    Answer.objects.create(problom = question,
                                        content = data['content'],
                                        file = files['file'],
                                        subject = data['subject']
                    )
                else: 
                    Answer.objects.create(problom = question,
                                        content = data['content'],
                                        subject = data['subject']
                    )                        
        elif action == 'delete':
            question.delete()
        elif action == 'publish':
            if question.publish:
                question.publish = False
            else:
                question.publish = True
            question.save()
        elif action =='close':
            if question.position =='باز':
                question.position ='بسته'
                question_link = 'SOON'
                student_name = question.sender.get_name
                question_Id = str(pk)
                line1 = f'سلام {student_name}'
                line2 = f' سوال شما با ایدی {question_Id} توسط تیم پشتیبانی حل شده و جواب ان برای شما قرار گرفته شده برای مشاهده جواب به وبسایت مراجعه کنید '
                line3 = f'لینک سوال: {question_link}'
                line4 = f'Chemistry Kiani'
                question_sms = line1 +'\n'+line2+'\n'+line3+'\n\n'+line4
                print(question.sender.send_sms(question_sms))
            else:
              question.position ='باز'
            question.save()
        return JsonResponse(context)
    else:
        entime = question.create_time
        localtimezone = timezone('Asia/Tehran')
        entime = entime.astimezone(localtimezone)
        fatime = datetime.fromgregorian(datetime=entime)

        DATA ={
            'title':question.title,
            'content':question.content,
            'time': fatime.strftime('%Y/%m/%d ~ %H:%M'),
            'sender':question.sender,
            'publish':question.publish,
            'pk':question.pk,
            'pos':question.position
        }

        if question.moredata:
            DATA['moredata']= question.moredata

        context['Q'] = DATA
        perm = False
        if request.user.groups.filter(name = 'Solutionist').count() > 0:
            perm = True

        try:
            answer =  Answer.objects.get(problom = question)
            context['answer'] = answer
        except:
            pass
        context['perm'] = perm

        similarQS = Solution.objects.filter()
        return render(request, 'home/question_view.html', context)

def Plans_view(request):
    context = {'title':'Plans','HT':'پلن ها'}
    plans = Plan.objects.all()
    cooked_plans = []
    for plan in plans:
        cooked_plans.append({
            'name': plan.name,
            'features': plan.features,
            'price': plan.price
        })
    context['plans'] = cooked_plans 

    return render(request, 'home/plans.html', context=context)

@login_required
def Question_bank(request):
    context = {'title':'Q-Bank','HT':'بانک سوالات'}
    if request.method == 'POST':
        DATA = request.POST
        action = DATA['action']

        if action == 'createExam':
            etime = int(DATA['etime'])
            ecount = int(DATA['ecount'])
            ediff = DATA['ediff']
            efilters = DATA['efilters'].split(',')
            filt = []
            ERR = 'None'
            for i in efilters:
                if i == 'T':
                    filt.append(True)
                else:
                    filt.append(False)
            filer = {
                'دهم': filt[0],
                'یازدهم': filt[1],
                'دوازدهم': filt[2],
                'اول': filt[3],
                'دوم': filt[4],
                'سوم': filt[5],
                'چهارم': filt[6]
            }
            
            grade_filter = []
            all_filters = ''

            for i in ['دهم','یازدهم','دوازدهم']:
                if filer[i]:
                    grade_filter.append(i)
                    all_filters += i+','

            unit_filter = []
            for i in ['اول','دوم','سوم','چهارم']:
                if filer[i]:
                    unit_filter.append(i)
                    all_filters += i + ','
            all_filters = all_filters[:-1]

            questions_grade = Question.objects.filter(
                Grade__in = grade_filter
            )
            
            filtered_questions = questions_grade.filter(
                Unit__in = unit_filter
            )
            
            

            diffs = {
                '1': 'ساده',
                '2': 'متوسط',
                '3': 'سخت'
            }
            main_diff_questions = []
            if len(filtered_questions) >= ecount:
                for q in filtered_questions:
                    diff_percent = int(q.difficulty.split(',')[0])
                    
                    if diff_percent < 33 and ediff == '1':
                        main_diff_questions.append(q)
                    elif 33 < diff_percent < 66 and ediff == '2':
                        main_diff_questions.append(q)
                    elif 66 < diff_percent < 99 and ediff == '3':
                        main_diff_questions.append(q)
                    
                filtered_questions = [x for x in filtered_questions if x not in main_diff_questions]

                registered_questions = []
                used_questions_diff = []
                used_questions_filtered = []
                while len(registered_questions) < ecount:
                    if len(registered_questions) < len(main_diff_questions):
                        randomNum = random.randint(0, len(main_diff_questions)-1)
                        if randomNum not in used_questions_diff:
                            registered_questions.append(main_diff_questions[randomNum])
                            used_questions_diff.append(randomNum)
                    else:
                        randomNum = random.randint(0, len(filtered_questions)-1)
                        if randomNum not in used_questions_filtered:
                            registered_questions.append(filtered_questions[randomNum])
                            used_questions_filtered.append(randomNum)
                        
                vExam = virtualExam.objects.create(
                    time = etime,
                    filters = all_filters,
                    status = 'not_started',
                    difficulty = diffs[ediff],
                    studentRelated = request.user
                )

                for q in registered_questions:
                    vExam.questions.add(q)
                
            else:
                ERR = 'filter'
            context['ERR'] = ERR
        return JsonResponse(context)
    else:
        admin= False
        if request.user.groups.filter(name='Admin').count()> 0 :
            admin = True
        context['admin'] = admin

        questions = Question.objects.filter (
            Q(exam_related__isnull = True)|Q(exam_related__status = 'Ended')
        )
        page_num = request.GET.get('page')
        paginator = Paginator(questions, 10)
        questions = paginator.get_page(page_num)
        context['questions']= questions


        now_time = Tz.now()
        localtimezone = timezone('Asia/Tehran')
        entim = now_time.astimezone(localtimezone)
        fatim = datetime.fromgregorian(datetime=entim).strftime('%Y/%m/%d')
        context['time'] = fatim
        return render(request, 'home/questionbank.html', context=context)

@login_required
def Question_view(request, pk):
    question = Question.objects.get(pk= pk)
    context = {'title':f'Q - {pk}', 'HT': f'سوال {pk}'}
    if request.method == 'POST':
        context = {}
        
        question.difficulty_add(request.POST['diff'], request.user)
        diff ,_ =question.difficulty.split(',')
        context['othersdiff'] = diff
        question.voting.add(request.user)
        return JsonResponse(context)
    else:
        question_diff, counter  = question.difficulty.split(',')
        question_diff = int(question_diff)
        voted = False
        if request.user in question.voting.all():
            voted = True

        diffs = [True, False, False]
        if question_diff > 33:
            diffs[1] = True
            if question_diff > 66:
                diffs[2] = True
        questionDesc = ''
        if question.exam_related:
            examname = str(question.exam_related.name)
            print(examname)
            questionDesc = f'سوال آزمون <a href="/exam/{examname}" class="exam-link">{examname}</a>'
        else: 
            questionDesc = f'سوال {question.Grade} فصل {question.Unit}'
        
        time = question.date_submited
        localtimezone = timezone('Asia/Tehran')
        entime = time.astimezone(localtimezone)
        fatime = datetime.fromgregorian(datetime=entime)

        questiondic = {
            'Question' : question.Question,
            'Desc': questionDesc,
            'diffs': diffs,
            'diff_percent': question_diff,
            'pk':question.pk,
            'Answer': 'گزینه '+ question.Answer,
            'voted':voted,
            'time':fatime.strftime('%Y/%m/%d'),
            'grade':question.Grade,
            'unit':question.Unit
        }
        if question.get_solution != False:
            questiondic['solution'] = question.get_solution
        context['question'] = questiondic


        return render(request, 'home/questionbank-question-view.html', context=context)
@login_required
def VirtualExam(request):
    context = {'title':'Virtual Exam', 'HT':' آزمون آزمایشی'}

    exams = virtualExam.objects.all().order_by('date_created')
    
    paginator = Paginator(exams, 10)
    page_num = request.GET.get('page')
    exams = paginator.get_page(page_num)

    exams_list = []
    for exam in exams:
        exam_detail = {
            'date': exam.get_date,
            'filters': exam.get_filters,
            'fastatus': exam.fastatus,
            'status':exam.status,
            'question_count': exam.questions_count,
            'time':exam.time,
            'diff':exam.difficulty,
            'pk':exam.pk,
            'result':exam.result
        }
            
        exams_list.append(exam_detail)
    context['exams'] = exams_list
    return render(request, 'home/virtualexam.html', context)

@virtualExamNotEnded
@login_required
def virtualExamPage(request, pk):
    ve = virtualExam.objects.get(pk= pk)
    context = {'title': 'Exam - #'+pk , 'HT':'#'+'آزمون '+pk}
    if request.method == 'POST':
        keys = request.POST['key']
        ve.keys = keys
        ve.status ='ended'
        ve.save()
        context['ended'] = 'true'
        return JsonResponse(context)
    else:
        context['exam'] = ve
        if ve.status != 'started':
            ve.status = 'started'
            ve.save()
        return render(request, 'home/virtualexampage.html', context)
def virtualExamResultQuestions(request,pk): 
    wrongs_q = []
    corrects_q =[]
    notAnswered_q =[]

    exam = virtualExam.objects.get(pk = pk)
    result = exam.result

    for q in result['not_anwered_pk']:
        notAnswered_q.append(Question.objects.get(pk=q))
    for q in result['corrects_pk']:
        corrects_q.append(Question.objects.get(pk=q))
    for q in result['wrongs_pk']:
        wrongs_q.append(Question.objects.get(pk=q))
        
    return render(request,'exam/result_questions.html',context={'title':'Questions',
                                                                    'HT':'سوالات آزمون',
                                                                    'wrongs':wrongs_q,
                                                                    'corrects':corrects_q,
                                                                    'notAnswered':notAnswered_q
                                                                    })