from os import link
import requests
import lxml.html as html
import links_analyzer
import markdown
import HTML_fix
from datetime import datetime
from os import mkdir

## <--- HIGHLY IMPORTANT ---> ##
XPATH_LINK_EXPIRATION = '//span[@class = "objectStatus stateNone"]/text()'
XPATH_ORIGIN_SOURCE = '//a[@id="externalJobLink"]'
XPATH_JOBID = '//button[@data-jbfejobid]/@data-jbfejobid'
XPATH_HIRING_FOREIGNERS = '//span[@class="fas fa-exclamation fa-stack-1x fa-inverse"]'
XPATH_LMIA_APROVED = '//span[@class="tfw-icon lmia-icon-approved"]'
XPATH_LMIA_PENDING = '//div[@class="disclaimer tfw col-md-12"]/p[2]'
## <--- HIGHLY IMPORTANT ---> ##
#--------------------------------------------------------------------------------------
## <--- DATA SCRAPER ---> ##
XPATH_JOB_TITLE = '//h1[@class="title"]/span[@property="title"]/text()'
XPATH_DATE_POSTED = '//span[@property="datePosted"]/text()'
XPATH_ENTERPRISE_NAME = '//span[@property="hiringOrganization"]/*/*/text()'
XPATH_ENTERPRISE_URL = '//span[@property="name"]/a/@href'
XPATH_STREET_ADDRESS = '//span[@property="streetAddress"]/text()'
XPATH_JOB_CITY = '//span[@property="addressLocality"]/text()'
XPATH_JOB_STATE = '//span[@property="addressRegion"]/text()'
XPATH_WORK_HOURS = '//span[@property="workHours"]/text()'
XPATH_SALARY_BASE = '//span[@property="baseSalary"]//text()'
XPATH_EMAIL = '//div[@id="howtoapply"]/p/a/text()'
XPATH_FULL_OR_PART = '//span[@property="employmentType"]/text()[2]'
XPATH_JOB_VACANCIES = "//span[contains(text(),'vacancies')]/text()"
XPATH_LANG_REQ = '//p[@property="qualification"]/text()'
XPATH_EDU_REQ = '//ul[@property="educationRequirements qualification"]//span[2]/text()'
XPATH_EXP_REQ = '//p[@property="experienceRequirements qualification"]/span[not(@*)]/text()'
XPATH_TASKS = '//div[@property="responsibilities"]/ul//span/text()'
XPATH_SKILLS = '//div[@property="skills"]/ul[1]/li/span/text()'
XPATH_SOFT_SKILLS = '//div[@property="skills"]/ul[2]/li/span/text()'
## <--- DATA SCRAPER ---> ##
stars_rank = 0
temp_info = ''
links = []
offers_num = 1
## <--- Printable variables ---> ##
printable_title = ""
printable_date = ""

## <--- Printable variables ---> ##

#link_base = 'https://www.jobbank.gc.ca/jobsearch/jobposting/'
#link_ID = 36781020
#max_num = link_ID + 100 # << Indica el máximo de páginas a analizar

# Algoritmo: check_expire > check_origin_source > check_hiring_foreigners > check_lmia

def check_expire(link):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home) # < Se obtiene el HTML
            Link_Expiration = parsed.xpath(XPATH_LINK_EXPIRATION) # < Se le pasan los parámetros de XPATH

            if Link_Expiration != []:
                print('La oferta: '+link+' ha expirado\n')
            else:
                #print('La oferta: '+link+" está disponible")
                check_origin_source(link, parsed)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print('La oferta: '+link+" muestra un "+str(ve)+"\n")

def check_origin_source(link, parsed):
    origin_source = parsed.xpath(XPATH_ORIGIN_SOURCE)
    if origin_source != []:
        pass
        #print('La oferta: '+link+" no se origina en JobBank\n")
    else:
        check_hiring_foreigners(link, parsed)

def check_hiring_foreigners(link, parsed):
    hiring_foreigners = parsed.xpath(XPATH_HIRING_FOREIGNERS)
    if hiring_foreigners != []:
        pass
        #print('La oferta: '+link+" no está contratando extranjeros\n")

    else:
        #print('La oferta: '+link+" contrata extranjeros")
        check_lmia(link, parsed)


def check_lmia(link, parsed):
    LMIA_Aproved = parsed.xpath(XPATH_LMIA_APROVED)
    LMIA_Pending = parsed.xpath(XPATH_LMIA_PENDING)
    if LMIA_Aproved != []:
        #print('La oferta: '+link+' tiene aprovado un LMIA\n')
        check_jobtitle(link, parsed)
    elif LMIA_Pending != []:
        print('La oferta: '+link+' tiene pendiente un LMIA\n')
    else:
        print('La oferta: '+link+' No tiene información de LMIA\n')

def check_jobtitle(link, parsed):
    global temp_info
    global printable_title

    jobtitle = parsed.xpath(XPATH_JOB_TITLE)
    printable_title = jobtitle[0]
    temp_info = temp_info + "# "+ str(jobtitle[0])+ "\n"
    #print("# "+str(jobtitle[0]))
    check_date(link, parsed)

def check_date(link, parsed):
    global temp_info
    global printable_date

    job_date = parsed.xpath(XPATH_DATE_POSTED)
    job_date = job_date[0]
    printable_date = job_date
    job_date = job_date.lstrip()
    temp_info = temp_info + str(job_date)+ "\n"
    enterprise_name(link, parsed)

def enterprise_name(link, parsed):
    global temp_info
    global stars_rank

    e_name = parsed.xpath(XPATH_ENTERPRISE_NAME)
    e_url = parsed.xpath(XPATH_ENTERPRISE_URL)

    if e_url != []:
        stars_rank = stars_rank+0.5
    else:
        e_url = "#"

    temp_info = temp_info +"["+str(e_name[0])+"]"+"("+str(e_url[0])+")"+"<br>"
    check_jobid(link, parsed)

def check_jobid(link, parsed):
    JobID = parsed.xpath(XPATH_JOBID)
    JobID = str(JobID[0])
    check_email(link, JobID)

def check_email(link, JobID):
    global temp_info
    global stars_rank

    session = requests.Session()
    response = session.get(link+'?seekeractivity%3Ajobid='+JobID+']&seekeractivity_SUBMIT=1&javax.faces.ViewState=stateless&javax.faces.behavior.event=action&jbfeJobId='+JobID+']&action=applynowbutton&javax.faces.partial.event=click&javax.faces.source=seekeractivity&javax.faces.partial.ajax=true&javax.faces.partial.execute=jobid&javax.faces.partial.render=applynow%20markappliedgroup&seekeractivity=seekeractivity') # I know this line is very large, it is a Query to get the cookies needed to load new job offers
    response = session.get(link)
    home = response.content.decode('utf-8')
    parsed = html.fromstring(home)
    job_email = parsed.xpath(XPATH_EMAIL)
    job_email = str(job_email[0])
    
    temp_info = temp_info + "Contact: "+'<a href="mailto:'+job_email+'">' +job_email+'</a>'+"<br>"
    if "@gmail" in job_email or "@yahoo" in job_email or "@outlook" in job_email or "@hotmail" in job_email or "@aol" in job_email:
        pass
    else:
        stars_rank = stars_rank+2
    #print('Contact: '+job_email)
    #print('\n')
    check_street(link, parsed)

def check_street(link, parsed):
    global temp_info
    street_address = parsed.xpath(XPATH_STREET_ADDRESS)
    if street_address != []:
        street_address = street_address[0]
    else:
        street_address = "No address info"
    temp_info = temp_info + str(street_address)+"<br>"
    #print(str(street_address)+"\n")
    check_city_state(link, parsed)

def check_city_state(link, parsed):
    global temp_info
    city = parsed.xpath(XPATH_JOB_CITY)
    state = parsed.xpath(XPATH_JOB_STATE)
    city_state = str(city[0])+", "+str(state[0])
    temp_info = temp_info + city_state + "\n"
    #print(city_state+"\n")
    work_hours(link, parsed)

def work_hours(link, parsed):
    global temp_info
    job_hours = parsed.xpath(XPATH_WORK_HOURS)
    job_hours = job_hours[0]
    temp_info = temp_info + "#### Details:\n"
    temp_info = temp_info + "*"+str(job_hours)+"\n"
    #print('#### Details:')
    #print("*"+job_hours+"\n")
    salary_base(link, parsed)

def salary_base(link, parsed):
    global temp_info
    salary = parsed.xpath(XPATH_SALARY_BASE)
    try:
        salary = "* "+salary[1]+salary[2]+salary[3]+salary[4]+" CAD"+salary[6]
    except:
        salary = "* "+salary[1]+salary[2]+" CAD"+salary[4]
    
    #print(salary+"\n")

    salary = salary.replace("$", "&dollar;")
    temp_info = temp_info + salary + "\n"
    full_or_part(link, parsed)

def full_or_part(link, parsed):
    global temp_info
    full_or_what = parsed.xpath(XPATH_FULL_OR_PART)
    full_or_what = full_or_what[0]
    full_or_what = full_or_what.lstrip()
    full_or_what = "* "+full_or_what
    temp_info = temp_info + full_or_what
    #print(full_or_what)
    check_vacancies(link, parsed)

def check_vacancies(link, parsed):
    global temp_info
    job_vacancies = parsed.xpath(XPATH_JOB_VACANCIES)
    try:
        job_vacancies = job_vacancies[1]
        job_vacancies = job_vacancies.lstrip()
        job_vacancies = "* "+job_vacancies
    except:
        job_vacancies = "* 1 vacancy"
    
    temp_info = temp_info + job_vacancies + "\n"
    #print(job_vacancies+"\n")
    check_lang(link, parsed)

def check_lang(link, parsed):
    global temp_info
    lang_req = parsed.xpath(XPATH_LANG_REQ)
    lang_req = lang_req[0]
    temp_info = temp_info + "\n#### Requeriments:\n"
    temp_info = temp_info + "* " + lang_req + "\n"
    #print('#### Requeriments')
    #print("* "+lang_req+"\n")
    check_edu(link, parsed)

def check_edu(link, parsed):
    global temp_info
    global stars_rank
    edu_req = parsed.xpath(XPATH_EDU_REQ)
    edu_req = edu_req[0]
    if edu_req == 'No degree, certificate or diploma' and stars_rank != 0:
        stars_rank = stars_rank + 1.25
    temp_info = temp_info + "* " + edu_req + "\n"
    #print("* "+edu_req+"\n")
    check_exp(link, parsed)

def check_exp(link, parsed):
    global temp_info
    global stars_rank
    exp_req = parsed.xpath(XPATH_EXP_REQ)
    exp_req = exp_req[0]
    if exp_req == 'Will train' and stars_rank != 0 or exp_req == 'Experience an asset' and stars_rank != 0:
        stars_rank = stars_rank + 1.25
    temp_info = temp_info + "* " + exp_req + "\n"
    #print("* "+exp_req+"\n")
    check_tasks(link, parsed)

def check_tasks(link, parsed):
    global temp_info
    tasks_req = parsed.xpath(XPATH_TASKS)
    z = 0
    tasks_fixed = '#### Tasks:\n'
    for i in tasks_req:
        tasks_fixed = tasks_fixed + "* "+tasks_req[z]+"\n"
        z = z+1
    temp_info = temp_info + tasks_fixed
    #print(tasks_fixed)
    check_skills(link, parsed)

def check_skills(link, parsed):
    global temp_info
    skills_req = parsed.xpath(XPATH_SKILLS)
    z = 0
    skills_fixed = '#### Skills:\n'
    for i in skills_req:
        skills_fixed = skills_fixed + "* "+skills_req[z]+"\n"
        z = z+1
    temp_info = temp_info + skills_fixed
    #print(skills_fixed)
    check_soft_skills(link, parsed)

def check_soft_skills(link, parsed):
    global temp_info
    global stars_rank
    global offers_num

    global printable_title
    global printable_date

    soft_skills_req = parsed.xpath(XPATH_SOFT_SKILLS)
    z = 0
    soft_skills_fixed = '#### Soft Skills:\n'
    for i in soft_skills_req:
        soft_skills_fixed = soft_skills_fixed + "* "+soft_skills_req[z]+"\n"
        z = z+1
    temp_info = temp_info + soft_skills_fixed+"\n"
    temp_info = temp_info + '**Stars Rank: '+str(stars_rank)+"** <br>"
    temp_info = temp_info + "URL Offer: "+'<a href="'+link+'">'+link+'</a>'+"\n"

    print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
    print('Offer number '+str(offers_num)+' found:\n')
    offers_num = offers_num+1
    print('Job title: '+printable_title)
    print('Date posted: '+printable_date)
    print('Stars Rank: '+str(stars_rank)+"\n")

    stars_rank = 0

def save_data():
    global temp_info
    temp_info =  HTML_fix.html_init + markdown.markdown(temp_info) + HTML_fix.html_ending
    fecha_carpeta = datetime.today().strftime('%d-%m-%y')
    fecha_carpeta = str(fecha_carpeta)
    num_archivo = 1

    while num_archivo != 0:

        try:
            with open(fecha_carpeta+'/'+str(num_archivo)+'.html', 'r+') as f:
                num_archivo = num_archivo+1
        except:

            try:
                mkdir(fecha_carpeta+'/')
                with open(fecha_carpeta+'/'+str(num_archivo)+'.html', 'w+') as f:
                    f.write(temp_info)
                    num_archivo = 0
                
            except:
                with open(fecha_carpeta+'/'+str(num_archivo)+'.html', 'w+') as f:
                    f.write(temp_info)
                    num_archivo = 0

if __name__ == "__main__":
    print('\n ####################################### Coded By @nonskilledeveloper ########################################\n')
    pag_loads = int(input('Write here the number of pages to analyze: '))

    #x = 1
    #while x <= pag_loads:
    #    links_analyzer.get_urls(x)
    #    links = links_analyzer.temp_list
    #    x = x+1

    links_analyzer.get_urls(pag_loads)
    links = links_analyzer.temp_list

    last_check = 0
    while last_check < len(links):
        try:
            check_expire(links[last_check])
            last_check = last_check+1
        except:
            print('Exception: '+ links[last_check])
            Error_Checkpoint = 1
            while Error_Checkpoint == 1:
                try:
                    check_expire(links[last_check+1])
                    last_check = last_check+1
                except:
                    print('Persistent exception: '+links[last_check])
                    last_check = last_check + 1
                    if last_check >= len(links):
                        save_data()
                        quit()
                    pass
            
        
    #for i in links:
    #    check_expire(links[last_check])
    #    last_check = last_check+1
    #last_check = 0

    save_data()
    
#                                       #
#    while link_ID <= max_num:          #
#        link = link_base+str(link_ID)  #
#        check_expire(link)             #
#        link_ID = link_ID+1            #
#                                       #
#        PREV_VERSION                   #