import requests
import lxml.html as html

XPATH_TO_DEBUG = '//div[@property="responsibilities"]/ul//span/text()'

link = 'https://www.jobbank.gc.ca/jobsearch/jobposting/36595282?source=searchresults'


try:
    response = requests.get(link)
    if response.status_code == 200:
        d_code = response.content.decode('utf-8')
        parsed = html.fromstring(d_code) # < Se obtiene el HTML
        result_debugged = parsed.xpath(XPATH_TO_DEBUG) # < Se le pasan los parámetros de XPATH

        if result_debugged != []:
            print('\n')
            print(result_debugged)
            print('\n')

            #salary_fixed = 'De '+str(result_debugged[1])+str(result_debugged[2])+' a $'+str(result_debugged[4])
            #print(salary_fixed)

            

        else:
            print('\nEmpty')
    else:

        raise ValueError(f'Error: {response.status_code}')


except ValueError as ve:
    print('La oferta: '+link+" muestra un "+str(ve)+"\n")

######## NOTAS #########
# XPATH_SALARY = //span[@property="baseSalary"]//text()
# salary_fixed = 'De &dollar;'+str(result_debugged[2])+' a &dollar;'+str(result_debugged[4])
# print(salary_fixed)

# XPATH_TASKS = //div[@property="responsibilities"]/ul//span/text()
# z = 0
# tasks_fixed = ''
# for y in result_debugged:
#   tasks_fixed = tasks_fixed + '* '+str(result_debugged[z])+'\n'
#   z = z+1
# print(tasks_fixed)

# XPATH_SKILLS = //div[@property="skills"]/ul[1]/li/span/text()
# z = 0
# skills_fixed = ''
# for y in result_debugged:
#     skills_fixed = skills_fixed + '* '+str(result_debugged[z])+'\n'
#     z = z+1
# print(skills_fixed)

# XPATH_SOFTSKILLS = //div[@property="skills"]/ul[2]/li/span/text()
# z = 0
# softskills_fixed = ''
# for y in result_debugged:
#     softskills_fixed = softskills_fixed + '* '+str(result_debugged[z])+'\n'
#     z = z+1
# print(softskills_fixed)